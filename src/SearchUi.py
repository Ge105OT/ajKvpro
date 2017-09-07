# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchUi.ui'
#
# Created: Tue Aug 29 22:59:32 2017
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

class Ui_Form_Search(object):
    def setupUi(self, Form_Search):
        Form_Search.setObjectName(_fromUtf8("Form_Search"))
        Form_Search.resize(350, 123)
        self.lineEdit_search = QtGui.QLineEdit(Form_Search)
        self.lineEdit_search.setGeometry(QtCore.QRect(30, 20, 211, 20))
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.pushButton_search = QtGui.QPushButton(Form_Search)
        self.pushButton_search.setGeometry(QtCore.QRect(260, 20, 61, 23))
        self.pushButton_search.setObjectName(_fromUtf8("pushButton_search"))
        self.comboBox_table = QtGui.QComboBox(Form_Search)
        self.comboBox_table.setGeometry(QtCore.QRect(70, 70, 91, 22))
        self.comboBox_table.setObjectName(_fromUtf8("comboBox_table"))
        self.comboBox_database = QtGui.QComboBox(Form_Search)
        self.comboBox_database.setGeometry(QtCore.QRect(230, 70, 91, 22))
        self.comboBox_database.setObjectName(_fromUtf8("comboBox_database"))
        self.label_table = QtGui.QLabel(Form_Search)
        self.label_table.setGeometry(QtCore.QRect(30, 70, 41, 20))
        self.label_table.setObjectName(_fromUtf8("label_table"))
        self.label_database = QtGui.QLabel(Form_Search)
        self.label_database.setGeometry(QtCore.QRect(200, 70, 31, 21))
        self.label_database.setObjectName(_fromUtf8("label_database"))

        self.retranslateUi(Form_Search)
        QtCore.QMetaObject.connectSlotsByName(Form_Search)

    def retranslateUi(self, Form_Search):
        Form_Search.setWindowTitle(_translate("Form_Search", "Search", None))
        self.pushButton_search.setText(_translate("Form_Search", "查找", None))
        self.label_table.setText(_translate("Form_Search", "字段：", None))
        self.label_database.setText(_translate("Form_Search", "表：", None))

