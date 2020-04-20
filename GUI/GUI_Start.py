# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Start.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import time
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from GUI_InputFldMgmt import Ui_GUI_InputFldMgmt
from GUI_InputFltPln import Ui_GUI_InputFltPln
from GUI_InputRskAssess import Ui_GUI_InputRskAssess
from GUI_RsltFldMgmt import Ui_GUI_RsltFldMgmt
from GUI_RsltFltPln import Ui_GUI_RsltFltPln
from GUI_RsltRskAssess import Ui_GUI_RsltRskAssess


class Ui_GUI_Start(object):
    def __init__(self):
        # Window object definition
        self.GUI_InputFldMgmt = QtWidgets.QMainWindow()
        self.GUI_InputFldMgmt_Ui = Ui_GUI_InputFldMgmt()
        self.GUI_InputFldMgmt_Ui.setupUi(self.GUI_InputFldMgmt)

        self.GUI_InputFltPln = QtWidgets.QMainWindow()
        self.GUI_InputFltPln_Ui = Ui_GUI_InputFltPln()
        self.GUI_InputFltPln_Ui.setupUi(self.GUI_InputFltPln)

        self.GUI_InputRskAssess = QtWidgets.QMainWindow()
        self.GUI_InputRskAssess_Ui = Ui_GUI_InputRskAssess()
        self.GUI_InputRskAssess_Ui.setupUi(self.GUI_InputRskAssess)

        self.GUI_RsltFldMgmt = QtWidgets.QMainWindow()
        self.GUI_RsltFldMgmt_Ui = Ui_GUI_RsltFldMgmt()
        self.GUI_RsltFldMgmt_Ui.setupUi(self.GUI_RsltFldMgmt)

        self.GUI_RsltFltPln = QtWidgets.QMainWindow()
        self.GUI_RsltFltPln_Ui = Ui_GUI_RsltFltPln()
        self.GUI_RsltFltPln_Ui.setupUi(self.GUI_RsltFltPln)

        self.GUI_RsltRskAssess = QtWidgets.QMainWindow()
        self.GUI_RsltRskAssess_Ui = Ui_GUI_RsltRskAssess()
        self.GUI_RsltRskAssess_Ui.setupUi(self.GUI_RsltRskAssess)

        # Window button actions (Start window button actions near bottom of this script)
        self.GUI_InputFldMgmt_Ui.RsltFldMgmtButton.clicked.connect(self.GoToRsltFldMgmt)
        self.GUI_InputFldMgmt_Ui.StartButton.clicked.connect(self.GoToStart)

        self.GUI_InputFltPln_Ui.RsltFltPlnButton.clicked.connect(self.GoToRsltFltPln)
        self.GUI_InputFltPln_Ui.StartButton.clicked.connect(self.GoToStart)

        self.GUI_InputRskAssess_Ui.RsltRskAssessButton.clicked.connect(self.GoToRsltRskAssess)
        self.GUI_InputRskAssess_Ui.StartButton.clicked.connect(self.GoToStart)

        self.GUI_RsltFldMgmt_Ui.InputFldMgmtButton.clicked.connect(self.GoToInputFldMgmt)
        self.GUI_RsltFldMgmt_Ui.StartButton.clicked.connect(self.GoToStart)
        self.GUI_RsltFldMgmt_Ui.PrintButton.clicked.connect(self.PrintRsltFldMgmt)

        self.GUI_RsltFltPln_Ui.InputFltPlnButton.clicked.connect(self.GoToInputFltPln)
        self.GUI_RsltFltPln_Ui.StartButton.clicked.connect(self.GoToStart)
        self.GUI_RsltFltPln_Ui.PrintButton.clicked.connect(self.PrintRsltFltPln)

        self.GUI_RsltRskAssess_Ui.InputRskAssessButton.clicked.connect(self.GoToInputRskAssess)
        self.GUI_RsltRskAssess_Ui.StartButton.clicked.connect(self.GoToStart)
        self.GUI_RsltRskAssess_Ui.PrintButton.clicked.connect(self.PrintRsltRskAssess)

    # Page transition functions
    def GoToStart(self):
        GUI_Start.show()
        self.GUI_InputFldMgmt.hide()
        self.GUI_InputFltPln.hide()
        self.GUI_InputRskAssess.hide()
        self.GUI_RsltFldMgmt.hide()
        self.GUI_RsltFltPln.hide()
        self.GUI_RsltRskAssess.hide()

    def GoToInputFldMgmt(self):
        GUI_Start.hide()
        self.GUI_InputFldMgmt.show()
        self.GUI_InputFltPln.hide()
        self.GUI_InputRskAssess.hide()
        self.GUI_RsltFldMgmt.hide()
        self.GUI_RsltFltPln.hide()
        self.GUI_RsltRskAssess.hide()

    def GoToInputFltPln(self):
        GUI_Start.hide()
        self.GUI_InputFldMgmt.hide()
        self.GUI_InputFltPln.show()
        self.GUI_InputRskAssess.hide()
        self.GUI_RsltFldMgmt.hide()
        self.GUI_RsltFltPln.hide()
        self.GUI_RsltRskAssess.hide()

    def GoToInputRskAssess(self):
        GUI_Start.hide()
        self.GUI_InputFldMgmt.hide()
        self.GUI_InputFltPln.hide()
        self.GUI_InputRskAssess.show()
        self.GUI_RsltFldMgmt.hide()
        self.GUI_RsltFltPln.hide()
        self.GUI_RsltRskAssess.hide()

    def GoToRsltFldMgmt(self):
        GUI_Start.hide()
        self.GUI_InputFldMgmt.hide()
        self.GUI_InputFltPln.hide()
        self.GUI_InputRskAssess.hide()
        self.GUI_RsltFldMgmt.show()
        self.GUI_RsltFltPln.hide()
        self.GUI_RsltRskAssess.hide()

    def GoToRsltFltPln(self):
        GUI_Start.hide()
        self.GUI_InputFldMgmt.hide()
        self.GUI_InputFltPln.hide()
        self.GUI_InputRskAssess.hide()
        self.GUI_RsltFldMgmt.hide()
        self.GUI_RsltFltPln.show()
        self.GUI_RsltRskAssess.hide()

    def GoToRsltRskAssess(self):
        GUI_Start.hide()
        self.GUI_InputFldMgmt.hide()
        self.GUI_InputFltPln.hide()
        self.GUI_InputRskAssess.hide()
        self.GUI_RsltFldMgmt.hide()
        self.GUI_RsltFltPln.hide()
        self.GUI_RsltRskAssess.show()

    # Result printing functions
    def PrintRsltFldMgmt(self):
        print('Field management print button successful')

    def PrintRsltFltPln(self):
        print('Flight planning print button successful')

    def PrintRsltRskAssess(self):
        print('Risk assessment print button successful')

    # Program exiting function
    def GoToExitScript(self):
        sys.exit()

    #Begin QtDesigner generated code
    def setupUi(self, GUI_Start):
        GUI_Start.setObjectName("GUI_Start")
        GUI_Start.resize(800, 600)
        GUI_Start.setMinimumSize(QtCore.QSize(800, 600))
        GUI_Start.setStyleSheet("background-color: rgb(255, 255, 255);")
        GUI_Start.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(GUI_Start)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TitleBlock = QtWidgets.QFrame(self.centralwidget)
        self.TitleBlock.setMaximumSize(QtCore.QSize(16777215, 100))
        self.TitleBlock.setStyleSheet("background-color: rgb(161, 172, 178);")
        self.TitleBlock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TitleBlock.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBlock.setObjectName("TitleBlock")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.TitleBlock)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.TitleBlock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(571, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Assets/GUI_StartScreenGraphic.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.TitleBlock)
        self.label_5.setMinimumSize(QtCore.QSize(218, 0))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.TitleBlock)
        self.label_6.setMinimumSize(QtCore.QSize(218, 0))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.TitleBlock)
        self.MainContent = QtWidgets.QFrame(self.centralwidget)
        self.MainContent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainContent.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainContent.setLineWidth(0)
        self.MainContent.setObjectName("MainContent")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainContent)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.MainContent)
        self.frame.setStyleSheet("background-color: rgb(161, 172, 178);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InputFltPlnButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.InputFltPlnButton.setFont(font)
        self.InputFltPlnButton.setToolTipDuration(0)
        self.InputFltPlnButton.setStyleSheet("background-color: rgb(101, 117, 125);\n"
"color: rgb(255, 255, 255);")
        self.InputFltPlnButton.setObjectName("InputFltPlnButton")
        self.verticalLayout.addWidget(self.InputFltPlnButton)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.MainContent)
        self.frame_2.setStyleSheet("background-color: rgb(161, 172, 178);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.InputFldMgmtButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.InputFldMgmtButton.setFont(font)
        self.InputFldMgmtButton.setToolTipDuration(0)
        self.InputFldMgmtButton.setStyleSheet("background-color: rgb(101, 117, 125);\n"
"color: rgb(255, 255, 255);")
        self.InputFldMgmtButton.setObjectName("InputFldMgmtButton")
        self.verticalLayout_2.addWidget(self.InputFldMgmtButton)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.MainContent)
        self.frame_3.setStyleSheet("background-color: rgb(161, 172, 178);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InputRskAssessButton = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.InputRskAssessButton.setFont(font)
        self.InputRskAssessButton.setToolTipDuration(0)
        self.InputRskAssessButton.setStyleSheet("background-color: rgb(101, 117, 125);\n"
"color: rgb(255, 255, 255);")
        self.InputRskAssessButton.setObjectName("InputRskAssessButton")
        self.verticalLayout_3.addWidget(self.InputRskAssessButton)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout_5.addWidget(self.MainContent)
        self.ButtonBar = QtWidgets.QFrame(self.centralwidget)
        self.ButtonBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ButtonBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ButtonBar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ButtonBar.setLineWidth(0)
        self.ButtonBar.setObjectName("ButtonBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ButtonBar)
        self.horizontalLayout_3.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.QuitButton = QtWidgets.QPushButton(self.ButtonBar)
        self.QuitButton.setMinimumSize(QtCore.QSize(100, 50))
        self.QuitButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.QuitButton.setFont(font)
        self.QuitButton.setStyleSheet("background-color: rgb(101, 117, 125);\n"
"color: rgb(255, 255, 255);")
        self.QuitButton.setObjectName("QuitButton")
        self.horizontalLayout_3.addWidget(self.QuitButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.ButtonBar)
        self.MainContent.raise_()
        self.TitleBlock.raise_()
        self.ButtonBar.raise_()
        GUI_Start.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GUI_Start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        GUI_Start.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GUI_Start)
        self.statusbar.setObjectName("statusbar")
        GUI_Start.setStatusBar(self.statusbar)

        self.retranslateUi(GUI_Start)
        QtCore.QMetaObject.connectSlotsByName(GUI_Start)

        # Start Window Button Actions
        self.InputFldMgmtButton.clicked.connect(self.GoToInputFldMgmt)
        self.InputFltPlnButton.clicked.connect(self.GoToInputFltPln)
        self.InputRskAssessButton.clicked.connect(self.GoToInputRskAssess)
        self.QuitButton.clicked.connect(self.GoToExitScript)

    def retranslateUi(self, GUI_Start):
        _translate = QtCore.QCoreApplication.translate
        GUI_Start.setWindowTitle(_translate("GUI_Start", "MainWindow"))
        self.label_5.setText(_translate("GUI_Start", "Bird Strike Analysis"))
        self.label_6.setText(_translate("GUI_Start", "AME505 Group 8"))
        self.InputFltPlnButton.setText(_translate("GUI_Start", "Flight Planning"))
        self.label_2.setText(_translate("GUI_Start", "For users interested in the planning of a specific flight. Provides feedback on whether the planned departure and arrival times at the relevant airfields are of particular risk for bird strikes. Roles may include private pilots and commercial flight planners."))
        self.InputFldMgmtButton.setText(_translate("GUI_Start", "Airfield Management"))
        self.label_3.setText(_translate("GUI_Start", "For users interested in general trends specific to one airfield. Provides feedback on the frequency of bird strikes at a given airfield, which runways see the most strike activity, and when. Roles may include airfield managers, groundskeepers, etc."))
        self.InputRskAssessButton.setText(_translate("GUI_Start", "Risk Assessment"))
        self.label_4.setText(_translate("GUI_Start", "For users interested in general assessments of the risk of airstrikes at a given airfield as compared to all other airfields. Provides feedback on whether the airfield in question is a low, average, or high risk of bird strikes throughout a given year. Roles may include insurance analyst."))
        self.QuitButton.setText(_translate("GUI_Start", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI_Start = QtWidgets.QMainWindow()
    ui = Ui_GUI_Start()
    ui.setupUi(GUI_Start)
    GUI_Start.show()
    sys.exit(app.exec_())