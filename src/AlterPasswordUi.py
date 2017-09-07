# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangePassword.ui'
#
# Created: Fri Aug 25 22:53:01 2017
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

class Ui_Form_Password(object):
    def setupUi(self, Form_Password):
        Form_Password.setObjectName(_fromUtf8("Form_Password"))
        Form_Password.resize(290, 196)
        self.label_oldPassword = QtGui.QLabel(Form_Password)
        self.label_oldPassword.setGeometry(QtCore.QRect(30, 40, 51, 16))
        self.label_oldPassword.setObjectName(_fromUtf8("label_oldPassword"))
        self.label_newPassword = QtGui.QLabel(Form_Password)
        self.label_newPassword.setGeometry(QtCore.QRect(30, 80, 54, 12))
        self.label_newPassword.setObjectName(_fromUtf8("label_newPassword"))
        self.label_confirmPassword = QtGui.QLabel(Form_Password)
        self.label_confirmPassword.setGeometry(QtCore.QRect(20, 120, 54, 12))
        self.label_confirmPassword.setObjectName(_fromUtf8("label_confirmPassword"))
        self.lineEdit_oldPassword = QtGui.QLineEdit(Form_Password)
        self.lineEdit_oldPassword.setGeometry(QtCore.QRect(80, 40, 171, 20))
        self.lineEdit_oldPassword.setObjectName(_fromUtf8("lineEdit_oldPassword"))
        self.lineEdit_newPassword = QtGui.QLineEdit(Form_Password)
        self.lineEdit_newPassword.setGeometry(QtCore.QRect(80, 80, 171, 20))
        self.lineEdit_newPassword.setObjectName(_fromUtf8("lineEdit_newPassword"))
        self.lineEdit_confirmPassword = QtGui.QLineEdit(Form_Password)
        self.lineEdit_confirmPassword.setGeometry(QtCore.QRect(80, 120, 171, 20))
        self.lineEdit_confirmPassword.setObjectName(_fromUtf8("lineEdit_confirmPassword"))
        self.pushButton_enSure = QtGui.QPushButton(Form_Password)
        self.pushButton_enSure.setGeometry(QtCore.QRect(80, 160, 51, 23))
        self.pushButton_enSure.setObjectName(_fromUtf8("pushButton_enSure"))
        self.pushButton_cancel = QtGui.QPushButton(Form_Password)
        self.pushButton_cancel.setGeometry(QtCore.QRect(150, 160, 51, 23))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))

        self.retranslateUi(Form_Password)
        QtCore.QMetaObject.connectSlotsByName(Form_Password)

    def retranslateUi(self, Form_Password):
        Form_Password.setWindowTitle(_translate("Form_Password", "Password", None))
        self.label_oldPassword.setText(_translate("Form_Password", "旧密码：", None))
        self.label_newPassword.setText(_translate("Form_Password", "新密码：", None))
        self.label_confirmPassword.setText(_translate("Form_Password", "确认密码：", None))
        self.pushButton_enSure.setText(_translate("Form_Password", "OK", None))
        self.pushButton_cancel.setText(_translate("Form_Password", "Cancel", None))

