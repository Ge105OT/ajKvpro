# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PasswordCreator.ui'
#
# Created: Sat Aug 26 00:55:02 2017
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

class Ui_Form_PasswordCreate(object):
    def setupUi(self, Form_PasswordCreate):
        Form_PasswordCreate.setObjectName(_fromUtf8("Form_PasswordCreate"))
        Form_PasswordCreate.resize(302, 239)
        self.checkBox_digits = QtGui.QCheckBox(Form_PasswordCreate)
        self.checkBox_digits.setGeometry(QtCore.QRect(80, 40, 121, 16))
        self.checkBox_digits.setObjectName(_fromUtf8("checkBox_digits"))
        self.checkBox_letter = QtGui.QCheckBox(Form_PasswordCreate)
        self.checkBox_letter.setGeometry(QtCore.QRect(80, 80, 131, 16))
        self.checkBox_letter.setObjectName(_fromUtf8("checkBox_letter"))
        self.checkBox_specialChar = QtGui.QCheckBox(Form_PasswordCreate)
        self.checkBox_specialChar.setGeometry(QtCore.QRect(80, 120, 191, 16))
        self.checkBox_specialChar.setObjectName(_fromUtf8("checkBox_specialChar"))
        self.lineEdit_password = QtGui.QLineEdit(Form_PasswordCreate)
        self.lineEdit_password.setGeometry(QtCore.QRect(80, 160, 171, 20))
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.pushButton_create = QtGui.QPushButton(Form_PasswordCreate)
        self.pushButton_create.setGeometry(QtCore.QRect(120, 200, 51, 23))
        self.pushButton_create.setObjectName(_fromUtf8("pushButton_create"))
        self.spinBox = QtGui.QSpinBox(Form_PasswordCreate)
        self.spinBox.setGeometry(QtCore.QRect(10, 130, 41, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_bits = QtGui.QLabel(Form_PasswordCreate)
        self.label_bits.setGeometry(QtCore.QRect(10, 110, 31, 16))
        self.label_bits.setObjectName(_fromUtf8("label_bits"))
        self.label_sign = QtGui.QLabel(Form_PasswordCreate)
        self.label_sign.setGeometry(QtCore.QRect(0, 20, 54, 51))
        self.label_sign.setText(_fromUtf8(""))
        self.label_sign.setObjectName(_fromUtf8("label_sign"))

        self.retranslateUi(Form_PasswordCreate)
        QtCore.QMetaObject.connectSlotsByName(Form_PasswordCreate)

    def retranslateUi(self, Form_PasswordCreate):
        Form_PasswordCreate.setWindowTitle(_translate("Form_PasswordCreate", "PasswordCreate", None))
        self.checkBox_digits.setText(_translate("Form_PasswordCreate", "Digits ( 0 - 9 )", None))
        self.checkBox_letter.setText(_translate("Form_PasswordCreate", "Letter ( a-z A-Z )", None))
        self.checkBox_specialChar.setText(_translate("Form_PasswordCreate", "special characters ( -_#@ )", None))
        self.pushButton_create.setText(_translate("Form_PasswordCreate", "Create", None))
        self.label_bits.setText(_translate("Form_PasswordCreate", "Bits:", None))

