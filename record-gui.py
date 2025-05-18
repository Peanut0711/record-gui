#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
                              QInputDialog, QLineEdit, QTableWidgetItem, QLabel, 
                              QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QWidget)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QSize, QUrl
from PySide6.QtGui import QPixmap, QImage, QIcon, QAction, QDesktopServices
import requests
from io import BytesIO
import warnings
import logging

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
            
        # UI 표시
        self.ui.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 