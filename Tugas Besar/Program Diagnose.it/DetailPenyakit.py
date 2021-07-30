# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetailPenyakit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_DetailPenyakit(object):
    def __init__(self):
        # inisialisasi database yang dipakai
        con = pymysql.connect(db='db_diagnosispenyakit', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        self.cur = con.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.namaPenyakit_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.namaPenyakit_Label.setFont(font)
        self.namaPenyakit_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.namaPenyakit_Label.setWordWrap(True)
        self.namaPenyakit_Label.setObjectName("namaPenyakit_Label")
        self.verticalLayout.addWidget(self.namaPenyakit_Label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_GejalaPenyakit = QtWidgets.QWidget()
        self.tab_GejalaPenyakit.setObjectName("tab_GejalaPenyakit")
        self.gejalaPenyakit_listWidget = QtWidgets.QListWidget(self.tab_GejalaPenyakit)
        self.gejalaPenyakit_listWidget.setGeometry(QtCore.QRect(10, 10, 881, 491))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.gejalaPenyakit_listWidget.setFont(font)
        self.gejalaPenyakit_listWidget.setObjectName("gejalaPenyakit_listWidget")
        self.tabWidget.addTab(self.tab_GejalaPenyakit, "")
        self.tab_Obat = QtWidgets.QWidget()
        self.tab_Obat.setObjectName("tab_Obat")
        self.Obat_listWidget = QtWidgets.QListWidget(self.tab_Obat)
        self.Obat_listWidget.setGeometry(QtCore.QRect(10, 10, 881, 491))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Obat_listWidget.setFont(font)
        self.Obat_listWidget.setObjectName("Obat_listWidget")
        self.tabWidget.addTab(self.tab_Obat, "")
        self.tab_MetodePenyembuhan = QtWidgets.QWidget()
        self.tab_MetodePenyembuhan.setObjectName("tab_MetodePenyembuhan")
        self.metodePenyembuhan_label = QtWidgets.QLabel(self.tab_MetodePenyembuhan)
        self.metodePenyembuhan_label.setGeometry(QtCore.QRect(20, 20, 861, 471))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.metodePenyembuhan_label.setFont(font)
        self.metodePenyembuhan_label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.metodePenyembuhan_label.setWordWrap(True)
        self.metodePenyembuhan_label.setObjectName("metodePenyembuhan_label")
        self.tabWidget.addTab(self.tab_MetodePenyembuhan, "")
        self.tab_Keterangan = QtWidgets.QWidget()
        self.tab_Keterangan.setObjectName("tab_Keterangan")
        self.keterangan_label = QtWidgets.QLabel(self.tab_Keterangan)
        self.keterangan_label.setGeometry(QtCore.QRect(20, 20, 861, 471))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.keterangan_label.setFont(font)
        self.keterangan_label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.keterangan_label.setWordWrap(True)
        self.keterangan_label.setObjectName("keterangan_label")
        self.tabWidget.addTab(self.tab_Keterangan, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        ########################################################################################################
        # Detail Informasi Nama Penyakit
        ########################################################################################################
        sql = "SELECT distinct histori_cekDetailPenyakit from historiuser"
        self.cur.execute(sql)

        namaPenyakit = []
        for t in self.cur.fetchall():
            namaPenyakit += t

        ########################################################################################################
        # Detail Informasi Gejala
        ########################################################################################################
        sql = "SELECT distinct gejala from detailpenyakit where namaPenyakit = '%s'" % str("".join(namaPenyakit))
        self.cur.execute(sql)

        gejala = []
        for y in self.cur.fetchall():
            gejala += y

        for z in gejala: # Menambah daftar gejala penyakit pada list widget
            if len(str(z)) != 0:
                self.gejalaPenyakit_listWidget.addItem("".join(z))

        ########################################################################################################
        # Detail Informasi Obat
        ########################################################################################################
        sql = "SELECT distinct obat from detailpenyakit where namaPenyakit = '%s'" % str("".join(namaPenyakit))
        self.cur.execute(sql)

        obat = []
        for y in self.cur.fetchall():
            obat += y

        for z in obat: # Menambah daftar obat pada list widget
            if len(str(z)) != 0:
                self.Obat_listWidget.addItem("".join(z))

        ########################################################################################################
        # Detail Informasi Metode Penyembuhan
        ########################################################################################################
        sql = "SELECT distinct metodePenyembuhan from detailpenyakit where namaPenyakit = '%s'" % str("".join(namaPenyakit))
        self.cur.execute(sql)

        metodePenyembuhan = []
        for y in self.cur.fetchall():
            metodePenyembuhan += y

        ########################################################################################################
        # Detail Informasi Keterangan Penyakit
        ########################################################################################################
        sql = "SELECT distinct keterangan from detailpenyakit where namaPenyakit = '%s'" % str("".join(namaPenyakit))
        self.cur.execute(sql)

        keterangan = []
        for y in self.cur.fetchall():
            keterangan += y


        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.namaPenyakit_Label.setText(_translate("MainWindow", "".join(namaPenyakit)))
        __sortingEnabled = self.gejalaPenyakit_listWidget.isSortingEnabled()
        self.gejalaPenyakit_listWidget.setSortingEnabled(False)
        self.gejalaPenyakit_listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_GejalaPenyakit), _translate("MainWindow", "Gejala Penyakit"))
        __sortingEnabled = self.Obat_listWidget.isSortingEnabled()
        self.Obat_listWidget.setSortingEnabled(False)
        self.Obat_listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Obat), _translate("MainWindow", "Obat"))
        self.metodePenyembuhan_label.setText(_translate("MainWindow", " ".join(metodePenyembuhan)))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_MetodePenyembuhan), _translate("MainWindow", "Metode Penyembuhan"))
        self.keterangan_label.setText(_translate("MainWindow", " ".join(keterangan)))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Keterangan), _translate("MainWindow", "Keterangan"))

        for hapus in namaPenyakit: # Hapus histori penyakit yang dilihat detailnya pada database
            sql = "DELETE FROM `historiuser` WHERE `histori_cekDetailPenyakit` = '%s';" % hapus
            self.cur.execute(sql)

        ## Clear Isi Array
        keterangan.clear()
        namaPenyakit.clear()
        obat.clear()
        metodePenyembuhan.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DetailPenyakit()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
