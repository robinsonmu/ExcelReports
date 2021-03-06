# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\InicioSubirDatos.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from UI.Recursos import images_rc

class Ui_vistaInicioSubirDatos(object):
    def setupUi(self, vistaInicioSubirDatos):
        vistaInicioSubirDatos.setObjectName("vistaInicioSubirDatos")
        vistaInicioSubirDatos.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(vistaInicioSubirDatos.sizePolicy().hasHeightForWidth())
        vistaInicioSubirDatos.setSizePolicy(sizePolicy)
        vistaInicioSubirDatos.setMinimumSize(QtCore.QSize(1280, 720))
        vistaInicioSubirDatos.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(vistaInicioSubirDatos)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Logos/Logo.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonMostrarDatos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMostrarDatos.setMaximumSize(QtCore.QSize(16777215, 16777213))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.pushButtonMostrarDatos.setFont(font)
        self.pushButtonMostrarDatos.setStyleSheet("background-color: rgb(255, 255, 127);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/icons8-hand-box-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonMostrarDatos.setIcon(icon)
        self.pushButtonMostrarDatos.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonMostrarDatos.setObjectName("pushButtonMostrarDatos")
        self.gridLayout.addWidget(self.pushButtonMostrarDatos, 25, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(167777, 167777))
        self.label_2.setStyleSheet("image: url(:/newPrefix/Logo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 23, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 23, 5, 1, 1)
        self.listWidgetListaArchivos = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.listWidgetListaArchivos.sizePolicy().hasHeightForWidth())
        self.listWidgetListaArchivos.setSizePolicy(sizePolicy)
        self.listWidgetListaArchivos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.listWidgetListaArchivos.setAutoScrollMargin(23)
        self.listWidgetListaArchivos.setObjectName("listWidgetListaArchivos")
        self.gridLayout.addWidget(self.listWidgetListaArchivos, 23, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonAnadirArchivo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAnadirArchivo.setMaximumSize(QtCore.QSize(16777215, 48))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.pushButtonAnadirArchivo.setFont(font)
        self.pushButtonAnadirArchivo.setStyleSheet("background-color: rgb(255, 255, 127);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Iconos/icons8-añadir-libro-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAnadirArchivo.setIcon(icon1)
        self.pushButtonAnadirArchivo.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonAnadirArchivo.setObjectName("pushButtonAnadirArchivo")
        self.horizontalLayout.addWidget(self.pushButtonAnadirArchivo)
        self.pushButtonEliminar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.pushButtonEliminar.setFont(font)
        self.pushButtonEliminar.setStyleSheet("background-color: rgb(255, 255, 127);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Iconos/icons8-eliminar-400.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEliminar.setIcon(icon2)
        self.pushButtonEliminar.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonEliminar.setObjectName("pushButtonEliminar")
        self.horizontalLayout.addWidget(self.pushButtonEliminar)
        self.pushButtonCargarDatos = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.pushButtonCargarDatos.setFont(font)
        self.pushButtonCargarDatos.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Iconos/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCargarDatos.setIcon(icon3)
        self.pushButtonCargarDatos.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonCargarDatos.setObjectName("pushButtonCargarDatos")
        self.horizontalLayout.addWidget(self.pushButtonCargarDatos)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 5, 1, 1)
        vistaInicioSubirDatos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(vistaInicioSubirDatos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        vistaInicioSubirDatos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(vistaInicioSubirDatos)
        self.statusbar.setObjectName("statusbar")
        vistaInicioSubirDatos.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(vistaInicioSubirDatos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setObjectName("toolBar")
        vistaInicioSubirDatos.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbrir = QtWidgets.QAction(vistaInicioSubirDatos)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionNueva_Ventana = QtWidgets.QAction(vistaInicioSubirDatos)
        self.actionNueva_Ventana.setObjectName("actionNueva_Ventana")
        self.actionGuardar = QtWidgets.QAction(vistaInicioSubirDatos)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(vistaInicioSubirDatos)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionSalir = QtWidgets.QAction(vistaInicioSubirDatos)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionNueva_Ventana)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(vistaInicioSubirDatos)
        QtCore.QMetaObject.connectSlotsByName(vistaInicioSubirDatos)

    def retranslateUi(self, vistaInicioSubirDatos):
        _translate = QtCore.QCoreApplication.translate
        vistaInicioSubirDatos.setWindowTitle(_translate("vistaInicioSubirDatos", "MainWindow"))
        self.label_3.setText(_translate("vistaInicioSubirDatos", "LISTA DIRECTORIOS"))
        self.label_5.setText(_translate("vistaInicioSubirDatos", "<html><head/><body><p><img src=\":/Iconos/logoRaptor.png\"/></p></body></html>"))
        self.pushButtonMostrarDatos.setText(_translate("vistaInicioSubirDatos", "Ver Datos"))
        self.label.setText(_translate("vistaInicioSubirDatos", "<html><head/><body><p><img src=\":/Images/Iocom png.png\"/></p></body></html>"))
        self.pushButtonAnadirArchivo.setText(_translate("vistaInicioSubirDatos", "Añadir Archivos"))
        self.pushButtonEliminar.setWhatsThis(_translate("vistaInicioSubirDatos", "<html><head/><body><p><img src=\":/newPrefix/Iocom png.png\"/></p></body></html>"))
        self.pushButtonEliminar.setText(_translate("vistaInicioSubirDatos", "Eliminar Archivo"))
        self.pushButtonCargarDatos.setText(_translate("vistaInicioSubirDatos", "Cargar Datos"))
        self.label_7.setText(_translate("vistaInicioSubirDatos", "<html><head/><body><p><img src=\":/Iconos/Iocom.png\"/></p></body></html>"))
        self.label_6.setText(_translate("vistaInicioSubirDatos", "TextLabel"))
        self.menuArchivo.setTitle(_translate("vistaInicioSubirDatos", "Archivo"))
        self.toolBar.setWindowTitle(_translate("vistaInicioSubirDatos", "toolBar"))
        self.actionAbrir.setText(_translate("vistaInicioSubirDatos", "Abrir"))
        self.actionNueva_Ventana.setText(_translate("vistaInicioSubirDatos", "Nueva Ventana"))
        self.actionGuardar.setText(_translate("vistaInicioSubirDatos", "Guardar"))
        self.actionGuardar_Como.setText(_translate("vistaInicioSubirDatos", "Guardar Como "))
        self.actionSalir.setText(_translate("vistaInicioSubirDatos", "Salir "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vistaInicioSubirDatos = QtWidgets.QMainWindow()
    ui = Ui_vistaInicioSubirDatos()
    ui.setupUi(vistaInicioSubirDatos)
    vistaInicioSubirDatos.show()
    sys.exit(app.exec_())
