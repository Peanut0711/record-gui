#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import subprocess
import threading
import queue
import json
import time
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
                              QInputDialog, QLineEdit, QTableWidgetItem, QLabel, 
                              QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QWidget,
                              QTabWidget, QTextEdit)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QSize, QUrl, Signal, QObject
from PySide6.QtGui import QPixmap, QImage, QIcon, QAction, QDesktopServices
import requests
from io import BytesIO
import warnings
import logging

class StreamRecorder(QObject):
    status_changed = Signal(str, str)  # (url, status)
    progress_changed = Signal(str, str)  # (url, progress)
    metadata_received = Signal(dict)  # 메타데이터
    log_message = Signal(str)  # 로그 메시지
    size_changed = Signal(str, int)  # (url, size_bytes)
    
    def __init__(self, url, output_dir, username=None, password=None):
        super().__init__()
        self.url = url
        self.output_dir = output_dir  # 디렉토리만 저장
        self.output_path = None  # 실제 파일 경로는 메타데이터 획득 후 설정
        self.username = username
        self.password = password
        self.process = None
        self.is_running = False
        self.status_queue = queue.Queue()
        self.metadata = None
        self._table_row = None
        
    def get_metadata(self):
        """스트림의 메타데이터를 가져옵니다."""
        cmd = ["streamlink", "--json"]
        if self.username and self.password:
            cmd.extend(["--soop-username", self.username, "--soop-password", self.password])
        cmd.append(self.url)
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                try:
                    metadata = json.loads(result.stdout)
                    self.metadata = metadata
                    
                    # 메타데이터를 받은 후 파일명 설정
                    stream_metadata = metadata.get('metadata', {})
                    author = stream_metadata.get('author', 'unknown')
                    title = stream_metadata.get('title', 'untitled')
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                    
                    # 파일명 생성
                    filename = f"[{author}] {timestamp} {title}.ts"
                    # 파일명에서 사용할 수 없는 문자 제거
                    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
                    self.output_path = os.path.join(self.output_dir, filename)
                    
                    # 파일명 로깅
                    self.log_message.emit(f"녹화 파일명 설정: {filename}")
                    print(f"녹화 파일명 설정: {filename}")
                    
                    self.metadata_received.emit(metadata)
                    return metadata
                except json.JSONDecodeError as e:
                    error_msg = f"메타데이터 파싱 실패: {str(e)}"
                    self.status_changed.emit(self.url, error_msg)
                    self.log_message.emit(error_msg)
            else:
                error_msg = f"메타데이터 가져오기 실패: {result.stderr}"
                self.status_changed.emit(self.url, error_msg)
                self.log_message.emit(error_msg)
        except Exception as e:
            error_msg = f"메타데이터 오류: {str(e)}"
            self.status_changed.emit(self.url, error_msg)
            self.log_message.emit(error_msg)
        return None
        
    def start(self):
        if self.is_running:
            return
            
        # 먼저 메타데이터 확인
        if not self.get_metadata():
            return
            
        self.is_running = True
        self.status_changed.emit(self.url, "시작 중...")
        
        # streamlink 명령어 구성
        cmd = ["streamlink"]
        if self.username and self.password:
            cmd.extend(["--soop-username", self.username, "--soop-password", self.password])
        cmd.extend([self.url, "best", "-o", self.output_path])
        
        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                bufsize=1
            )
            
            # 출력 모니터링 스레드 시작
            threading.Thread(target=self._monitor_output, daemon=True).start()
            
            # 파일 저장 확인 스레드 시작
            threading.Thread(target=self._check_file_save, daemon=True).start()
            
        except Exception as e:
            self.status_changed.emit(self.url, f"오류: {str(e)}")
            self.is_running = False
            
    def stop(self):
        if self.process and self.is_running:
            try:
                # 먼저 정상 종료 시도
                self.process.terminate()
                self.process.wait(timeout=5)  # 최대 5초 대기
            except subprocess.TimeoutExpired:
                # 정상 종료가 안되면 강제 종료
                self.process.kill()
                self.process.wait()
            
            self.is_running = False
            self.status_changed.emit(self.url, "중지됨")
            
            # 녹화 파일 최종 확인
            if os.path.exists(self.output_path):
                final_size = os.path.getsize(self.output_path)
                if final_size > 0:
                    self.log_message.emit(f"녹화 완료: {self.output_path}")
                    self.log_message.emit(f"최종 파일 크기: {final_size / (1024*1024):.2f}MB")
                else:
                    self.log_message.emit("경고: 녹화 파일이 비어있습니다.")
            else:
                self.log_message.emit("경고: 녹화 파일이 생성되지 않았습니다.")
            
    def _monitor_output(self):
        while self.is_running:
            line = self.process.stdout.readline()
            if not line and self.process.poll() is not None:
                break
                
            if line:
                # 상태 메시지 파싱 및 처리
                if "error" in line.lower():
                    self.status_changed.emit(self.url, f"오류: {line.strip()}")
                elif "stream" in line.lower():
                    self.status_changed.emit(self.url, line.strip())
                # 진행률 정보가 있다면 처리
                if "progress" in line.lower():
                    self.progress_changed.emit(self.url, line.strip())
                    
        if self.is_running:
            self.is_running = False
            self.status_changed.emit(self.url, "완료")
            
    def _check_file_save(self):
        """파일이 제대로 저장되는지 확인합니다."""
        time.sleep(2)  # 녹화 시작 대기
        
        if not os.path.exists(self.output_path):
            self.status_changed.emit(self.url, "경고: 파일이 생성되지 않았습니다.")
            self.log_message.emit("경고: 녹화 파일이 생성되지 않았습니다.")
            return
            
        last_size = 0
        no_growth_count = 0
        initial_check = True
        
        while self.is_running:
            if not os.path.exists(self.output_path):
                self.status_changed.emit(self.url, "경고: 파일이 삭제되었습니다.")
                self.log_message.emit("경고: 녹화 파일이 삭제되었습니다.")
                break
                
            current_size = os.path.getsize(self.output_path)
            
            # 초기 파일 생성 확인
            if initial_check:
                if current_size > 0:
                    self.log_message.emit(f"녹화 파일 생성됨: {self.output_path}")
                    self.log_message.emit(f"초기 파일 크기: {current_size / (1024*1024):.2f}MB")
                    initial_check = False
                else:
                    self.log_message.emit("경고: 파일이 생성되었지만 크기가 0입니다.")
            
            if current_size == last_size:
                no_growth_count += 1
                if no_growth_count >= 5:  # 5초 동안 파일 크기가 변하지 않으면
                    self.status_changed.emit(self.url, "경고: 파일이 더 이상 저장되지 않습니다.")
                    self.log_message.emit("경고: 5초 동안 파일 크기가 증가하지 않았습니다.")
                    break
            else:
                no_growth_count = 0
            
            last_size = current_size
            # 용량 시그널 전송
            self.size_changed.emit(self.url, current_size)
            time.sleep(1)
            
    def update_status(self, url, status):
        # 상태 표시 업데이트
        self.ui.statusLabel.setText(status)
        
    def update_progress(self, url, progress):
        # 진행률 업데이트
        try:
            if "progress" in progress.lower():
                percent = int(re.search(r'(\d+)%', progress).group(1))
                self.ui.progressBar.setValue(percent)
        except:
            pass
            
    def update_metadata(self, metadata):
        """메타데이터를 UI에 표시하고, 테이블의 경로 컬럼을 갱신합니다."""
        if metadata:
            stream_metadata = metadata.get('metadata', {})
            author = stream_metadata.get('author', '알 수 없음')
            title = stream_metadata.get('title', '알 수 없음')
            info_text = f"{author} - {title}"
            
            # 메타데이터를 상태 레이블에 표시
            self.ui.statusLabel.setText(info_text)
            
            # 로그에도 출력
            self.log(f"스트림 정보: {info_text}")
            
            # 테이블의 경로 컬럼 갱신
            # 현재 녹화 중인 url로 recorder를 찾고, row 인덱스도 가져옴
            url = self.ui.urlInput.text().strip()
            recorder = self.recorders.get(url)
            if recorder and hasattr(recorder, '_table_row'):
                row = recorder._table_row
                self.ui.recordList.setItem(row, 3, QTableWidgetItem(recorder.output_path))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # UI 파일 로드
        ui_file_name = "ui/main_window.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
            
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()
        
        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)
            
        # 로그 탭 추가
        self.setup_log_tab()
            
        # 녹화 작업 관리
        self.recorders = {}  # url -> StreamRecorder
        
        # UI 이벤트 연결
        self.ui.startButton.clicked.connect(self.start_recording)
        self.ui.stopButton.clicked.connect(self.stop_recording)
        
        # UI 표시
        self.ui.show()
        
        # recordList 테이블에 용량 컬럼 추가 (초기화 시)
        self.ui.recordList.setColumnCount(6)
        self.ui.recordList.setHorizontalHeaderLabels(["URL", "상태", "시작시간", "경로", "용량", "중지"])
        
    def setup_log_tab(self):
        """로그 탭을 설정합니다."""
        # 기존 탭 위젯 찾기
        tab_widget = self.ui.findChild(QTabWidget)
        if not tab_widget:
            # 탭 위젯이 없는 경우 새로 생성
            tab_widget = QTabWidget()
            self.ui.setCentralWidget(tab_widget)
            
            # 기존 위젯들을 메인 탭으로 이동
            main_tab = QWidget()
            main_layout = QVBoxLayout()
            main_layout.addWidget(self.ui)
            main_tab.setLayout(main_layout)
            tab_widget.addTab(main_tab, "메인")
            
        # 로그 탭 추가
        log_tab = QWidget()
        log_layout = QVBoxLayout()
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        log_layout.addWidget(self.log_text)
        log_tab.setLayout(log_layout)
        tab_widget.addTab(log_tab, "로그")
        
    def log(self, message):
        """로그 메시지를 추가합니다."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        self.log_text.append(log_message)
        
    def start_recording(self):
        url = self.ui.urlInput.text().strip()
        if not url:
            QMessageBox.warning(self.ui, "경고", "URL을 입력해주세요.")
            return
            
        # 저장 경로 설정
        save_path = self.ui.savePathInput.text()
        if not save_path:
            save_path = QFileDialog.getExistingDirectory(self.ui, "저장 경로 선택")
            if not save_path:
                return
            self.ui.savePathInput.setText(save_path)
        
        # 로그인 정보 가져오기
        username = self.ui.soopIdInput.text() if self.ui.idPwRadio.isChecked() else None
        password = self.ui.soopPwInput.text() if self.ui.idPwRadio.isChecked() else None
        
        # 녹화 시작 (파일명은 메타데이터 획득 후 설정)
        recorder = StreamRecorder(url, save_path, username, password)
        recorder.status_changed.connect(self.update_status)
        recorder.progress_changed.connect(self.update_progress)
        recorder.metadata_received.connect(self.update_metadata)
        recorder.log_message.connect(self.log)
        recorder.size_changed.connect(self.update_size)
        
        self.recorders[url] = recorder
        recorder.start()
        
        # UI 상태 업데이트
        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)
        
        # 테이블에 정보 추가 (URL/상태/시작시간/경로/용량/중지버튼)
        row = self.ui.recordList.rowCount()
        self.ui.recordList.insertRow(row)
        self.ui.recordList.setItem(row, 0, QTableWidgetItem(url))  # URL
        self.ui.recordList.setItem(row, 1, QTableWidgetItem("녹화중"))  # 상태
        self.ui.recordList.setItem(row, 2, QTableWidgetItem(datetime.now().strftime("%Y-%m-%d %H:%M")))  # 시작시간
        self.ui.recordList.setItem(row, 3, QTableWidgetItem("메타데이터 대기중"))  # 경로(메타데이터 후 갱신)
        self.ui.recordList.setItem(row, 4, QTableWidgetItem("0 MB"))  # 용량
        stop_btn = QPushButton("중지")
        def stop_this_recording():
            recorder.stop()
            self.ui.recordList.setItem(row, 1, QTableWidgetItem("중지됨"))  # 상태 컬럼 업데이트
        stop_btn.clicked.connect(stop_this_recording)
        self.ui.recordList.setCellWidget(row, 5, stop_btn)
        
        # row 인덱스를 recorder에 저장해서 메타데이터 후 경로 갱신에 사용
        recorder._table_row = row

    def stop_recording(self):
        url = self.ui.urlInput.text().strip()
        if url in self.recorders:
            self.recorders[url].stop()
            self.ui.startButton.setEnabled(True)
            self.ui.stopButton.setEnabled(False)
            
    def update_status(self, url, status):
        # 상태 표시 업데이트
        self.ui.statusLabel.setText(status)
        
    def update_progress(self, url, progress):
        # 진행률 업데이트
        try:
            if "progress" in progress.lower():
                percent = int(re.search(r'(\d+)%', progress).group(1))
                self.ui.progressBar.setValue(percent)
        except:
            pass
            
    def update_metadata(self, metadata):
        """메타데이터를 UI에 표시하고, 테이블의 경로 컬럼을 갱신합니다."""
        if metadata:
            stream_metadata = metadata.get('metadata', {})
            author = stream_metadata.get('author', '알 수 없음')
            title = stream_metadata.get('title', '알 수 없음')
            info_text = f"{author} - {title}"
            
            # 메타데이터를 상태 레이블에 표시
            self.ui.statusLabel.setText(info_text)
            
            # 로그에도 출력
            self.log(f"스트림 정보: {info_text}")
            
            # 테이블의 경로 컬럼 갱신
            # 현재 녹화 중인 url로 recorder를 찾고, row 인덱스도 가져옴
            url = self.ui.urlInput.text().strip()
            recorder = self.recorders.get(url)
            if recorder and hasattr(recorder, '_table_row'):
                row = recorder._table_row
                self.ui.recordList.setItem(row, 3, QTableWidgetItem(recorder.output_path))

    def update_size(self, url, size_bytes):
        # 용량 컬럼 갱신
        recorder = self.recorders.get(url)
        if recorder and hasattr(recorder, '_table_row'):
            row = recorder._table_row
            size_mb = size_bytes / (1024*1024)
            self.ui.recordList.setItem(row, 4, QTableWidgetItem(f"{size_mb:.2f} MB"))

    def closeEvent(self, event):
        # 모든 녹화 중지
        for recorder in self.recorders.values():
            if recorder.is_running:
                recorder.stop()
        event.accept()  # 창 닫기 허용

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 