import sys
from  PyQt5 import QtWidgets
from MainWidget import Ui_MainWidget


class Rule:
    def __init__(self, cond, res):
        self.cond = cond
        self.res = res


class Main(QtWidgets.QWidget, Ui_MainWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.show()

    def slotAdd(self):
        item = self.listWidget.currentItem()
        if item != None:
            if item.text() not in self.dataset:
                self.dataset.add(item.text())
                self.listWidget_2.addItem(item.text())

    def slotRm(self):
        row = self.listWidget_2.currentRow()
        if row != -1:
            item = self.listWidget_2.takeItem(row)
            self.dataset.remove(item.text())

    def slotChooseFile(self):
        fileDlg = QtWidgets.QFileDialog()
        fileName, _ = fileDlg.getOpenFileName(None, '', '.', '*.dat')
        self.lineEdit.setText(fileName)
        file = open(fileName, 'r')

        self.conditions = set()  # All conditions
        self.results = set()  # All results
        self.dataset = set()  # Input dataset
        self.rules = []  # All rules

        self.results = set(file.readline()[:-1].split(','))
        for line in file:
            if len(line) > 1:
                condition, result = line[:-1].split(':')
                splitedCond = condition.split(',')
                currSet = set()
                for item in splitedCond:
                    currSet.add(item)
                    self.conditions.update(currSet)
                self.rules.append(Rule(currSet, result))

        self.listWidget.addItems(self.conditions)
        self.listWidget_3.addItems(self.results)

    def slotCalc(self):
        self.listWidget_4.clear()
        self.listWidget_5.clear()
        currentDB = self.dataset.copy()
        changed = True
        while changed:
            changed = False
            for rule in self.rules:
                if rule.res not in currentDB and rule.cond.issubset(currentDB):
                    currentDB.add(rule.res)
                    changed = True
        res = self.results & currentDB
        if res == set():
            self.listWidget_4.addItem("None")
        else:
            self.listWidget_4.addItems(res)
        self.listWidget_5.addItems(currentDB)


app = QtWidgets.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())
