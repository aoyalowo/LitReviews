# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pubcrawl.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)

    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailLabel.sizePolicy().hasHeightForWidth())
        self.emailLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.verticalLayout.addWidget(self.emailLabel)
        self.emailQle = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailQle.sizePolicy().hasHeightForWidth())
        self.emailQle.setSizePolicy(sizePolicy)
        self.emailQle.setMinimumSize(QtCore.QSize(200, 0))
        self.emailQle.setObjectName("emailQle")
        self.verticalLayout.addWidget(self.emailQle)
        self.emailButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailButton.sizePolicy().hasHeightForWidth())
        self.emailButton.setSizePolicy(sizePolicy)
        self.emailButton.setObjectName("emailButton")
        self.verticalLayout.addWidget(self.emailButton)
        self.searchTermLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchTermLabel.sizePolicy().hasHeightForWidth())
        self.searchTermLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.searchTermLabel.setFont(font)
        self.searchTermLabel.setObjectName("searchTermLabel")
        self.verticalLayout.addWidget(self.searchTermLabel)
        self.searchTermQle = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchTermQle.sizePolicy().hasHeightForWidth())
        self.searchTermQle.setSizePolicy(sizePolicy)
        self.searchTermQle.setObjectName("searchTermQle")
        self.verticalLayout.addWidget(self.searchTermQle)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout.addWidget(self.searchButton)
        self.summariesButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summariesButton.sizePolicy().hasHeightForWidth())
        self.summariesButton.setSizePolicy(sizePolicy)
        self.summariesButton.setObjectName("summariesButton")
        self.verticalLayout.addWidget(self.summariesButton)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.pmidsButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pmidsButton.sizePolicy().hasHeightForWidth())
        self.pmidsButton.setSizePolicy(sizePolicy)
        self.pmidsButton.setObjectName("Generate PMID List")
        self.verticalLayout.addWidget(self.pmidsButton)
        self.quickStatsLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickStatsLabel.sizePolicy().hasHeightForWidth())
        self.quickStatsLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.quickStatsLabel.setFont(font)
        self.quickStatsLabel.setObjectName("quickStatsLabel")
        self.verticalLayout.addWidget(self.quickStatsLabel)
        self.previousSearchTermLabelName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousSearchTermLabelName.sizePolicy().hasHeightForWidth())
        self.previousSearchTermLabelName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.previousSearchTermLabelName.setFont(font)
        self.previousSearchTermLabelName.setTextFormat(QtCore.Qt.PlainText)
        self.previousSearchTermLabelName.setObjectName("previousSearchTermLabelName")
        self.verticalLayout.addWidget(self.previousSearchTermLabelName)
        self.pmRefCountLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pmRefCountLabel.sizePolicy().hasHeightForWidth())
        self.pmRefCountLabel.setSizePolicy(sizePolicy)
        self.pmRefCountLabel.setObjectName("pmRefCountLabel")
        self.verticalLayout.addWidget(self.pmRefCountLabel)
        self.pmcRefCountLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pmcRefCountLabel.sizePolicy().hasHeightForWidth())
        self.pmcRefCountLabel.setSizePolicy(sizePolicy)
        self.pmcRefCountLabel.setObjectName("pmcRefCountLabel")
        self.verticalLayout.addWidget(self.pmcRefCountLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.webEngineView = QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setUrl(QtCore.QUrl("https://www.ncbi.nlm.nih.gov/Structure/flink/flink.cgi"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setMinimumSize(QtCore.QSize(200, 150))
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 22))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.emailLabel.setText(_translate("MainWindow", "Email:"))
        self.emailButton.setText(_translate("MainWindow", "Set Email"))
        self.searchTermLabel.setText(_translate("MainWindow", "Search Term:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.summariesButton.setText(_translate("MainWindow", "Generate Summaries"))
        self.pmidsButton.setText(_translate("MainWindow", "Generate PMID List"))
        self.quickStatsLabel.setText(_translate("MainWindow", "Quick Stats:"))
        self.previousSearchTermLabelName.setText(_translate("MainWindow", "None"))
        self.pmRefCountLabel.setText(_translate("MainWindow", "Pm Ref Count:"))
        self.pmcRefCountLabel.setText(_translate("MainWindow", "Pmc Ref Count:"))
        self.label_2.setText(_translate("MainWindow", "NCBI FLink WebPage. Right-click for context menu to access back/forward/reload buttons."))
        self.label.setText(_translate("MainWindow", "Double-click file (below) to change name:"))