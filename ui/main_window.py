# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.verticalLayout_2 = QVBoxLayout(self.mainTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.mainTab)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.urlInput = QLineEdit(self.groupBox)
        self.urlInput.setObjectName(u"urlInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.urlInput)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.savePathInput = QLineEdit(self.groupBox)
        self.savePathInput.setObjectName(u"savePathInput")

        self.horizontalLayout.addWidget(self.savePathInput)

        self.browseButton = QPushButton(self.groupBox)
        self.browseButton.setObjectName(u"browseButton")

        self.horizontalLayout.addWidget(self.browseButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.qualityCombo = QComboBox(self.groupBox)
        self.qualityCombo.addItem("")
        self.qualityCombo.addItem("")
        self.qualityCombo.addItem("")
        self.qualityCombo.addItem("")
        self.qualityCombo.setObjectName(u"qualityCombo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.qualityCombo)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.mainTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startButton = QPushButton(self.groupBox_2)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout_2.addWidget(self.startButton)

        self.stopButton = QPushButton(self.groupBox_2)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.stopButton)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.mainTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.statusLabel = QLabel(self.groupBox_3)
        self.statusLabel.setObjectName(u"statusLabel")

        self.verticalLayout_3.addWidget(self.statusLabel)

        self.progressBar = QProgressBar(self.groupBox_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.recordList = QTableWidget(self.mainTab)
        if (self.recordList.columnCount() < 4):
            self.recordList.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.recordList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.recordList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.recordList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.recordList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.recordList.setObjectName(u"recordList")

        self.verticalLayout_2.addWidget(self.recordList)

        self.tabWidget.addTab(self.mainTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.verticalLayout_4 = QVBoxLayout(self.settingsTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.settingsTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_2 = QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.defaultSavePathInput = QLineEdit(self.groupBox_4)
        self.defaultSavePathInput.setObjectName(u"defaultSavePathInput")

        self.horizontalLayout_3.addWidget(self.defaultSavePathInput)

        self.defaultPathBrowseButton = QPushButton(self.groupBox_4)
        self.defaultPathBrowseButton.setObjectName(u"defaultPathBrowseButton")

        self.horizontalLayout_3.addWidget(self.defaultPathBrowseButton)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.defaultQualityCombo = QComboBox(self.groupBox_4)
        self.defaultQualityCombo.addItem("")
        self.defaultQualityCombo.addItem("")
        self.defaultQualityCombo.addItem("")
        self.defaultQualityCombo.addItem("")
        self.defaultQualityCombo.setObjectName(u"defaultQualityCombo")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.defaultQualityCombo)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.settingsTab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.idPwRadio = QRadioButton(self.groupBox_6)
        self.idPwRadio.setObjectName(u"idPwRadio")
        self.idPwRadio.setChecked(True)

        self.verticalLayout_5.addWidget(self.idPwRadio)

        self.cookieRadio = QRadioButton(self.groupBox_6)
        self.cookieRadio.setObjectName(u"cookieRadio")

        self.verticalLayout_5.addWidget(self.cookieRadio)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.soopIdInput = QLineEdit(self.groupBox_6)
        self.soopIdInput.setObjectName(u"soopIdInput")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.soopIdInput)

        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.soopPwInput = QLineEdit(self.groupBox_6)
        self.soopPwInput.setObjectName(u"soopPwInput")
        self.soopPwInput.setEchoMode(QLineEdit.Password)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.soopPwInput)


        self.verticalLayout_5.addLayout(self.formLayout_4)

        self.saveCredentialsCheck = QCheckBox(self.groupBox_6)
        self.saveCredentialsCheck.setObjectName(u"saveCredentialsCheck")

        self.verticalLayout_5.addWidget(self.saveCredentialsCheck)


        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.settingsTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout_3 = QFormLayout(self.groupBox_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.autoRestartCheck = QCheckBox(self.groupBox_5)
        self.autoRestartCheck.setObjectName(u"autoRestartCheck")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.autoRestartCheck)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.maxRetrySpin = QSpinBox(self.groupBox_5)
        self.maxRetrySpin.setObjectName(u"maxRetrySpin")
        self.maxRetrySpin.setMinimum(1)
        self.maxRetrySpin.setMaximum(10)
        self.maxRetrySpin.setValue(3)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.maxRetrySpin)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.retryIntervalCombo = QComboBox(self.groupBox_5)
        self.retryIntervalCombo.addItem("")
        self.retryIntervalCombo.addItem("")
        self.retryIntervalCombo.addItem("")
        self.retryIntervalCombo.addItem("")
        self.retryIntervalCombo.addItem("")
        self.retryIntervalCombo.addItem("")
        self.retryIntervalCombo.setObjectName(u"retryIntervalCombo")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.retryIntervalCombo)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.saveSettingsButton = QPushButton(self.settingsTab)
        self.saveSettingsButton.setObjectName(u"saveSettingsButton")

        self.horizontalLayout_4.addWidget(self.saveSettingsButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.settingsTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc2a4\ud2b8\ub9bc \ub179\ud654 \ud504\ub85c\uadf8\ub7a8", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc(&X)", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+F4", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uc815\ubcf4(&A)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\uc2a4\ud2b8\ub9bc \uc124\uc815", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc2a4\ud2b8\ub9bc URL:", None))
        self.urlInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://play.sooplive.co.kr/dlrnf/284041142", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \uacbd\ub85c:", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\uc544\ubcf4\uae30", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \ud488\uc9c8:", None))
        self.qualityCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"\ucd5c\uace0 \ud488\uc9c8", None))
        self.qualityCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"\uace0\ud654\uc9c8", None))
        self.qualityCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc911\ud654\uc9c8", None))
        self.qualityCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc800\ud654\uc9c8", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc81c\uc5b4", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc911\uc9c0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc0c1\ud0dc", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"\ub300\uae30 \uc911...", None))
        ___qtablewidgetitem = self.recordList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtablewidgetitem1 = self.recordList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None));
        ___qtablewidgetitem2 = self.recordList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791 \uc2dc\uac04", None));
        ___qtablewidgetitem3 = self.recordList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uacbd\ub85c", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("MainWindow", u"\uba54\uc778", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\uae30\ubcf8 \uc124\uc815", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uae30\ubcf8 \uc800\uc7a5 \uacbd\ub85c:", None))
        self.defaultPathBrowseButton.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\uc544\ubcf4\uae30", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uae30\ubcf8 \ub179\ud654 \ud488\uc9c8:", None))
        self.defaultQualityCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"\ucd5c\uace0 \ud488\uc9c8", None))
        self.defaultQualityCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"\uace0\ud654\uc9c8", None))
        self.defaultQualityCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc911\ud654\uc9c8", None))
        self.defaultQualityCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc800\ud654\uc9c8", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Soop \ub85c\uadf8\uc778 \uc124\uc815", None))
        self.idPwRadio.setText(QCoreApplication.translate("MainWindow", u"ID/PW \uc9c1\uc811 \uc785\ub825", None))
        self.cookieRadio.setText(QCoreApplication.translate("MainWindow", u"\ucfe0\ud0a4 \ubc29\uc2dd", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.soopIdInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Soop \uacc4\uc815 ID", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.soopPwInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Soop \uacc4\uc815 \ube44\ubc00\ubc88\ud638", None))
        self.saveCredentialsCheck.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778 \uc815\ubcf4 \uc800\uc7a5", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\uace0\uae09 \uc124\uc815", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub3d9 \uc7ac\uc2dc\uc791:", None))
        self.autoRestartCheck.setText(QCoreApplication.translate("MainWindow", u"\uc2a4\ud2b8\ub9bc \uc911\ub2e8 \uc2dc \uc790\ub3d9 \uc7ac\uc2dc\uc791", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300 \uc7ac\uc2dc\uc791 \ud69f\uc218:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc2dc\ub3c4 \uac04\uaca9:", None))
        self.retryIntervalCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"5\ucd08", None))
        self.retryIntervalCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"10\ucd08", None))
        self.retryIntervalCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"30\ucd08", None))
        self.retryIntervalCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"1\ubd84", None))
        self.retryIntervalCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"3\ubd84", None))
        self.retryIntervalCombo.setItemText(5, QCoreApplication.translate("MainWindow", u"5\ubd84", None))

        self.saveSettingsButton.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815 \uc800\uc7a5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"\ud658\uacbd\uc124\uc815", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c(&F)", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0(&H)", None))
    # retranslateUi

