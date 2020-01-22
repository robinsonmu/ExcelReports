# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\VistaAnalisisDatos.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VistaAnalisisDatos(object):
    def setupUi(self, VistaAnalisisDatos):
        VistaAnalisisDatos.setObjectName("VistaAnalisisDatos")
        VistaAnalisisDatos.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VistaAnalisisDatos.sizePolicy().hasHeightForWidth())
        VistaAnalisisDatos.setSizePolicy(sizePolicy)
        VistaAnalisisDatos.setMinimumSize(QtCore.QSize(1280, 720))
        VistaAnalisisDatos.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(85, 125, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(VistaAnalisisDatos)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButtonGuardarDatosIMISISIMEI = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.pushButtonGuardarDatosIMISISIMEI.setFont(font)
        self.pushButtonGuardarDatosIMISISIMEI.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 117, 194, 200), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-añadir-libro-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGuardarDatosIMISISIMEI.setIcon(icon)
        self.pushButtonGuardarDatosIMISISIMEI.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonGuardarDatosIMISISIMEI.setObjectName("pushButtonGuardarDatosIMISISIMEI")
        self.gridLayout_5.addWidget(self.pushButtonGuardarDatosIMISISIMEI, 2, 0, 1, 1)
        self.pushButtonGraficar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.pushButtonGraficar.setFont(font)
        self.pushButtonGraficar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 117, 194, 200), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("20803.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGraficar.setIcon(icon1)
        self.pushButtonGraficar.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonGraficar.setObjectName("pushButtonGraficar")
        self.gridLayout_5.addWidget(self.pushButtonGraficar, 4, 1, 1, 1)
        self.tableWidgetVerDatosFiltrados = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetVerDatosFiltrados.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetVerDatosFiltrados.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidgetVerDatosFiltrados.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidgetVerDatosFiltrados.setObjectName("tableWidgetVerDatosFiltrados")
        self.tableWidgetVerDatosFiltrados.setColumnCount(8)
        self.tableWidgetVerDatosFiltrados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerDatosFiltrados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerDatosFiltrados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerDatosFiltrados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerDatosFiltrados.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerDatosFiltrados.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerDatosFiltrados.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerDatosFiltrados.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerDatosFiltrados.setHorizontalHeaderItem(7, item)
        self.gridLayout_5.addWidget(self.tableWidgetVerDatosFiltrados, 4, 0, 1, 1)
        self.pushButtonGuardarReporte = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.pushButtonGuardarReporte.setFont(font)
        self.pushButtonGuardarReporte.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 117, 194, 200), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.pushButtonGuardarReporte.setIcon(icon)
        self.pushButtonGuardarReporte.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonGuardarReporte.setObjectName("pushButtonGuardarReporte")
        self.gridLayout_5.addWidget(self.pushButtonGuardarReporte, 1, 0, 1, 1)
        self.pushButtonReporte = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.pushButtonReporte.setFont(font)
        self.pushButtonReporte.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 117, 194, 200), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-hand-box-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonReporte.setIcon(icon2)
        self.pushButtonReporte.setObjectName("pushButtonReporte")
        self.gridLayout_5.addWidget(self.pushButtonReporte, 1, 1, 1, 1)
        self.pushButtonIMSIS = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.pushButtonIMSIS.setFont(font)
        self.pushButtonIMSIS.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 117, 194, 200), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.pushButtonIMSIS.setIcon(icon2)
        self.pushButtonIMSIS.setObjectName("pushButtonIMSIS")
        self.gridLayout_5.addWidget(self.pushButtonIMSIS, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 3, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout.addLayout(self.gridLayout_4, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("image: url(:/Imagenes/Logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        VistaAnalisisDatos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VistaAnalisisDatos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuVolver_A_Filtros = QtWidgets.QMenu(self.menubar)
        self.menuVolver_A_Filtros.setObjectName("menuVolver_A_Filtros")
        VistaAnalisisDatos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VistaAnalisisDatos)
        self.statusbar.setObjectName("statusbar")
        VistaAnalisisDatos.setStatusBar(self.statusbar)
        self.actionVer_Filtros = QtWidgets.QAction(VistaAnalisisDatos)
        self.actionVer_Filtros.setObjectName("actionVer_Filtros")
        self.menuVolver_A_Filtros.addAction(self.actionVer_Filtros)
        self.menubar.addAction(self.menuVolver_A_Filtros.menuAction())

        self.retranslateUi(VistaAnalisisDatos)
        QtCore.QMetaObject.connectSlotsByName(VistaAnalisisDatos)

    def retranslateUi(self, VistaAnalisisDatos):
        _translate = QtCore.QCoreApplication.translate
        VistaAnalisisDatos.setWindowTitle(_translate("VistaAnalisisDatos", "MainWindow"))
        self.pushButtonGuardarDatosIMISISIMEI.setText(_translate("VistaAnalisisDatos", "Guargar Datos IMSIS-IMEI"))
        self.pushButtonGraficar.setText(_translate("VistaAnalisisDatos", "Graficar Datos"))
        item = self.tableWidgetVerDatosFiltrados.horizontalHeaderItem(0)
        item.setText(_translate("VistaAnalisisDatos", "RAT"))
        item = self.tableWidgetVerDatosFiltrados.horizontalHeaderItem(1)
        item.setText(_translate("VistaAnalisisDatos", "Operator"))
        item = self.tableWidgetVerDatosFiltrados.horizontalHeaderItem(2)
        item.setText(_translate("VistaAnalisisDatos", "IMEI"))
        item = self.tableWidgetVerDatosFiltrados.horizontalHeaderItem(3)
        item.setText(_translate("VistaAnalisisDatos", "IMSI"))
        item = self.tableWidgetVerDatosFiltrados.horizontalHeaderItem(4)
        item.setText(_translate("VistaAnalisisDatos", "TA"))
        item = self.tableWidgetVerDatosFiltrados.horizontalHeaderItem(5)
        item.setText(_translate("VistaAnalisisDatos", "MS Power"))
        item = self.tableWidgetVerDatosFiltrados.horizontalHeaderItem(6)
        item.setText(_translate("VistaAnalisisDatos", "Last Lac"))
        item = self.tableWidgetVerDatosFiltrados.horizontalHeaderItem(7)
        item.setText(_translate("VistaAnalisisDatos", "Hits"))
        self.pushButtonGuardarReporte.setText(_translate("VistaAnalisisDatos", "Generar Reporte Final"))
        self.pushButtonReporte.setText(_translate("VistaAnalisisDatos", "Ver Reporte"))
        self.pushButtonIMSIS.setText(_translate("VistaAnalisisDatos", "Ver IMSIS.IMEI"))
        self.label_2.setText(_translate("VistaAnalisisDatos", "REPORTE FINAL "))
        self.menuVolver_A_Filtros.setTitle(_translate("VistaAnalisisDatos", "Volver"))
        self.actionVer_Filtros.setText(_translate("VistaAnalisisDatos", "Ver Filtros"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VistaAnalisisDatos = QtWidgets.QMainWindow()
    ui = Ui_VistaAnalisisDatos()
    ui.setupUi(VistaAnalisisDatos)
    VistaAnalisisDatos.show()
    sys.exit(app.exec_())