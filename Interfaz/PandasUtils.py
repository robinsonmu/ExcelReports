import pandas as pd
import concurrent.futures
import time
from PyQt5.QtCore import QThread, pyqtSignal


class PandasDataLoader:
    """
    A class that acts as a container for the dataframe and manages all the operations
    with the data
    """
    __instance = None
    @staticmethod
    def getInstance():
        if PandasDataLoader.__instance is None:
            PandasDataLoader()
        return PandasDataLoader.__instance

    def __init__(self):
        if PandasDataLoader.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.dfsList = []
            self.allData = None
            self.processing = False
            self.threadProcessor = ThreadingUtils()
            self.uniqueColumnValues = dict()
            PandasDataLoader.__instance = self

    def setUniqueColumnValues(self, df, column):
        self.uniqueColumnValues[column] = df[column].unique().tolist()

    def getCantidadDatos(self, df, columna, filtros=[]):
        groupedData = df.groupby(columna)
        dfs = [groupedData.get_group(gn) for gn in filtros]
        return pd.concat(dfs).shape[0]

    def getUniqueColumnValues(self, column):
        """
        Returns a list of all the diferent values for a column
        """
        return self.uniqueColumnValues[column]

    def loadDataframes(self, pathList=[], callback=None):
        def loadDataWrapper():
            print("Empieza carga de datos desde thread")
            self.processing = True
            """
            Reads each excel file and saves all the sheets into a list with the specified columns
            """
            COLS = ["RAT", "OPERATOR", "CHANNEL", "IMEI", "IMSI", "TMSI",
                    "MS POWER", "TA", "LAST LAC", "NAME", "HITS", "DATE-TIME"]
            for filePath in pathList:
                temd_dfs = [pd.read_excel(f"{filePath}", sheet_name=0, usecols=COLS),  # 2G
                            pd.read_excel(
                                f"{filePath}", sheet_name=1, usecols=COLS),  # 3G
                            pd.read_excel(f"{filePath}", sheet_name=2, usecols=COLS)]  # 4G
                self.dfsList.append(temd_dfs)
            # Puts all the general and raw data into a df
            self.allData = pd.concat(
                [df for dflist in self.dfsList for df in dflist])
            self.processing = False
        self.threadProcessor.setWorker(loadDataWrapper)
        self.threadProcessor.start(QThread.HighestPriority)
        self.threadProcessor.finished.connect(callback)
        # ThreadingUtils.doInThread(loadDataWrapper, callback)


class ThreadingUtils_:

    @staticmethod
    def doInThread(worker=None, callback=None):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(worker)
            future.add_done_callback(callback)
            return future


class ThreadingUtils(QThread):
    updateSignal = pyqtSignal()

    def __init__(self, worker=None):
        super(QThread, self).__init__()
        self.worker = worker

    def setWorker(self, worker):
        self.worker = worker

    def run(self):
        self.worker()
        self.updateSignal.emit()


# Testing
def worker():
    time.sleep(5)
    return "Worker done"


def callBack(future):
    print(f"Se ejecuta callback {future} {future.result()}")


if(__name__ == '__main__'):
    ThreadingUtils.doInThread(worker, callBack)
