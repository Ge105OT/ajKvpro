# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewTable.ui'
#
# Created: Fri Aug 25 00:17:59 2017
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

class Ui_Form_Table(object):
    def setupUi(self, Form_Table):
        Form_Table.setObjectName(_fromUtf8("Form_Table"))
        Form_Table.resize(283, 157)
        self.label_table = QtGui.QLabel(Form_Table)
        self.label_table.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label_table.setObjectName(_fromUtf8("label_table"))
        self.label_type = QtGui.QLabel(Form_Table)
        self.label_type.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.label_type.setObjectName(_fromUtf8("label_type"))
        self.lineEdit_table = QtGui.QLineEdit(Form_Table)
        self.lineEdit_table.setGeometry(QtCore.QRect(100, 30, 151, 20))
        self.lineEdit_table.setObjectName(_fromUtf8("lineEdit_table"))
        self.lineEdit_type = QtGui.QLineEdit(Form_Table)
        self.lineEdit_type.setGeometry(QtCore.QRect(100, 70, 151, 20))
        self.lineEdit_type.setObjectName(_fromUtf8("lineEdit_type"))
        self.pushButton_enSure = QtGui.QPushButton(Form_Table)
        self.pushButton_enSure.setGeometry(QtCore.QRect(80, 110, 51, 23))
        self.pushButton_enSure.setObjectName(_fromUtf8("pushButton_enSure"))
        self.pushButton_cancel = QtGui.QPushButton(Form_Table)
        self.pushButton_cancel.setGeometry(QtCore.QRect(150, 110, 51, 23))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))

        self.retranslateUi(Form_Table)
        QtCore.QMetaObject.connectSlotsByName(Form_Table)

    def retranslateUi(self, Form_Table):
        Form_Table.setWindowTitle(_translate("Form_Table", "NewTable", None))
        self.label_table.setText(_translate("Form_Table", "tablename:", None))
        self.label_type.setText(_translate("Form_Table", "tabletype:", None))
        self.pushButton_enSure.setText(_translate("Form_Table", "OK", None))
        self.pushButton_cancel.setText(_translate("Form_Table", "Cancel", None))

