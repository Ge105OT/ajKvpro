# -*- coding:utf-8 -*-
# date:2017-7-16

import sys, time, os
import re
import random
from PyQt4 import QtCore, QtGui
import UoKeyp
import NewUi
import LoginUi
import NewTableUi
import NewRecordUi
import AlterPasswordUi
import PasswordCreatorUi
import SearchUi
import DirectUi
import AboutUi
import Sqlite3Work
from encryt import md5enc, Aes_encrypt, Aes_decrypt, iv_create

tree_list = ["table", "colume"]

# main class
class ajKvpro(QtGui.QMainWindow, UoKeyp.Ui_MainWindow):  
    def __init__(self, parent=None):
        super(ajKvpro, self).__init__(parent)
        self.setupUi(self)
        self.ui_Member()

        self.list_color = [QtGui.QColor(255, 255, 255), QtGui.QColor(246, 246, 246)]

        self.Statu_ajKvpro()
        self.InitUi()
        self.table_UserKey()
        self.action_Var()

    def InitUi(self):
         # 工具栏
        self.new_Bar = QtGui.QAction(QtGui.QIcon("..\\img\\report.ico"), "New", self)
        self.open_Bar = QtGui.QAction(QtGui.QIcon("..\\img\\open.ico"), "Open", self)
        self.save_Bar = QtGui.QAction(QtGui.QIcon("..\\img\\save.ico"), "Save", self)
        self.key_Bar = QtGui.QAction(QtGui.QIcon("..\\img\\key.ico"), "Key", self)
        self.WriteOff_Bar = QtGui.QAction(QtGui.QIcon("..\\img\\Sign_Out.ico"), "WriteOff", self)
        self.switch_Bar = QtGui.QAction(QtGui.QIcon("..\\img\\user.ico"), "switch", self)
        self.search_Bar = QtGui.QAction(QtGui.QIcon("..\\img\\search.ico"), "search", self)
        self.Lock_Bar = QtGui.QAction(QtGui.QIcon("..\\img\\lock.ico"), "Lock", self)
        self.action_New.setIcon(QtGui.QIcon("..\\img\\report.ico"))
        self.action_Open.setIcon(QtGui.QIcon("..\\img\\open.ico"))
        self.action_Save.setIcon(QtGui.QIcon("..\\img\\save.ico"))
        self.action_Copy.setIcon(QtGui.QIcon("..\\img\\copy.ico"))
        self.action_Cut.setIcon(QtGui.QIcon("..\\img\\cut.ico"))
        self.action_Paste.setIcon(QtGui.QIcon("..\\img\\paste.ico"))
        self.action_Used.setIcon(QtGui.QIcon("..\\img\\direction.ico"))
        self.action_About.setIcon(QtGui.QIcon("..\\img\\about.ico"))
        self.action_RdomPass.setIcon(QtGui.QIcon("..\\img\\generator.ico"))

        self.toolbar = self.addToolBar('Func')
        self.toolbar.addAction(self.new_Bar)
        self.toolbar.addAction(self.open_Bar)
        self.toolbar.addAction(self.save_Bar)
        self.toolbar.addAction(self.key_Bar)
        self.toolbar.addAction(self.WriteOff_Bar)
        self.toolbar.addAction(self.switch_Bar)
        self.toolbar.addAction(self.search_Bar)
        self.toolbar.addAction(self.Lock_Bar)

        # 设置部件的列数为1  
        self.treeWidget_database.setColumnCount(1) 
        self.treeWidget_database.setHeaderLabel('data') 
        self.treeWidget_database.setColumnWidth(0, 120)

        self.action_Open.setShortcut('Ctrl+O')
        self.action_Save.setShortcut('Ctrl+S')
        self.action_New.setShortcut('Ctrl+N')
        self.action_Copy.setShortcut('Ctrl+C')
        self.action_Cut.setShortcut('Ctrl+X')
        self.action_Paste.setShortcut('Ctrl+P')
        self.search_Bar.setShortcut('Ctrl+F')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\\img\\password.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.screeWid = QtGui.QWidget(self)
        pe = QtGui.QPalette()  
        pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.red)  
        self.screeWid.setAutoFillBackground(True)  
        pe.setColor(QtGui.QPalette.Window, QtCore.Qt.blue)  
        # pe.setColor(QtGui.QPalette.Background,Qt.blue)  
        self.screeWid.setPalette(pe)
        self.pictureScreen = QtGui.QLabel(self.screeWid)
        self.pictureScreen.setPixmap(QtGui.QPixmap("..\\img\\screen.ico"))
        self.pass_edit = QtGui.QLineEdit(self.screeWid)
        self.pass_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.screeWid.hide()

        self.resize(430, 400)
        self.Login()
        pass

    def ui_Member(self):
        self.sql = None
        self.database = None
        self.key = ""
        self.user = ""
        self.tree_table = None
        self.tree_Type = None
        self.statu = False
        self.isSave = False
        self.isTable = False
        self.ui_x = 0
        self.ui_y = 0
        self.tree_endx = 0
        self.log_y = 0
        self.tree_move_tmp = 0
        self.log_move_tmp = 0 
        self.alter_tree = False
        self.alter_log = False
        self.click_table_dict = {}
        self.change_table_dict = {}
        self.tableName_dict = {}
        self.edit_tableItem = True
        self.isLock = False
        self.searchTable = None
        self.searchFouse = False
        self.searchIndex = 0
        pass

    def table_UserKey(self):
        self.init_tabel = QtGui.QTableWidget(self.frame_Info)
        iWidth = self.frame_Info.width()
        iHeight = self.frame_Info.height()
        self.init_tabel.setGeometry(QtCore.QRect(0, 0, iWidth, iHeight))
        self.init_tabel.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        self.init_tabel.setColumnCount(3)
        self.init_tabel.setHorizontalHeaderLabels(['username', 'password', 'web'])
        # self.init_tabel.setShowGrid(False)
        self.init_tabel.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        pass

    def Statu_ajKvpro(self):
        self.label_statu = QtGui.QLabel(self.statusBar())
        text = "ajKvpro: 1.0.0"
        self.label_statu.setText(text)
        self.statusBar().insertWidget(0, self.label_statu, 2)

        self.label_login_statu = QtGui.QLabel(self.statusBar())
        login_text = u"状态："
        self.label_login_statu.setText(login_text)
        self.statusBar().insertWidget(1, self.label_login_statu, 2)

        self.label_user_statu = QtGui.QLabel(self.statusBar())
        user_text = u"用户："
        self.label_user_statu.setText(user_text)
        self.statusBar().insertWidget(2, self.label_user_statu, 2)

        self.label_table_statu = QtGui.QLabel(self.statusBar())
        table_text = u"表名："
        self.label_table_statu.setText(table_text)
        self.statusBar().insertWidget(3, self.label_table_statu, 2)

        self.label_time = QtGui.QLabel(self.statusBar())
        dtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.label_time.setText(dtime)
        self.statusBar().insertWidget(4, self.label_time, 1)

        # self.pd = QtGui.QProgressBar(self.statusBar())
        # self.pd.setTextVisible(False)
        # self.statusBar().addPermanentWidget(self.pd, 1)
        pass

    def resize_ctrl(self, ui_width, ui_height):
        tree_width = self.treeWidget_database.width()
        log_height = self.textEdit_Log.height()
        log_pos_y = ui_height - log_height - 95
        info_width = ui_width - tree_width

        self.screeWid.setGeometry(QtCore.QRect(0, 0, ui_width, ui_height))
        spos_x = (ui_width - 130) / 2
        spos_y = (ui_height - 130) / 2
        self.pictureScreen.setGeometry(QtCore.QRect(spos_x, spos_y, 130, 130))
        self.pass_edit.setGeometry(QtCore.QRect(spos_x, spos_y + 150, 130, 20))
        self.treeWidget_database.setFixedHeight(log_pos_y)
        self.frame_Info.setGeometry(QtCore.QRect(tree_width, 0, info_width, log_pos_y))
        self.init_tabel.setFixedSize(info_width, log_pos_y)

        self.textEdit_Log.setGeometry(QtCore.QRect(0, log_pos_y, ui_width, log_height))

        
        ix1 = self.init_tabel.columnWidth(0)
        ix2 = self.init_tabel.columnWidth(1)
        ix3 = self.init_tabel.columnWidth(2)
        ix = ix1 + ix2 + ix3
        iPrex1 = 0
        iPrex2 = 0
        iPrex3 = 0
        table_width = info_width - 3
        if ix == 0:
            iPrex1 = table_width / 3
            iPrex2 = table_width / 3
            iPrex3 = table_width / 3
        else:     
            iPrex1 = table_width * ix1 / ix
            iPrex2 = table_width * ix2 / ix
            iPrex3 = table_width * ix3 / ix

        self.init_tabel.setColumnWidth(0, iPrex1)                   # 将第2列的单元格，设置成50宽度
        self.init_tabel.setColumnWidth(1, iPrex2)
        self.init_tabel.setColumnWidth(2, iPrex3)

    def paintEvent(self, e):
        ui_height = self.height()
        log_height = self.textEdit_Log.height() + 100
        if (ui_height < log_height):
            return
        self.resize_ctrl(self.width(), ui_height)
        pass

    def closeEvent(self, e):
        if self.isSave:
            button = QtGui.QMessageBox.question(self, "Exit", "Would you save the change?",
                                        QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            if button == QtGui.QMessageBox.Ok:
                self.Save_Change()
        self.isSave = False
        self.click_table_dict.clear()
        if self.sql:
            self.sql.sqlClose()
        print "close"
        pass

    # main ui event
    def action_Var(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_Open.triggered.connect(self.Open_Database)
        self.open_Bar.triggered.connect(self.Open_Database)
        self.action_New.triggered.connect(self.New_UserOrBase)
        self.new_Bar.triggered.connect(self.New_UserOrBase)
        self.action_Login.triggered.connect(self.Login)
        self.switch_Bar.triggered.connect(self.Login)
        self.key_Bar.triggered.connect(self.Change_Password)
        self.action_AlterPassword.triggered.connect(self.Change_Password)
        self.action_RdomPass.triggered.connect(self.Create_Password)
        self.action_WriteOff.triggered.connect(self.Sign_Out)
        self.WriteOff_Bar.triggered.connect(self.Sign_Out)
        self.action_Save.triggered.connect(self.Save_Change)
        self.save_Bar.triggered.connect(self.Save_Change)
        self.search_Bar.triggered.connect(self.Search)
        self.Lock_Bar.triggered.connect(self.Lock_Ui)
        self.action_Copy.triggered.connect(self.Copy_itemText)
        self.action_Cut.triggered.connect(self.Cut_itemText)
        self.action_Paste.triggered.connect(self.Paste_itemText)
        self.action_Used.triggered.connect(self.Direction)
        self.action_About.triggered.connect(self.About)

        self.connect(self.treeWidget_database, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.Click_Tree)
        self.connect(self.init_tabel, QtCore.SIGNAL('itemDoubleClicked(QTableWidgetItem*)'), self.outSelect)           # 将itemClicked信号与函数outSelect绑定
        self.connect(self.init_tabel, QtCore.SIGNAL('itemChanged(QTableWidgetItem*)'), self.change_tablePassword)      # 将itemClicked信号与函数outSelect绑定

        self.treeWidget_database.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)     # 允许右键产生子菜单
        self.treeWidget_database.customContextMenuRequested.connect(self.tree_Menu)     # 检测鼠标右键

        self.init_tabel.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)     # 允许右键产生子菜单
        self.init_tabel.customContextMenuRequested.connect(self.table_Menu)   # 右键菜单
        self.init_tabel.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # 设置为可以选中多个目标
        
        pass

    def Open_Database(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self, "database", "..\\", "base(*.db)")
        # print file_name
        pass

    def New_UserOrBase(self):
        if self.statu:         
            if (self.tree_Type == tree_list[0]):
                # print "create record to", self.tree_Select
                tablename = self.user + '_' + self.tree_table
                new_record = NewRecord_ajK(self)
                new_record.setDatabase(self.sql, tablename)
                new_record.setKey_iv(self.key, self.user)
                new_record.exec_()
                isAdd, username, password, web = new_record.retNewRecord_create()
                if isAdd:
                    logtxt = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time())) + self.user + u'增加一条用户密码记录'
                    self.textEdit_Log.append(logtxt)
                    self.add_record2Table(tablename, username, password, web)
            elif (self.tree_Type == tree_list[2]):
                print "select ", self.tree_table
            else:
                print "error"
        else:
            QtGui.QMessageBox.warning(self, "warning", "not login!",
                                      QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        pass

    def Login(self):
        if self.statu:
            print "have login"
            pass
        else:
            user_Login = Login_ajK(self)
            user_Login.exec_()
            self.statu, user, self.key = user_Login.Ret_Login()
            if self.statu:
                text = u'用户：' + user
                self.label_user_statu.setText(text)
                login_text = u'状态：已登录'
                self.label_login_statu.setText(login_text)
                self.user = user
                self.TreeWidget_data(user)
                logtxt = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time())) + user + u'用户登录'
                self.textEdit_Log.append(logtxt)
        pass

    def TreeWidget_data(self, username):
        iLen = len(username) + 1
        self.sql = Sqlite3Work.Sqlite3Worker('ajKvpro.db')
        sql_ret = self.sql.execute("SELECT database FROM user where username = ?;", (username, ))        # search the user is exit
        self.database = sql_ret[0][0]
        # print database

        tables_list = []
        tables = self.sql.execute("select tablename, type from " + self.database + ";")
        for table in tables:
            tableName = table[0]
            tables_list.append(tableName)

            table = tableName[iLen: ]
            # 设置根节点的名称  
            root = QtGui.QTreeWidgetItem(self.treeWidget_database)
            root.setText(0, table)
           
            table_colums = self.sql.execute("PRAGMA table_info(" + tableName + ");")
            for table_colum in table_colums:
                colum_name = table_colum[1]
                colum_child = QtGui.QTreeWidgetItem(root)
                colum_child.setText(0, colum_name)
        self.tableName_dict[self.database] = tables_list
        pass

    def Click_Tree(self, item, column):
        self.tree_table = unicode(item.text(0), 'utf-8', 'ignore')
        parent = item.parent()
        i = 0
        while parent:
            i += 1
            parent = parent.parent()
        self.tree_Type = tree_list[i]

        # click table item 
        if i == 0:
            # self.init_tabel.clear()
            self.isTable = True
            tablename = self.tree_table
            self.ShowTable(tablename)
        else:
            self.isTable = False
        pass

    def ShowTable(self, table):
        table_text = u'表名：' + table
        tablename = self.user + '_' + table
        self.label_table_statu.setText(table_text)
        if (tablename not in self.click_table_dict.keys()):
            self.addToTableDict(tablename)
            self.show_dictTable(tablename)
        else:
            self.show_dictTable(tablename)
        pass

    def addToTableDict(self, tablename):
        iv = iv_create(self.user + tablename)
        # print self.key, iv
        table_sql = self.sql.execute("select * from " + tablename + ";")
        list_table = []
        for item in table_sql:
            password = Aes_decrypt(item[1], self.key, iv)
            item_list = [item[0], password, item[2]]
            list_table.append(item_list)
        self.click_table_dict[tablename] = list_table
        pass

    def show_dictTable(self, tablename):
        self.edit_tableItem = False
        list_table = self.click_table_dict[tablename]
        self.init_tabel.setRowCount(len(list_table))
        iCout = 1
        for item in list_table:
            color = self.list_color[iCout % 2]

            newItem = QtGui.QTableWidgetItem(item[0], -1)
            newItem.setBackgroundColor(color) 
            self.init_tabel.setItem(iCout - 1, 0, newItem)

            
            newItem = QtGui.QTableWidgetItem(item[1], -1)
            newItem.setBackgroundColor(color) 
            self.init_tabel.setItem(iCout - 1, 1, newItem)

            newItem = QtGui.QTableWidgetItem(item[2], -1)
            newItem.setBackgroundColor(color) 
            self.init_tabel.setItem(iCout - 1, 2, newItem)
            iCout += 1
        self.edit_tableItem = True
        pass

    def add_record2Table(self, tablename, username, password, web):
        record_list = [username, password, web]
        table_dict = self.click_table_dict[tablename]
        table_dict.append(record_list)
        self.click_table_dict[tablename] = table_dict
        self.show_dictTable(tablename)
        pass

    def Change_Password(self):
        if self.user is None or self.user == "" or self.statu is False:
            return
        else:    
            change_pass = Change_Password_ajK()
            change_pass.setUser(self.user)
            change_pass.exec_()
            isAlter, key = change_pass.ret_changePassword()
            if isAlter:
                logtxt = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time())) + self.user + u'修改了密码'
                self.textEdit_Log.append(logtxt)
                self.ChangeAllPassword(key)
        pass

    def Create_Password(self):
        ramdonPass = Password_Creator_ajK()
        ramdonPass.exec_()
        pass

    def ChangeAllPassword(self, key):
        basetable = self.user + '_tables'
        tables = self.sql.execute("select tablename, type from " + basetable + ";")
        for table in tables:
            # print 'table list'
            tableName = table[0]
            iv = iv_create(self.user + tableName)
            if (tableName in self.click_table_dict.keys()):
                table_dict = self.click_table_dict[tableName]
                for item in table_dict:
                    password = Aes_encrypt(item[1], key, iv)
                    self.sql.execute("update " + tableName + " set password = ? where username = ? and web = ?", (password, item[0], item[2]))
            # print key, iv
            else:    
                user_web = self.sql.execute("select username, password, web from " + tableName + ";")
                for username, old_password, web in user_web:
                    # print username, old_password, web
                    dec_oldPassword = Aes_decrypt(old_password, self.key, iv)
                    
                    password = Aes_encrypt(dec_oldPassword, key, iv)
                    self.sql.execute("update " + tableName + " set password = ? where username = ? and web = ?", (password, username, web))

        self.key = key
        pass

    def Sign_Out(self):
        if self.statu:
            if self.isSave:
                button = QtGui.QMessageBox.question(self, "Exit", "Would you save the change?",
                                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
                if button == QtGui.QMessageBox.Ok:
                    self.Save_Change()
            self.isSave = False
            self.click_table_dict.clear()
            logtxt = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time())) + self.user + u'用户退出登录'
            self.textEdit_Log.append(logtxt)
            self.statu = False
            self.init_tabel.setRowCount(0)
            self.sql.sqlClose()
            self.sql = None
            self.user = None
            self.key = None
            self.treeWidget_database.clear()
            self.label_login_statu.setText(u'状态：未登录')
            self.label_user_statu.setText(u'用户：')
            self.label_table_statu.setText(u'表名：')
        else:
            QtGui.QMessageBox.warning(self, "warning", "No user logged on",
                                      QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        pass

    def table_Menu(self, pos):
        print pos
        selItem = self.init_tabel.selectedRanges()
        if len(selItem) > 1:
            row_list = []
            for row in selItem:
                row_list.append(row.topRow())

            menu = QtGui.QMenu()
            delAll = menu.addAction(QtGui.QIcon("..\\img\\delete.ico"), u"删除选中项")
            action = menu.exec_(self.init_tabel.mapToGlobal(pos))
            if action == delAll:
                self.delete_selItem(row_list)
                

        else:
            item = self.init_tabel.currentItem()  
            if item:
                row = item.row()
                menu = QtGui.QMenu()
                copyUser = menu.addAction(QtGui.QIcon("..\\img\\copy.ico"), u"复制用户名")
                copyKey = menu.addAction(QtGui.QIcon("..\\img\\copy.ico"), u"复制密码")
                changeKey = menu.addAction(QtGui.QIcon("..\\img\\modify.ico"), u"修改密码")
                deleteRecord = menu.addAction(QtGui.QIcon("..\\img\\delete.ico"), u"删除记录" )
                action = menu.exec_(self.init_tabel.mapToGlobal(pos))
                if action == copyUser:
                    clipboard = QtGui.QApplication.clipboard()
                    username = unicode(self.init_tabel.item(row, 0).text().toUtf8(), 'utf-8', 'ignore')
                    clipboard.setText(username)

                elif action == copyKey:
                    clipboard = QtGui.QApplication.clipboard()
                    copytext = unicode(self.init_tabel.item(row, 1).text().toUtf8(), 'utf-8', 'ignore')
                    clipboard.setText(copytext)
                    # print u'您选了选项一，当前行文字内容是：', self.init_tabel.item(row, 0).text()

                elif action == changeKey:
                    item_edit = self.init_tabel.item(row, 1)
                    self.init_tabel.editItem(item_edit)
                    # print u'您选了选项二，当前行文字内容是：', self.init_tabel.item(row, 0).text()

                elif action == deleteRecord:
                    table = self.user + '_' + self.tree_table
                    username = unicode(self.init_tabel.item(row, 0).text().toUtf8(), 'utf-8', 'ignore')
                    web = unicode(self.init_tabel.item(row, 2).text().toUtf8(), 'utf-8', 'ignore')
                    self.sql.execute('delete from ' + table + ' where username = ? and web = ?;', (username, web))
                    table_dict = self.click_table_dict[table]
                    del table_dict[row]
                    self.init_tabel.removeRow(row)
                    self.delete_changeTableList(table, username, web)
                    logtxt = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time())) + self.user + u'用户删除了记录 user=' + username
                    self.textEdit_Log.append(logtxt)
                    # print u'您选了选项三，当前行文字内容是：', self.init_tabel.item(row, 0).text()
                else:
                    return
        pass

    def tree_Menu(self, point):
        if self.isTable:
            menu = QtGui.QMenu()
            addItem = menu.addAction(u"增加数据")
            item2 = menu.addAction(u"增加新表")
            action = menu.exec_(self.treeWidget_database.mapToGlobal(point))
            if action == addItem:
                self.New_UserOrBase()
                # print u'您选了选项一，当前行文字内容是：'

            elif action == item2:
                new_table = NewTable_ajK(self)
                new_table.setDatabase(self.sql, self.user)
                new_table.exec_()
                isAdd, tablename = new_table.retnNewTable()
                if isAdd:
                    logtxt = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time())) + self.user + u'用户增加表：' + tablename
                    self.textEdit_Log.append(logtxt)
                # print u'您选了选项二，当前行文字内容是：'
            else:
                return
        pass

    def outSelect(self, item = None):
        if (item.column() == 1):
            self.init_tabel.editItem(item)
        # print self.init_tabel.item(item.row(), 1).text()
        pass

    def change_tablePassword(self, item = None):
        if self.edit_tableItem:
            self.isSave = True
            # print item.text()
            row = item.row()
            username = unicode(self.init_tabel.item(row, 0).text().toUtf8(), 'utf-8', 'ignore')
            web = unicode(self.init_tabel.item(row, 2).text().toUtf8(), 'utf-8', 'ignore')
            password = unicode(item.text().toUtf8(), 'utf-8', 'ignore')
            tablename = self.tree_table
            self.edit_ChangeTableList(tablename, username, password, web)
            self.edit_showTableList(tablename, password, row)
        pass

    def Save_Change(self):
        tablenames = self.change_table_dict.keys()
        key = self.key
        for table in tablenames:
            iv = iv_create(self.user + table)
            item_list = self.change_table_dict[table]
            for items in item_list:
                password = Aes_encrypt(items[1], key, iv)
                self.sql.execute("update " + table + " set password = ? where username = ? and web = ?", (password, items[0], items[2]))
        self.change_table_dict.clear()
        self.isSave = False
        pass

    def Search(self):
        if self.statu:
            if self.searchTable is None:
                self.searchTable = Search_ajK(self)
                tableList = self.tableName_dict[self.database]
                self.searchTable.setCommbox(tableList, len(self.user) + 1)
                self.connect(self.searchTable, QtCore.SIGNAL('clickSearch(QString, QString, QString)'), self.Search_table)      # Sub-window with parent window for signal and slot settings
                self.connect(self.searchTable, QtCore.SIGNAL('clickSearchUi(bool)'), self.setSearchFouse)
                self.connect(self.searchTable, QtCore.SIGNAL('setSearchNone()'), self.setSearchClose)
                self.connect(self.searchTable, QtCore.SIGNAL('setSearchZero()'), self.setSearchIndexZero)
                self.searchTable.setWindowOpacity(1)
                self.searchTable.show()
                self.searchIndex = 0
                # self.searchTable = QtCore.QEventLoop()             #   line  3
                # self.searchTable.exec_()
        pass

    def Search_table(self, tablename, tabletype, searchStr):
        # print table, tabletype, searchStr
        table = self.user + '_' + tablename
        table_list = self.tableName_dict[self.database]
        dateTxt = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time()))
        for table in table_list:
            if tabletype == u'全部':
                if table not in self.click_table_dict.keys():
                    self.addToTableDict(table)
                table_txtList = self.click_table_dict[table]
                iLen = len(table_txtList)
                if self.searchIndex >= iLen:
                    self.searchIndex = 0
                index = self.searchIndex
                while index < iLen:
                    if searchStr in table_txtList[index]:
                        logTxt = dateTxt +  'user:' + self.init_tabel.item(index, 0).text() + ';  password:' + self.init_tabel.item(index, 1).text() + ';  web:' + self.init_tabel.item(index, 2).text()
                        self.textEdit_Log.append(logTxt)
                        self.searchIndex += 1
                        break
                    self.searchIndex += 1
                    index += 1
            else:
                iPos = 0
                if tabletype == 'password':
                    iPos = 1
                elif tabletype == 'web':
                    iPos = 2
                if table not in self.click_table_dict.keys():
                    self.addToTableDict(table)

                table_txtList = self.click_table_dict[table]
                iLen = len(table_txtList)
                if self.searchIndex >= iLen:
                    self.searchIndex = 0
                index = self.searchIndex
                while index < iLen:
                    if searchStr == table_txtList[index][iPos]:
                        logTxt = dateTxt +  'user:' + self.init_tabel.item(index, 0).text() + ';  password:' + self.init_tabel.item(index, 1).text() + ';  web:' + self.init_tabel.item(index, 2).text()
                        self.textEdit_Log.append(logTxt)
                        self.searchIndex += 1
                        break
                    self.searchIndex += 1
                    index += 1                                      
        pass

    def setSearchClose(self):
        self.searchTable = None

    def setSearchIndexZero(self):
        self.searchIndex = 0

    def setSearchFouse(self, bToF):
        self.searchFouse = bToF
        pass

    def Lock_Ui(self):
        if self.statu:
            self.screeWid.show()
            self.isLock = True
            if self.searchTable:
                self.searchTable.close()
        pass

    # filter the event 
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton:
                pos = event.globalPos()
                x = pos.x()
                y = pos.y()
                # print x, y
                if ((x >= self.tree_endx - 1) and (x <= self.tree_endx + 1) and (y > self.ui_y + 55) and (y < self.log_y)):
                    self.setCursor(QtCore.Qt.SizeHorCursor)
                    self.alter_tree = True
                    self.alter_log = False
                elif (y >= self.log_y) and (y <= self.log_y + 2):
                    self.setCursor(QtCore.Qt.SizeVerCursor)
                    self.alter_log = True
                    self.alter_tree = False
                else:
                    self.setCursor(QtCore.Qt.ArrowCursor)
                    self.alter_log = False
                    self.alter_tree = False
            else:
                pass # do other stuff
        elif event.type() == QtCore.QEvent.MouseButtonPress:        # mouse click
            if self.alter_log:
                pos = event.globalPos()
                self.log_move_tmp = pos.y()
                print pos
            elif self.alter_tree:
                pos = event.globalPos()
                self.tree_move_tmp = pos.x()
                print pos
            else:
                # print self.searchFouse
                if self.searchTable is not None:
                    if self.searchFouse is False:
                        self.searchTable.setWindowOpacity(0.5)
                    else:
                        self.searchTable.setWindowOpacity(1)
                print "press"
            
        elif event.type() == QtCore.QEvent.Move:        # mouse move
            rect = self.geometry()
            print rect
            self.ui_x = rect.x()
            self.ui_y = rect.y()
            self.tree_endx = self.ui_x + self.treeWidget_database.width()
            self.log_y = self.ui_y + self.textEdit_Log.y() + self.menu_File.y() + 55

        elif event.type() == QtCore.QEvent.MouseButtonRelease:      # mouse click release
            if self.isLock:
                pass
            elif self.alter_log:
                pos = event.globalPos()
                height = pos.y() - self.log_move_tmp
                alter_height = self.textEdit_Log.height() - height
                ui_height = self.height()
                if (alter_height > 60 and alter_height < ui_height - 200):
                    self.textEdit_Log.setFixedHeight(alter_height)
                    self.resize_ctrl(self.width(), ui_height)
                print pos, alter_height
            elif self.alter_tree:
                pos = event.globalPos()
                width = pos.x() - self.tree_move_tmp
                alter_width = self.treeWidget_database.width() + width
                ui_width = self.width()
                if (alter_width > 50 and alter_width < ui_width - 200):
                    self.treeWidget_database.setFixedWidth(alter_width)
                    self.resize_ctrl(ui_width, self.height())
                print pos
            else:
                print "reslese"

        elif event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Enter - 1:
                if self.isLock:
                    text = unicode(self.pass_edit.text().toUtf8(), 'utf-8', 'ignore')
                    if (text != "" and text is not None):
                        pwd_md5 = md5enc(text)
                        sql = Sqlite3Work.Sqlite3Worker("ajKvpro.db")
                        ret = sql.execute("SELECT * FROM user where username = ? and password = ?;", (self.user, pwd_md5))
                        sql.sqlClose()
                        if len(ret):
                            self.screeWid.hide()
                            self.isLock = False
                        self.pass_edit.clear()
            pass
        return QtGui.QMainWindow.eventFilter(self, source, event)

    # edit the list change
    def edit_ChangeTableList(self, tablename, username, password, web):
        if (tablename in self.change_table_dict.keys()):
            table_dict = self.change_table_dict[tablename]
            isExit, row = self.search_tableList(self.change_table_dict, tablename, username, web)
            if isExit:
                table_dict[row][1] = password
            else:
                list_item = [username, password, web]
                table_dict.append(list_item)
            self.change_table_dict[tablename] = table_dict
        else:
            table_dict = []
            list_item = [username, password, web]
            table_dict.append(list_item)
            self.change_table_dict[tablename] = table_dict
        pass

    # edit the dict table
    def edit_showTableList(self, tablename, password, row):
        ctable_dict = self.click_table_dict[tablename]
        ctable_dict[row][1] = password
        self.click_table_dict[tablename] = ctable_dict
        pass

    # delete the dict change
    def delete_changeTableList(self, tablename, username, web):
        if (tablename in self.change_table_dict.keys()):
            table_dict = self.change_table_dict[tablename]
            isExit, row = self.search_tableList(self.change_table_dict, tablename, username, web)
            if isExit:
                del table_dict[row]
                self.change_table_dict[tablename] = table_dict
        pass

    # is exit in the change dict
    def search_tableList(self, tablelist, tablename, username, web):
        table_dict = tablelist[tablename]
        i = 0
        for item in table_dict:
            if username == item[0] and web == item[2]:
                return True, i
            i += 1
        return False, -1
        pass

    def delete_selItem(self, row_list):
        table = self.tree_table
        iLen= len(row_list)
        if (iLen > 0):
            logtxt = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time())) + self.user + u'用户删除了' + iLen + '条记录，分别为：'
            self.textEdit_Log.append(logtxt)
        while iLen > 0:
            row = row_list.pop()
            username = unicode(self.init_tabel.item(row, 0).text().toUtf8(), 'utf-8', 'ignore')
            web = unicode(self.init_tabel.item(row, 2).text().toUtf8(), 'utf-8', 'ignore')
            self.sql.execute('delete from ' + table + ' where username = ? and web = ?;', (username, web))
            table_dict = self.click_table_dict[table]
            del table_dict[row]
            self.delete_changeTableList(table, username, web)
            self.init_tabel.removeRow(row)
            logtxt = 'user=' + username
            self.textEdit_Log.append(logtxt)
        pass

    def Copy_itemText(self, parameter_list):
        item = self.init_tabel.currentItem()  
        if item:
            row = item.row()
            copytext = unicode(self.init_tabel.item(row, 1).text().toUtf8(), 'utf-8', 'ignore')
            clipboard = QtGui.QApplication.clipboard()
            clipboard.setText(copytext)
        pass

    def Cut_itemText(self, parameter_list):
        item = self.init_tabel.currentItem()  
        if item:
            row = item.row()
            copytext = unicode(self.init_tabel.item(row, 1).text().toUtf8(), 'utf-8', 'ignore')
            clipboard = QtGui.QApplication.clipboard()
            clipboard.setText(copytext)
            self.init_tabel.item(row, 1).setText("")
        pass

    def Paste_itemText(self, parameter_list):
        item = self.init_tabel.currentItem()  
        if item:
            row = item.row()
            copytext = unicode(self.init_tabel.item(row, 1).text().toUtf8(), 'utf-8', 'ignore')
            clipboard = QtGui.QApplication.clipboard()
            self.init_tabel.item(row, 1).setText(clipboard.text())
        pass

    def Direction(self):
        dire = Direction_ajK(self)
        dire.exec_()
        pass

    def About(self):
        about = About_ajK(self)
        about.exec_()
        pass

