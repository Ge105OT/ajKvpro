# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created: Thu Sep 07 21:35:38 2017
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

class Ui_Form_About(object):
    def setupUi(self, Form_About):
        Form_About.setObjectName(_fromUtf8("Form_About"))
        Form_About.resize(261, 113)
        self.label_version = QtGui.QLabel(Form_About)
        self.label_version.setGeometry(QtCore.QRect(70, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        self.label_version.setFont(font)
        self.label_version.setObjectName(_fromUtf8("label_version"))
        self.label_author = QtGui.QLabel(Form_About)
        self.label_author.setGeometry(QtCore.QRect(170, 80, 41, 16))
        self.label_author.setObjectName(_fromUtf8("label_author"))

        self.retranslateUi(Form_About)
        QtCore.QMetaObject.connectSlotsByName(Form_About)

    def retranslateUi(self, Form_About):
        Form_About.setWindowTitle(_translate("Form_About", "About", None))
        self.label_version.setText(_translate("Form_About", "ajKvpro  1.0.0", None))
        self.label_author.setText(_translate("Form_About", "105aj", None))

