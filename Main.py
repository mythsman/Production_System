import sys
from  PyQt5 import QtWidgets
from MainWidget import Ui_MainWidget


def chooseFile(self):
    fileDlg= QtWidgets.QFileDialog()
    fileName,_=fileDlg.getOpenFileName(None,'','.','*.dat')
    print(fileName)
    pass

def calculate(self):
    print('32132')
    pass




app = QtWidgets.QApplication(sys.argv)
MainWidget = QtWidgets.QWidget()

MainWidget.slotChooseFile=chooseFile
MainWidget.slotCalc=calculate

ui = Ui_MainWidget()
ui.setupUi(MainWidget)

MainWidget.show()
sys.exit(app.exec_())