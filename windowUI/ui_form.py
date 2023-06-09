# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PiCam(object):
    def setupUi(self, PiCam):
        PiCam.setObjectName("PiCam")
        PiCam.resize(850, 700)
        self.verticalLayout = QtWidgets.QVBoxLayout(PiCam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pic = QtWidgets.QGraphicsView(PiCam)
        self.pic.setObjectName("pic")
        self.verticalLayout.addWidget(self.pic)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.int_LB = QtWidgets.QLabel(PiCam)
        self.int_LB.setObjectName("int_LB")
        self.gridLayout.addWidget(self.int_LB, 0, 0, 1, 1)
        self.int_LE = QtWidgets.QLineEdit(PiCam)
        self.int_LE.setObjectName("int_LE")
        self.gridLayout.addWidget(self.int_LE, 0, 1, 1, 1)
        self.int_BTN = QtWidgets.QPushButton(PiCam)
        self.int_BTN.setObjectName("int_BTN")
        self.gridLayout.addWidget(self.int_BTN, 0, 2, 1, 1)
        self.ang_LB = QtWidgets.QLabel(PiCam)
        self.ang_LB.setObjectName("ang_LB")
        self.gridLayout.addWidget(self.ang_LB, 1, 0, 1, 1)
        self.ang_LE = QtWidgets.QLineEdit(PiCam)
        self.ang_LE.setObjectName("ang_LE")
        self.gridLayout.addWidget(self.ang_LE, 1, 1, 1, 1)
        self.ang_BTN = QtWidgets.QPushButton(PiCam)
        self.ang_BTN.setObjectName("ang_BTN")
        self.gridLayout.addWidget(self.ang_BTN, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fetch = QtWidgets.QPushButton(PiCam)
        self.fetch.setObjectName("fetch")
        self.horizontalLayout.addWidget(self.fetch)
        self.warning = QtWidgets.QPushButton(PiCam)
        self.warning.setObjectName("warning")
        self.horizontalLayout.addWidget(self.warning)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 12)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(PiCam)
        QtCore.QMetaObject.connectSlotsByName(PiCam)

    def retranslateUi(self, PiCam):
        _translate = QtCore.QCoreApplication.translate
        PiCam.setWindowTitle(_translate("PiCam", "MyWidget"))
        self.int_LB.setText(_translate("PiCam", "interval/s"))
        self.int_BTN.setText(_translate("PiCam", "update"))
        self.ang_LB.setText(_translate("PiCam", "angle/deg"))
        self.ang_BTN.setText(_translate("PiCam", "update"))
        self.fetch.setText(_translate("PiCam", "fetch"))
        self.warning.setText(_translate("PiCam", "warning"))