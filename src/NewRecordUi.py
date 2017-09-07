# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewRecord.ui'
#
# Created: Fri Aug 25 00:18:24 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form_Record(object):
    def setupUi(self, Form_Record):
        Form_Record.setObjectName(_fromUtf8("Form_Record"))
        Form_Record.resize(315, 210)
        self.label_user = QtGui.QLabel(Form_Record)
        self.label_user.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.label_password = QtGui.QLabel(Form_Record)
        self.label_password.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.label_userWeb = QtGui.QLabel(Form_Record)
        self.label_userWeb.setGeometry(QtCore.QRect(30, 120, 61, 16))
        self.label_userWeb.setObjectName(_fromUtf8("label_userWeb"))
        self.lineEdit_user = QtGui.QLineEdit(Form_Record)
        self.lineEdit_user.setGeometry(QtCore.QRect(90, 40, 191, 20))
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))
        self.lineEdit_password = QtGui.QLineEdit(Form_Record)
        self.lineEdit_password.setGeometry(QtCore.QRect(90, 80, 191, 20))
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.lineEdit_userWeb = QtGui.QLineEdit(Form_Record)
        self.lineEdit_userWeb.setGeometry(QtCore.QRect(90, 120, 191, 20))
        self.lineEdit_userWeb.setObjectName(_fromUtf8("lineEdit_userWeb"))
        self.pushButton_enSure = QtGui.QPushButton(Form_Record)
        self.pushButton_enSure.setGeometry(QtCore.QRect(100, 170, 51, 23))
        self.pushButton_enSure.setObjectName(_fromUtf8("pushButton_enSure"))
        self.pushButton_cancel = QtGui.QPushButton(Form_Record)
        self.pushButton_cancel.setGeometry(QtCore.QRect(170, 170, 51, 23))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))

        self.retranslateUi(Form_Record)
        QtCore.QMetaObject.connectSlotsByName(Form_Record)

    def retranslateUi(self, Form_Record):
        Form_Record.setWindowTitle(_translate("Form_Record", "NewRecord", None))
        self.label_user.setText(_translate("Form_Record", "username:", None))
        self.label_password.setText(_translate("Form_Record", "password:", None))
        self.label_userWeb.setText(_translate("Form_Record", "user web:", None))
        self.pushButton_enSure.setText(_translate("Form_Record", "OK", None))
        self.pushButton_cancel.setText(_translate("Form_Record", "Cancel", None))

