# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Direction.ui'
#
# Created: Thu Sep 07 21:35:21 2017
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

class Ui_Form_Direct(object):
    def setupUi(self, Form_Direct):
        Form_Direct.setObjectName(_fromUtf8("Form_Direct"))
        Form_Direct.resize(411, 358)
        self.label_title = QtGui.QLabel(Form_Direct)
        self.label_title.setGeometry(QtCore.QRect(30, 20, 351, 311))
        self.label_title.setObjectName(_fromUtf8("label_title"))

        self.retranslateUi(Form_Direct)
        QtCore.QMetaObject.connectSlotsByName(Form_Direct)

    def retranslateUi(self, Form_Direct):
        Form_Direct.setWindowTitle(_translate("Form_Direct", "Direction", None))
        self.label_title.setText(_translate("Form_Direct", "<html><head/><body><p>ajKvpro:1.0.0<br/></p><p align=\"center\">该软件用于保存个人多个账号密码的安全，减轻大脑记忆，</p><p>记住该软件登录密码，即可查看其他账号密码，方便实用。<br/></p><p align=\"center\">其中账号对应的密码都经过加密存放数据库，登录该软件</p><p>是通过MD5验证，保证没有该软件和其对应账号密码登录，查看</p><p>不到其账号对应的真实的密码。且注册用户的密码也需要8位到</p><p>16为数字字母(可加特殊字符)的组合，更保证登录该软件的安全。<br/></p><p align=\"center\">该软件会生成一个ajKvpro.db的库，用于保存使用者的信息，</p><p>及其保存的账号密码信息。</p><p>更多信息查看readme！</p></body></html>", None))

