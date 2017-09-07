# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUserUi.ui'
#
# Created: Wed Sep 06 22:57:14 2017
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

class Ui_Form_New(object):
    def setupUi(self, Form_New):
        Form_New.setObjectName(_fromUtf8("Form_New"))
        Form_New.resize(291, 193)
        self.label_User = QtGui.QLabel(Form_New)
        self.label_User.setGeometry(QtCore.QRect(40, 30, 61, 16))
        self.label_User.setObjectName(_fromUtf8("label_User"))
        self.label_Password = QtGui.QLabel(Form_New)
        self.label_Password.setGeometry(QtCore.QRect(40, 70, 61, 16))
        self.label_Password.setObjectName(_fromUtf8("label_Password"))
        self.label_ConfirmPassword = QtGui.QLabel(Form_New)
        self.label_ConfirmPassword.setGeometry(QtCore.QRect(40, 110, 61, 16))
        self.label_ConfirmPassword.setObjectName(_fromUtf8("label_ConfirmPassword"))
        self.lineEdit_User = QtGui.QLineEdit(Form_New)
        self.lineEdit_User.setGeometry(QtCore.QRect(110, 30, 141, 20))
        self.lineEdit_User.setObjectName(_fromUtf8("lineEdit_User"))
        self.lineEdit_Password = QtGui.QLineEdit(Form_New)
        self.lineEdit_Password.setGeometry(QtCore.QRect(110, 70, 141, 20))
        self.lineEdit_Password.setStyleSheet(_fromUtf8("lineedit-password-character: 42"))
        self.lineEdit_Password.setObjectName(_fromUtf8("lineEdit_Password"))
        self.lineEdit_ConfirmPassword = QtGui.QLineEdit(Form_New)
        self.lineEdit_ConfirmPassword.setGeometry(QtCore.QRect(110, 110, 141, 20))
        self.lineEdit_ConfirmPassword.setStyleSheet(_fromUtf8("lineedit-password-character: 42"))
        self.lineEdit_ConfirmPassword.setObjectName(_fromUtf8("lineEdit_ConfirmPassword"))
        self.pushButton_Ensure = QtGui.QPushButton(Form_New)
        self.pushButton_Ensure.setGeometry(QtCore.QRect(110, 160, 51, 23))
        self.pushButton_Ensure.setObjectName(_fromUtf8("pushButton_Ensure"))
        self.pushButton_Cancel = QtGui.QPushButton(Form_New)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(190, 160, 51, 23))
        self.pushButton_Cancel.setObjectName(_fromUtf8("pushButton_Cancel"))

        self.retranslateUi(Form_New)
        QtCore.QMetaObject.connectSlotsByName(Form_New)

    def retranslateUi(self, Form_New):
        Form_New.setWindowTitle(_translate("Form_New", "New", None))
        self.label_User.setText(_translate("Form_New", "用    户：", None))
        self.label_Password.setText(_translate("Form_New", "密    码：", None))
        self.label_ConfirmPassword.setText(_translate("Form_New", "确认密码：", None))
        self.pushButton_Ensure.setText(_translate("Form_New", "OK", None))
        self.pushButton_Cancel.setText(_translate("Form_New", "Cancel", None))

