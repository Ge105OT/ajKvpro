# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UoKeyp.ui'
#
# Created: Sun Aug 20 11:38:35 2017
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(803, 590)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeWidget_database = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget_database.setGeometry(QtCore.QRect(0, 0, 121, 441))
        self.treeWidget_database.setObjectName(_fromUtf8("treeWidget_database"))
        self.treeWidget_database.headerItem().setText(0, _fromUtf8("1"))
        self.textEdit_Log = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_Log.setGeometry(QtCore.QRect(0, 441, 801, 100))
        self.textEdit_Log.setFrameShape(QtGui.QFrame.WinPanel)
        self.textEdit_Log.setReadOnly(True)
        self.textEdit_Log.setObjectName(_fromUtf8("textEdit_Log"))
        self.frame_Info = QtGui.QFrame(self.centralwidget)
        self.frame_Info.setGeometry(QtCore.QRect(120, -1, 681, 441))
        self.frame_Info.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Info.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Info.setObjectName(_fromUtf8("frame_Info"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        self.menu_Tools = QtGui.QMenu(self.menubar)
        self.menu_Tools.setObjectName(_fromUtf8("menu_Tools"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setObjectName(_fromUtf8("action_New"))
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.action_Login = QtGui.QAction(MainWindow)
        self.action_Login.setObjectName(_fromUtf8("action_Login"))
        self.action_AlterPassword = QtGui.QAction(MainWindow)
        self.action_AlterPassword.setObjectName(_fromUtf8("action_AlterPassword"))
        self.action_WriteOff = QtGui.QAction(MainWindow)
        self.action_WriteOff.setObjectName(_fromUtf8("action_WriteOff"))
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("actionExit"))
        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setObjectName(_fromUtf8("action_Copy"))
        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setObjectName(_fromUtf8("action_Cut"))
        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setObjectName(_fromUtf8("action_Paste"))
        self.action_RdomPass = QtGui.QAction(MainWindow)
        self.action_RdomPass.setObjectName(_fromUtf8("action_RdomPass"))
        self.action_Used = QtGui.QAction(MainWindow)
        self.action_Used.setObjectName(_fromUtf8("action_Used"))
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_Login)
        self.menu_File.addAction(self.action_AlterPassword)
        self.menu_File.addAction(self.action_WriteOff)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Tools.addAction(self.action_RdomPass)
        self.menu_Help.addAction(self.action_Used)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ajKvpro", None))
        self.menu_File.setTitle(_translate("MainWindow", "File", None))
        self.menu_Edit.setTitle(_translate("MainWindow", "Edit", None))
        self.menu_Tools.setTitle(_translate("MainWindow", "Tools", None))
        self.menu_Help.setTitle(_translate("MainWindow", "Help", None))
        self.action_New.setText(_translate("MainWindow", "New", None))
        self.action_Open.setText(_translate("MainWindow", "Open", None))
        self.action_Save.setText(_translate("MainWindow", "Save", None))
        self.action_Login.setText(_translate("MainWindow", "Login", None))
        self.action_AlterPassword.setText(_translate("MainWindow", "AlterPass", None))
        self.action_WriteOff.setText(_translate("MainWindow", "WriteOff", None))
        self.action_Exit.setText(_translate("MainWindow", "Exit", None))
        self.action_Copy.setText(_translate("MainWindow", "Copy", None))
        self.action_Cut.setText(_translate("MainWindow", "Cut", None))
        self.action_Paste.setText(_translate("MainWindow", "Paste", None))
        self.action_RdomPass.setText(_translate("MainWindow", "RdomPass", None))
        self.action_Used.setText(_translate("MainWindow", "Direction", None))
        self.action_About.setText(_translate("MainWindow", "About", None))

