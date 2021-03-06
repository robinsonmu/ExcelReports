from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QAbstractItemView,
                             QAction, QTableWidgetItem, QTableWidget, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import pandas as pd
from PandasUtils import PandasDataLoader
import UiUtils
from VentanaFiltros import VentanaFiltros
from VentanaAnalisisHorario import VentanaAnalisisHorario

from UIPyfiles.VistaGeneralDatos import Ui_vistaGeneralDatos
from LoadingOverlay import Overlay
from UI.Recursos import images_rc


class VistaGeneralDatos(QMainWindow, Ui_vistaGeneralDatos):
    def __init__(self, parent, pandasUtilsInstance):
        super(QMainWindow, self).__init__(parent)
        Ui_vistaGeneralDatos.__init__(self)
        self.setupUi(self)
        # State fields
        # print(f"pandas instance {pandasUtilsInstance}")
        self.pandasUtils = pandasUtilsInstance
        self.ratsSeleccionados = dict()
        self.operadoresSeleccionados = dict()
        self.viendoIncidentales = False
        # UI
        # loadUi('UI/VistaGeneralDatos.ui', self)
        self.ventanaFiltroDatos = VentanaFiltros(parent=self, pandasUtilsInstance=self.pandasUtils)
        self.ventanaAnalisisHorario = VentanaAnalisisHorario(self, self.pandasUtils)
        self.overlay = Overlay(self)

    def setupUiCustom(self):
        self.overlay.hide()
        self.pandasUtils.setTempDf(self.pandasUtils.getAllData())
        # print(f"Setup UI vista general y temp df {self.pandasUtils.tempDf.shape}")
        self.pushButtonGuardarDatos4G.setEnabled(False)
        # Setting the menus for the RAT and OPERATOR buttons
        self.pandasUtils.setUniqueColumnValues(self.pandasUtils.tempDf, 'RAT')
        self.ratsSeleccionados = {rat: True for rat in self.pandasUtils.getUniqueColumnValues('RAT')}
        self.menuRats = UiUtils.createMenu(self.ratsSeleccionados.keys())

        self.pandasUtils.setUniqueColumnValues(self.pandasUtils.tempDf, 'OPERATOR')
        # TODO: CHANGE TO STATIC OPERATORS
        self.operadoresSeleccionados = {op: True for op in self.pandasUtils.getUniqueColumnValues('OPERATOR')}
        print(f"Colum names for operator -> {self.operadoresSeleccionados}")

        self.menuOperadores = UiUtils.createMenu(self.operadoresSeleccionados.keys())

        self.pushButtonOperadores.setMenu(self.menuOperadores)
        self.pushButtonRATS.setMenu(self.menuRats)

        # Establece contadores inicialmente
        self.fnMuestraCantidadEnRats()
        self.fnMuestraCantidadEnOperadores()
        self.fnMuestraCantidadesImeisImsis()
        # Connects signals to sloots and callbacks
        self.menuOperadores.triggered.connect(self.fnProcesaSeleccionOperadores)
        self.menuRats.triggered.connect(self.fnProcesaSeleccionRats)
        # Busqueda IMEI
        self.pushButtonBuscarDato.clicked.connect(self.fnProcesaFiltroImei)
        # Boton exportar
        self.pushButtonGuardarDatos.clicked.connect(self.fnProcesaGuardarDatos)
        # Boton Analisis horario
        self.pushButtonAnalisisHorario.clicked.connect(self.fnVentanaAnalisisHorario)
        # Btn Ver datos indidentales
        self.pushButtonVerDatosIncidentales.clicked.connect(self.fnFiltroDatosIncidentales)
        # Btn Ver tabla original
        self.pushButtonVerTablaOriginal.clicked.connect(self.fnMuestraTablaOriginal)
        # Btn volver a principal de inicio
        self.actionIr_A_Principal.triggered.connect(self.fnMuestraVentanaPrincipal)
        # Btn ventana filtro  de datos
        self.pushButtonFiltrarDatos.clicked.connect(self.fnVentanaFiltroDatos)
        # Btn guardar datos 4g sin sus imeis
        self.pushButtonGuardarDatos4G.clicked.connect(self.fnGuardar4gSinImeis)
        # Btn ver IMSIS VS IMEIS
        self.pushButtonVerImsisVSImeis.clicked.connect(self.fnVerImsisImeis)
        # Btn guardar imsis vs imeis
        self.pushButtonGuardarImsisVSImei.clicked.connect(self.fnGuardarImsisImeis)
        # Fill the table with a df where all the EMAIS are
        self.tableWidgetDatosExcel.setWordWrap(False)
        self.tableWidgetDatosExcel.setTextElideMode(Qt.ElideRight)
        self.tableWidgetDatosExcel.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableWidgetDatosExcel.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.pushButtonAsignarIMEIS.clicked.connect(self.fnProcesaAsignarImeis)
        # self.fillTableWidget(self.pandasUtils.tempDf)

    def fnMuestraCantidadesImeisImsis(self):
        self.labelIMEIDatos.setText(str(self.pandasUtils.getRowCountForColumn(self.pandasUtils.tempDf, "IMEI")))
        self.labelIMSIDatos.setText(str(self.pandasUtils.getRowCountForColumn(self.pandasUtils.tempDf, "IMSI")))

    def fnVerImsisImeis(self):
        self.pandasUtils.setTempDf(self.pandasUtils.getGroupedByIMSI(self.pandasUtils.getAllData()))
        self.fillTableWidget(self.pandasUtils.tempDf)

    def fnGuardarImsisImeis(self):
        # print("Fn procesa guardar datos imsis vs imeis")
        def guardaImsisImeis(msg):
            self.pandasUtils.saveToExcelFile(
                groupedIMSIS, filePath, False, self.saveProcessFinished)
            self.overlay.killAndHide()

        groupedIMSIS = self.pandasUtils.getGroupedByIMSI(self.pandasUtils.getAllData())
        filePath = self.saveFileDialog()
        if(filePath):
            self.fnAplicaFiltrosDfOk(guardaImsisImeis)

        # print("Fn generacion del reporte")

    def fnProcesaAsignarImeis(self):
        # print("Empieza proceso de asignacion de IMEIS")
        self.overlay.show()
        self.pandasUtils.asignarIMEIS(self.pandasUtils.getAllData(),
                                      self.pandasUtils.getDfImeisFaltantes(), self.fnAsignacionTerminada)

    def fnAsignacionTerminada(self, msg):
        # Dividir de nuevo los df en 2g 3g y 4g y asignarlos de nuevo
        self.fnMuestraCantidadEnOperadores()
        self.fnMuestraCantidadEnRats()
        self.fnMuestraCantidadesImeisImsis()
        self.fillTableWidget(self.pandasUtils.tempDf)
        self.pushButtonGuardarDatos4G.setEnabled(True)
        self.overlay.killAndHide()
        UiUtils.showInfoMessage(parent=self, title="Estado de la asignacion",
                                description=msg)

        # print(f"Cantidad de imeis despues {cantidadDespuesCon}")

    def pandasProcessingFinished(self):
        UiUtils.showInfoMessage(parent=self, title="Estado de la operacion",
                                description=f"Se realizo la operación correctamente.")

    def fnGuardar4gSinImeis(self):
        # print(f"Funcion guardar datos de 4g sin sus imeis")
        # print("Fn procesa guardar datos 4g sin imei")
        def guarda4GSin(msg):
            self.pandasUtils.saveToExcelFile(self.pandasUtils.sinImei, filePath, False, self.saveProcessFinished)
            self.overlay.killAndHide()
        filePath = self.saveFileDialog()
        if(filePath):
            self.fnAplicaFiltrosDfOk(guarda4GSin)

    def reseteoFiltros(self):
        self.operadoresSeleccionados = {op: True for op in self.operadoresSeleccionados.keys()}
        self.ratsSeleccionados = {rat: True for rat in self.ratsSeleccionados.keys()}
        self.textEditBuscarDatos.setText("")

    def fnMuestraTablaOriginal(self):
        print(f"Muestra tabla completa ")
        self.viendoIncidentales = False
        self.fnMuestraCantidadEnOperadores()
        self.fnMuestraCantidadEnRats()
        self.reseteoFiltros()
        self.fillTableWidget(
            self.pandasUtils.getAllData()
        )

    def fnMuestraVentanaPrincipal(self):
        self.parent().show()
        self.hide()

    def fnVentanaFiltroDatos(self):
        # print(f"Fn mostrar ventana filtro de datos")
        self.hide()
        self.ventanaFiltroDatos.setupUiCustom()
        self.ventanaFiltroDatos.show()

    # def fnAsignaNombresPorEmais(self):
        print(f"Fn asgina nombre a emai")
        # self.pandasUtils.tempDf = self.pandasUtils.setUniqueNameIdColumn(
        # self.pandasUtils.getDfCompletoEmaisOk(self.pandasUtils.tempDf)
        # )
        # self.fillTableWidget(
        # self.pandasUtils.tempDf
        # )

    def fnFiltroDatosIncidentales(self):
        # self.pushButtonVerDatosIncidentales.setStyleSheet('QPushButton {color: green;}')
        def incidentalesProcess(msg):
            self.fnMuestraCantidadEnOperadores()
            self.fnMuestraCantidadEnRats()
            self.fillTableWidget(self.pandasUtils.tempDf)
            self.overlay.killAndHide()

        self.reseteoFiltros()
        self.viendoIncidentales = True
        self.fnAplicaFiltrosDfOk(incidentalesProcess)

    def fnVentanaAnalisisHorario(self):
        # print(f"Fn analisis horario")
        def muestraAnalisisHorario(msg):
            self.ventanaAnalisisHorario.data = data = self.pandasUtils.tempDf
            self.ventanaAnalisisHorario.setupUiCustom()
            self.ventanaAnalisisHorario.show()
            self.overlay.killAndHide()

        self.hide()
        self.fnAplicaFiltrosDfOk(muestraAnalisisHorario)

    def fnProcesaGuardarDatos(self):
        # print("Fn procesa guardar datos")
        def guardarDatos(msg):
            self.pandasUtils.saveToExcelFile(
                self.pandasUtils.tempDf, filePath, False, self.saveProcessFinished)
            self.overlay.killAndHide()

        filePath = self.saveFileDialog()
        if(filePath):
            self.fnAplicaFiltrosDfOk(guardarDatos)

    def saveProcessFinished(self):
        UiUtils.showInfoMessage(parent=self, title="Guardado de archivos",
                                description=f"Se guardo el archivo correctamente.")

    def saveFileDialog(self):
        """
        Opens a save file dialog and returns the path to the file
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "", "Excel Files (*.xlsx)", options=options)
        return fileName

    def fnAplicaFiltrosDfOk(self, callback):
        """
        Calls filltable according to all the filters that the user has set and returns the df
        """
        # df = self.pandasUtils.tempDf if self.viendoIncidentales is False else self.pandasUtils.dfIncidentales
        listaRats = [rat for rat, v in self.ratsSeleccionados.items() if v is True]
        listaOps = [op for op, v in self.operadoresSeleccionados.items() if v is True]

        self.overlay.show()
        self.pandasUtils.fnAplicaFiltrosGeneral(listaRats, listaOps, self.viendoIncidentales, callback)

    def fnAplicacionFiltrosFinished(self, msg):
        self.overlay.killAndHide()
        print(f"Se termino la aplicación de filtros msg->{msg}\n")

    def fnProcesaFiltroImei(self):
        def filtroImeiProcess(msg):
            df = self.pandasUtils.filterDfByEmai(self.pandasUtils.tempDf, imei)
            if(df.shape[0] > 0):
                print("Shape del filtro ", df.shape, "dato buscar", imei)
                self.fillTableWidget(df)
                self.fnMuestraCantidadEnOperadores()
                self.fnMuestraCantidadEnRats()
            else:
                UiUtils.showInfoMessage(self,
                                        title=f"Busqueda de imei: {imei} ",
                                        description=f"No se encontro el imei {imei} .")
            self.overlay.killAndHide()

        imei = self.textEditBuscarDatos.toPlainText()
        if(len(imei) > 0 and self.pandasUtils.isFloat(imei)):
            self.fnAplicaFiltrosDfOk(filtroImeiProcess)

    def fillTableWidget(self, df: pd.DataFrame = None):
        # Limpiar contenidos de tabla
        headerList = tuple(df.columns.values)
        self.tableWidgetDatosExcel.clearContents()
        self.tableWidgetDatosExcel.setColumnCount(len(headerList))
        self.tableWidgetDatosExcel.setHorizontalHeaderLabels(headerList)
        self.tableWidgetDatosExcel.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDatosExcel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        rowCount = 0
        for row in df.itertuples():
            # Sets the number of rows in this table's model to rows. If this is less than rowCount(),
            # the data in the unwanted rows is discarded.
            self.tableWidgetDatosExcel.setRowCount(rowCount+1)
            for i, columnName in enumerate(headerList):
                # val = QTableWidgetItem(row._asdict()[str(columnName)])
                val = QTableWidgetItem(str(row._asdict()[columnName]))
                self.tableWidgetDatosExcel.setItem(rowCount, i, val)
            rowCount += 1

    def fnProcesaSeleccionRats(self, action: QAction):
        def llenarTabla(msg):
            self.fillTableWidget(self.pandasUtils.tempDf)
            self.overlay.killAndHide()
        self.ratsSeleccionados[str(action.data())] = action.isChecked()
        print(f"Fn procesa seleccion Rat {action} {self.ratsSeleccionados}")
        if(sum([1 for rat, v in self.ratsSeleccionados.items() if v is True]) == 0):
            action.setChecked(True)
            self.ratsSeleccionados[str(action.data())] = action.isChecked()
        self.fnMuestraCantidadEnRats()
        self.fnAplicaFiltrosDfOk(llenarTabla)

    def fnMuestraCantidadEnRats(self, msg=None):
        """
        This function is called when there is a change in the selected rats dictionary
        """
        def muestraCantidadRats(msg):
            cantidad = self.pandasUtils.getCantidadDatos(self.pandasUtils.tempDf, 'RAT', listaRats)
            self.labelRATContador.setText(str(cantidad))
            self.overlay.killAndHide()

        listaRats = [rat for rat, v in self.ratsSeleccionados.items()
                     if v is True]
        if len(listaRats) > 0:
            self.fnAplicaFiltrosDfOk(muestraCantidadRats)

    def fnProcesaSeleccionOperadores(self, action: QAction):
        def llenarTabla(msg):
            self.fillTableWidget(self.pandasUtils.tempDf)
            self.overlay.killAndHide()
        self.operadoresSeleccionados[str(action.data())] = action.isChecked()
        print(f"Fn procesa seleccion opeadores {action} {self.operadoresSeleccionados}")
        if(sum([1 for rat, v in self.operadoresSeleccionados.items() if v is True]) == 0):
            action.setChecked(True)
            self.operadoresSeleccionados[str(action.data())] = action.isChecked()

        self.fnMuestraCantidadEnOperadores()
        self.fnAplicaFiltrosDfOk(llenarTabla)

    def fnMuestraCantidadEnOperadores(self, msg=None):
        """
        This function is called when there is a change in the selected rats dictionary
        """
        def muestraCantidadOperadores(msg):
            cantidad = self.pandasUtils.getCantidadDatos(self.pandasUtils.tempDf, 'OPERATOR', listaOps)
            self.labelOperadorDatos.setText(str(cantidad))
            self.overlay.killAndHide()
        listaOps = [op for op, v in self.operadoresSeleccionados.items() if v]
        if len(listaOps) > 0:
            self.fnAplicaFiltrosDfOk(muestraCantidadOperadores)

    def resizeEvent(self, event):
        self.overlay.resize(event.size())
        event.accept()
