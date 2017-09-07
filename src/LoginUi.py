# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Thu Aug 24 22:17:19 2017
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

class Ui_Form_Login(object):
    def setupUi(self, Form_Login):
        Form_Login.setObjectName(_fromUtf8("Form_Login"))
        Form_Login.resize(277, 175)
        self.label_User = QtGui.QLabel(Form_Login)
        self.label_User.setGeometry(QtCore.QRect(40, 30, 61, 16))
        self.label_User.setObjectName(_fromUtf8("label_User"))
        self.label_Password = QtGui.QLabel(Form_Login)
        self.label_Password.setGeometry(QtCore.QRect(40, 80, 61, 16))
        self.label_Password.setObjectName(_fromUtf8("label_Password"))
        self.lineEdit_User = QtGui.QLineEdit(Form_Login)
        self.lineEdit_User.setGeometry(QtCore.QRect(100, 30, 141, 20))
        self.lineEdit_User.setStyleSheet(_fromUtf8("lineedit-password-character: 42"))
        self.lineEdit_User.setObjectName(_fromUtf8("lineEdit_User"))
        self.lineEdit_Password = QtGui.QLineEdit(Form_Login)
        self.lineEdit_Password.setGeometry(QtCore.QRect(100, 80, 141, 20))
        self.lineEdit_Password.setObjectName(_fromUtf8("lineEdit_Password"))
        self.pushButton_Login = QtGui.QPushButton(Form_Login)
        self.pushButton_Login.setGeometry(QtCore.QRect(80, 130, 51, 23))
        self.pushButton_Login.setObjectName(_fromUtf8("pushButton_Login"))
        self.pushButton_Cancel = QtGui.QPushButton(Form_Login)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(150, 130, 51, 23))
        self.pushButton_Cancel.setObjectName(_fromUtf8("pushButton_Cancel"))
        self.label_signup = QtGui.QLabel(Form_Login)
        self.label_signup.setGeometry(QtCore.QRect(240, 160, 31, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Modern"))
        font.setBold(False)
        font.setWeight(50)
        self.label_signup.setFont(font)
        self.label_signup.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_signup.setFrameShadow(QtGui.QFrame.Plain)
        self.label_signup.setObjectName(_fromUtf8("label_signup"))

        self.retranslateUi(Form_Login)
        QtCore.QMetaObject.connectSlotsByName(Form_Login)

    def retranslateUi(self, Form_Login):
        Form_Login.setWindowTitle(_translate("Form_Login", "Login", None))
        self.label_User.setText(_translate("Form_Login", "用    户：", None))
        self.label_Password.setText(_translate("Form_Login", "密    码：", None))
        self.pushButton_Login.setText(_translate("Form_Login", "Login", None))
        self.pushButton_Cancel.setText(_translate("Form_Login", "Cancel", None))
        self.label_signup.setText(_translate("Form_Login", "新用户", None))

