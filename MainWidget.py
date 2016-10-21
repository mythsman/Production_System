# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMinimumSize(QtCore.QSize(635, 658))
        MainWidget.setMaximumSize(QtCore.QSize(635, 658))
        MainWidget.setMouseTracking(False)
        MainWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.listView = QtWidgets.QListView(MainWidget)
        self.listView.setGeometry(QtCore.QRect(30, 140, 181, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(MainWidget)
        self.listView_2.setGeometry(QtCore.QRect(370, 140, 221, 151))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(MainWidget)
        self.listView_3.setGeometry(QtCore.QRect(370, 320, 221, 81))
        self.listView_3.setObjectName("listView_3")
        self.btnCalc = QtWidgets.QPushButton(MainWidget)
        self.btnCalc.setGeometry(QtCore.QRect(440, 430, 80, 22))
        self.btnCalc.setObjectName("btnCalc")
        self.textBrowser = QtWidgets.QTextBrowser(MainWidget)
        self.textBrowser.setGeometry(QtCore.QRect(370, 480, 221, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(MainWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 40, 256, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.btnChooseFile = QtWidgets.QPushButton(MainWidget)
        self.btnChooseFile.setGeometry(QtCore.QRect(370, 40, 141, 31))
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.label = QtWidgets.QLabel(MainWidget)
        self.label.setGeometry(QtCore.QRect(40, 110, 161, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWidget)
        self.label_2.setGeometry(QtCore.QRect(278, 140, 81, 151))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWidget)
        self.label_3.setGeometry(QtCore.QRect(278, 320, 81, 71))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.btnExit = QtWidgets.QPushButton(MainWidget)
        self.btnExit.setGeometry(QtCore.QRect(440, 560, 80, 22))
        self.btnExit.setObjectName("btnExit")
        self.label_4 = QtWidgets.QLabel(MainWidget)
        self.label_4.setGeometry(QtCore.QRect(280, 480, 81, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(MainWidget)
        self.btnExit.clicked.connect(MainWidget.close)
        self.btnChooseFile.clicked.connect(MainWidget.slotChooseFile)
        self.btnCalc.clicked.connect(MainWidget.slotCalc)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Production System"))
        self.btnCalc.setText(_translate("MainWidget", "Calculate"))
        self.btnChooseFile.setText(_translate("MainWidget", "Choose Rule File"))
        self.label.setText(_translate("MainWidget", "Accepted Data"))
        self.label_2.setText(_translate("MainWidget", "Database"))
        self.label_3.setText(_translate("MainWidget", "Accepted Result"))
        self.btnExit.setText(_translate("MainWidget", "Exit"))
        self.label_4.setText(_translate("MainWidget", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWidget = QtWidgets.QWidget()
    ui = Ui_MainWidget()
    ui.setupUi(MainWidget)
    MainWidget.show()
    sys.exit(app.exec_())

