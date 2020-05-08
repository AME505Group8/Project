# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_RsltKmeans.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI_RsltKmeans(object):
    def setupUi(self, GUI_RsltKmeans):
        GUI_RsltKmeans.setObjectName("GUI_RsltKmeans")
        GUI_RsltKmeans.resize(800, 600)
        GUI_RsltKmeans.setMinimumSize(QtCore.QSize(800, 600))
        GUI_RsltKmeans.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(GUI_RsltKmeans)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleBlock = QtWidgets.QFrame(self.centralwidget)
        self.TitleBlock.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        self.TitleBlock.setFont(font)
        self.TitleBlock.setStyleSheet("background-color: rgb(51, 58, 62);")
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
        self.label.setPixmap(QtGui.QPixmap("GUI/Assets/GUI_StartScreenGraphic.jpg"))
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
        self.label_5.setStyleSheet("background-color: rgb(51, 58, 62);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.TitleBlock)
        self.label_6.setMinimumSize(QtCore.QSize(218, 0))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(51, 58, 62);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.TitleBlock)
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(161, 172, 178);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.FltPlnOutput = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.FltPlnOutput.setFont(font)
        self.FltPlnOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.FltPlnOutput.setObjectName("FltPlnOutput")
        self.verticalLayout_2.addWidget(self.FltPlnOutput)
        self.label_18 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 20))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(175, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(175, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addWidget(self.MainContent)
        self.ButtonBar = QtWidgets.QFrame(self.centralwidget)
        self.ButtonBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ButtonBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ButtonBar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ButtonBar.setLineWidth(0)
        self.ButtonBar.setObjectName("ButtonBar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ButtonBar)
        self.horizontalLayout_4.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.StartButton = QtWidgets.QPushButton(self.ButtonBar)
        self.StartButton.setMinimumSize(QtCore.QSize(100, 50))
        self.StartButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("background-color: rgb(101, 117, 125);\n"
"color: rgb(255, 255, 255);")
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_4.addWidget(self.StartButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
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
        self.horizontalLayout_4.addWidget(self.QuitButton)
        self.verticalLayout.addWidget(self.ButtonBar)
        GUI_RsltKmeans.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GUI_RsltKmeans)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        GUI_RsltKmeans.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GUI_RsltKmeans)
        self.statusbar.setObjectName("statusbar")
        GUI_RsltKmeans.setStatusBar(self.statusbar)

        self.retranslateUi(GUI_RsltKmeans)
        QtCore.QMetaObject.connectSlotsByName(GUI_RsltKmeans)

    def retranslateUi(self, GUI_RsltKmeans):
        _translate = QtCore.QCoreApplication.translate
        GUI_RsltKmeans.setWindowTitle(_translate("GUI_RsltKmeans", "MainWindow"))
        self.label_5.setText(_translate("GUI_RsltKmeans", "Bird Strike Analysis"))
        self.label_6.setText(_translate("GUI_RsltKmeans", "AME505 Group 8"))
        self.FltPlnOutput.setText(_translate("GUI_RsltKmeans", "K Means Output"))
        self.label_18.setText(_translate("GUI_RsltKmeans", "The output plots will appear external to this GUI. Please be aware that this process may take several minutes. During this time, the GUI may become unresponsive."))
        self.label_3.setText(_translate("GUI_RsltKmeans", "WARNING"))
        self.label_2.setText(_translate("GUI_RsltKmeans", "All plots must be closed prior to navigating away for this window. Failure to close plots will result in a FATAL EXCEPTION ERROR."))
        self.StartButton.setText(_translate("GUI_RsltKmeans", "Back"))
        self.QuitButton.setText(_translate("GUI_RsltKmeans", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI_RsltKmeans = QtWidgets.QMainWindow()
    ui = Ui_GUI_RsltKmeans()
    ui.setupUi(GUI_RsltKmeans)
    GUI_RsltKmeans.show()
    sys.exit(app.exec_())