# new user class
class New_User_ajK(QtGui.QDialog, NewUi.Ui_Form_New):
    def __init__(self, parent = None):
        super(New_User_ajK, self).__init__(parent)
        self.setupUi(self)
        self.sqlit = None
        self.initUi()
        self.action_btn()

    def initUi(self):
        self.lineEdit_Password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_ConfirmPassword.setEchoMode(QtGui.QLineEdit.Password)
        pass

    def action_btn(self):
        self.pushButton_Ensure.clicked.connect(self.Click_EnsureBtn)
        self.pushButton_Cancel.clicked.connect(self.Click_CancelBtn)
        pass

    # click sure btn
    def Click_EnsureBtn(self):
        password = unicode(self.lineEdit_Password.text().toUtf8(), 'utf-8', 'ignore')
        username = unicode(self.lineEdit_User.text().toUtf8(), 'utf-8', 'ignore')
        confim = unicode(self.lineEdit_ConfirmPassword.text().toUtf8(), 'utf-8', 'ignore')

        # ^(?!(?:[^a-zA-Z]|\D|[a-zA-Z0-9])$).{8,}$  ^.{8,}(?:?<!(?:[^a-zA-Z]|\D|[a-zA-Z0-9]))$  ^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,16}$
        isMatch = re.match(r'^(?![0-9]+$)(?![a-zA-Z]+$)[\w\-]{8,16}$', password)
        if (password == "" or username == ""):
            QtGui.QMessageBox.warning(self, "warning", "not allow empty",
                                      QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return

        elif isMatch is None:
            QtGui.QMessageBox.warning(self, "warning", "The password must be a numeric letter from 8 to 16 digits or a combination of special characters",
                                      QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)         
            return

        elif password == confim:
            if self.sqlit is None:
                self.sqlit = Sqlite3Work.Sqlite3Worker('ajKvpro.db')
            self.sqlit.execute('''CREATE TABLE IF NOT EXISTS user( 
                            username char(25) PRIMARY KEY,
                            password char(33),
                            database char(30)
                            );''')
            sql_ret = self.sqlit.execute("SELECT * FROM user where username = ?;", (username, ))        # search the user is exit
            if len(sql_ret) > 0:
                QtGui.QMessageBox.warning(self, "error", "please new anther user",
                                        QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                return
            
            database = username + '_tables'
            userbase = username + '_base'
            password_md5 = md5enc(password)
            self.sqlit.execute("insert into user (username, password, database) values (?, ?, ?);" , (username, password_md5, database))    # insert record to user table
            self.sqlit.execute('CREATE TABLE IF NOT EXISTS ' + database + '''( 
                            tablename char(50) primary key,
                            type char(16)
                            );''')
            self.sqlit.execute("insert into " + database + " (tablename, type) values (?, ?);", (userbase, 'base'))
            self.sqlit.execute('CREATE TABLE IF NOT EXISTS ' + userbase + '''( 
                            username char(50),
                            password text,
                            web char(50),
                            primary key (username, web)
                            );''')
            self.sqlit.sqlClose()
            QtGui.QMessageBox.information(self, "New", "new success!")
            self.close()
        else:
            QtGui.QMessageBox.warning(self, "error", "Two passwords are inconsistent",
                                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        pass

    # cancel btn click
    def Click_CancelBtn(self):
        button = QtGui.QMessageBox.question(self, "Exit", "Would you exit add user!!!",
                                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
        if button == QtGui.QMessageBox.Ok:
            self.close()
        elif button == QtGui.QMessageBox.Cancel:
            return
        else:
            return
        pass

    def closeEvent(self, e):
        if self.sqlit:
            self.sqlit.sqlClose()
        pass

# login class
class Login_ajK(QtGui.QDialog, LoginUi.Ui_Form_Login):
    def __init__(self, parent = None):
        super(Login_ajK, self).__init__(parent)
        self.setupUi(self)
        self.sqlit = None
        self.Login_stuta = False
        self.user = ""
        self.key = ""
        self.initUi()
        self.action_Btn()

    def initUi(self):
        self.lineEdit_Password.setEchoMode(QtGui.QLineEdit.Password)
        self.lable_signup_x = self.label_signup.x();
        self.lable_signup_y = self.label_signup.y();
        self.label_signup_w = self.lable_signup_x + self.label_signup.width()
        self.label_signup_h = self.lable_signup_y + self.label_signup.height()

        pe = QtGui.QPalette()  
        pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.red)  
        self.label_signup.setAutoFillBackground(True)  
        # pe.setColor(QtGui.QPalette.Window, QtCore.Qt.blue)  
        # pe.setColor(QPalette.Background,Qt.blue)  
        self.label_signup.setPalette(pe)
        pass

    def action_Btn(self):
        self.pushButton_Cancel.clicked.connect(self.close)
        self.pushButton_Login.clicked.connect(self.Click_Login)
        pass

    def Click_Login(self):
        password = unicode(self.lineEdit_Password.text().toUtf8(), 'utf-8', 'ignore')
        self.user = unicode(self.lineEdit_User.text().toUtf8(), 'utf-8', 'ignore')

        if(password == "" or self.user == ""):
            QtGui.QMessageBox.warning(self, "error", "it's empty!",
                                    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            return
        password_md5 = md5enc(password)
        self.key = md5enc(password + self.user)
        if self.sqlit is None:
            self.sqlit = Sqlite3Work.Sqlite3Worker('ajKvpro.db')
        if (self.Check_Allow(self.sqlit) is False):
            button = QtGui.QMessageBox.question(self, "Create", "Would you create a new user!!!",
                                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            if button == QtGui.QMessageBox.Ok:
                newUser = New_User(self)
                newUser.exec_()
            elif button == QtGui.QMessageBox.Cancel:
                return
            return
        sql_ret = self.sqlit.execute("SELECT * FROM user where username = ? and password = ?;", (self.user, password_md5))        # search the user is exit
        if len(sql_ret) > 0:
            self.Login_stuta = True
            self.close()
        else:
            QtGui.QMessageBox.warning(self, "error", "user or password error!",
                                    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            self.lineEdit_Password.clear()
        pass

    def closeEvent(self, e):
        if self.sqlit:
            self.sqlit.sqlClose()

    def Ret_Login(self):
        return self.Login_stuta, self.user, self.key
        pass

    def mousePressEvent(self, e):
        if e.button() == 0x00000001:
            mouse_x = e.x() 
            mouse_y = e.y()
            if (mouse_x > self.lable_signup_x and mouse_x < self.label_signup_w) and (mouse_y > self.lable_signup_y and mouse_y < self.label_signup_h):
                newUser = New_User(self)
                newUser.exec_()

    def Check_Allow(self, sql):
        ret = sql.execute("select name from sqlite_master where type = 'table' order by name;")
        for table in ret:
            if table[0] == 'user':
                return True
        return False
        pass

# new table class
class NewTable_ajK(QtGui.QDialog, NewTableUi.Ui_Form_Table):
    def __init__(self, parent = None):
        super(NewTable_ajK, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.action_btn()

    def initUi(self):
        self.user = None
        self.isAdd = False
        self.addTable = None
        pass

    def action_btn(self):
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_enSure.clicked.connect(self.Click_Ensure)
        pass

    def Click_Ensure(self):
        table = unicode(self.lineEdit_table.text().toUtf8(), 'utf-8', 'ignore')
        table_type = unicode(self.lineEdit_type.text().toUtf8(), 'utf-8', 'ignore')
        userbase = self.user + '_tables'
        tablename = self.user + '_' + table
        self.sql.execute("insert into " + userbase + " (tablename, type) values (?, ?);", (tablename, table_type))
        self.sql.execute('''CREATE TABLE IF NOT EXISTS ''' + tablename + '''( 
                            username char(50),
                            password text,
                            web char(50),
                            primary key (username, web)
                            );''')
        QtGui.QMessageBox.information(self, "table", "new table success!")
        self.close()
        self.isAdd = True
        self.addTable = tablename[len(self.user) + 1:]
        pass
    
    def setDatabase(self, sql, user):
        self.sql = sql
        self.user = user
        pass

    def retnNewTable(self):
        return self.isAdd, self.addTable

class NewRecord_ajK(QtGui.QDialog, NewRecordUi.Ui_Form_Record):
    def __init__(self, parent = None):
        super(NewRecord_ajK, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.action_btn()
    
    def initUi(self):
        self.sql = None
        self.table = None
        self.iv = None
        self.isCreate = False
        self.username = None
        self.password = None
        self.web = None
        pass
    
    def action_btn(self):
        self.pushButton_enSure.clicked.connect(self.Click_Ensure)
        self.pushButton_cancel.clicked.connect(self.close)
        pass
        
    def Click_Ensure(self):
        table = self.table
        key = self.Key
        iv = self.iv
        username = unicode(self.lineEdit_user.text().toUtf8(), 'utf-8', 'ignore')
        password = unicode(self.lineEdit_password.text().toUtf8(), 'utf-8', 'ignore')
        web = unicode(self.lineEdit_userWeb.text().toUtf8(), 'utf-8', 'ignore')
        if (username == "" or password == ""):
            return
        ecs_password = Aes_encrypt(password, key, iv)
        # print ecs_password
        self.sql.execute("insert into " + table + " (username, password, web) values (?, ?, ?);", (username, ecs_password, web))
        QtGui.QMessageBox.information(self, "Record", "add new record success!")
        self.isCreate = True
        self.username = username
        self.password = password
        self.web = web
        self.close()
        pass

    def setDatabase(self, sql, table):
        self.sql = sql
        self.table = table
        pass

    def setKey_iv(self, Key, user):
        self.Key = Key
        self.iv = iv_create(user + self.table)
        pass

    def retNewRecord_create(self):
        return self.isCreate, self.username, self.password, self.web
        pass

# change password ui
class Change_Password_ajK(QtGui.QDialog, AlterPasswordUi.Ui_Form_Password):
    def __init__(self, parent = None):
        super(Change_Password_ajK, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.action_btn()

    def initUi(self):
        self.user = None
        self.key = None
        self.isAlter = False
        self.lineEdit_oldPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_newPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_confirmPassword.setEchoMode(QtGui.QLineEdit.Password)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\\img\\password.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        pass

    def action_btn(self):
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_enSure.clicked.connect(self.Click_Change)
        pass

    def Click_Change(self):
        qtOld_password = self.lineEdit_oldPassword.text()
        qtNew_password = self.lineEdit_newPassword.text()
        qtConfirm_password = self.lineEdit_confirmPassword.text()
        old_password = unicode(qtOld_password.toUtf8(), 'utf-8', 'ignore')
        new_password = unicode(qtNew_password.toUtf8(), 'utf-8', 'ignore')
        confirm_password = unicode(qtConfirm_password.toUtf8(), 'utf-8', 'ignore')
        old_password_md5 = md5enc(old_password)
        sql = Sqlite3Work.Sqlite3Worker("ajKvpro.db")
        isMatch = re.match(r'^(?![0-9]+$)(?![a-zA-Z]+$)[\w\-]{8,16}$', new_password)
        search = sql.execute("SELECT * FROM user where username = ? and password = ?;", (self.user, old_password_md5))
        if search is None:
            QtGui.QMessageBox.warning(self, "error", "password is error!",
                                    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            sql.sqlClose()
            self.lineEdit_oldPassword.clear()
            self.lineEdit_newPassword.clear()
            self.lineEdit_confirmPassword.clear()
            return
        elif isMatch is None:
            QtGui.QMessageBox.warning(self, "warning", "The password must be a numeric letter from 8 to 16 digits or a combination of special characters",
                                    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            sql.sqlClose()
            self.lineEdit_oldPassword.clear()
            self.lineEdit_newPassword.clear()
            self.lineEdit_confirmPassword.clear()
            return
        elif new_password != confirm_password or new_password == "":
            QtGui.QMessageBox.warning(self, "error", "password not allow empty or two password not same!",
                                    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
            sql.sqlClose()
            self.lineEdit_oldPassword.clear()
            self.lineEdit_newPassword.clear()
            self.lineEdit_confirmPassword.clear()
            return
        else:
            new_password_md5 = md5enc(new_password)
            sql.execute("UPDATE user set password = ? where username = ?;", (new_password_md5, self.user))
            sql.sqlClose()
            self.key = md5enc(new_password + self.user)
            self.isAlter = True
            self.close()
        pass

    def setUser(self, user):
        self.user = user
        pass

    def ret_changePassword(self):
        return self.isAlter, self.key
        pass

# create password
class Password_Creator_ajK(QtGui.QDialog, PasswordCreatorUi.Ui_Form_PasswordCreate):
    def __init__(self, parent = None):
        super(Password_Creator_ajK, self).__init__(parent)
        self.setupUi(self)
        self.ditgit = '0123456789'
        self.leter = 'abcdefghijkmnpqrstuvwxyzABCDEFGHIJKMNPQRSTUVWXYZ'
        self.spcler = '~@#$%^&*()_+'
        self.initUi()

    def initUi(self):
        self.label_sign.setPixmap(QtGui.QPixmap("..\\img\\generator.ico"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\\img\\password.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.spinBox.setValue(8)
        self.pushButton_create.clicked.connect(self.Create_btn)
        pass

    def Create_btn(self):
        if self.checkBox_digits.isChecked() or self.checkBox_letter.isChecked() or self.checkBox_specialChar.isChecked():    
            num = self.spinBox.value()
            text = self.GetRandomPwd(num)
            self.lineEdit_password.setText(text)
        pass

    def GetRandomNum(self, p):
        pwdStrPool = ""
        if self.checkBox_digits.isChecked():
            pwdStrPool += self.ditgit

        if self.checkBox_letter.isChecked():
            pwdStrPool += self.leter

        if self.checkBox_specialChar.isChecked():
            pwdStrPool += self.spcler

        pwdStrPoolSize = len(pwdStrPool)
        randomNum = random.randint(0, pwdStrPoolSize - 1)
        return pwdStrPool[randomNum]

    def GetRandomPwd(self, pwdLen):
        ranPwdLen = random.randint(pwdLen, pwdLen) 
        RandomPwd = ''.join(map(self.GetRandomNum, xrange(ranPwdLen)))
        return RandomPwd

class Search_ajK(QtGui.QDialog, SearchUi.Ui_Form_Search):
    def __init__(self, parent = None):
        super(Search_ajK, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
    
    def initUi(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\\img\\password.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.comboBox_table.addItems(['username', 'password', 'web', u'全部'])
        self.pushButton_search.clicked.connect(self.Search_Record)
        self.comboBox_table.currentIndexChanged.connect(self.seletTableBox)
        self.comboBox_database.currentIndexChanged.connect(self.seletDataBox)
        pass

    def Search_Record(self):
        searchTxt = unicode(self.lineEdit_search.text().toUtf8(), 'utf-8', 'ignore')
        if (searchTxt != ""):
            typeTxt = unicode(self.comboBox_table.currentText().toUtf8(), 'utf-8', 'ignore')
            tableTxt = unicode(self.comboBox_database.currentText().toUtf8(), 'utf-8', 'ignore')        
            self.emit(QtCore.SIGNAL("clickSearch(QString, QString, QString)"), tableTxt, typeTxt, searchTxt)
        pass

    def setCommbox(self, tableList, iLen):
        for item in tableList:
            self.comboBox_database.addItem(item[iLen: ])
        pass
    
    def enterEvent(self, event):
        self.emit(QtCore.SIGNAL("clickSearchUi(bool)"), True)

    def leaveEvent(self, event):
        self.emit(QtCore.SIGNAL("clickSearchUi(bool)"), False)

    def closeEvent(self, event):
        self.emit(QtCore.SIGNAL("setSearchNone()"), )
        pass

    def seletTableBox(self, strSel):
        self.emit(QtCore.SIGNAL("clickSearchUi(bool)"), True)
        self.emit(QtCore.SIGNAL("setSearchZero()"), )
        pass

    def seletDataBox(self, strSel):
        self.emit(QtCore.SIGNAL("clickSearchUi(bool)"), True)
        self.emit(QtCore.SIGNAL("setSearchZero()"), )
        pass

# Direction
class Direction_ajK(QtGui.QDialog, DirectUi.Ui_Form_Direct):
    def __init__(self, parent = None):
        super(Direction_ajK, self).__init__(parent)
        self.setupUi(self)

# About
class About_ajK(QtGui.QDialog, AboutUi.Ui_Form_About):
    def __init__(self, parent = None):
        super(About_ajK, self).__init__(parent)
        self.setupUi(self)        

# main enter
def main():
    app = QtGui.QApplication(sys.argv)  
    w = ajKvpro()    # 生成一个类w
    w.show()        # 显示窗口w
    app.installEventFilter(w)
    app.exec_()

if __name__ == '__main__':
    main() 