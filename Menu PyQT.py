import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from kyrsovaya  import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        q= QPushButton('Вихід', self)
        q.clicked.connect(QCoreApplication.instance().quit)
        q.resize(300,100)
        q.move(250, 320)

        ng = QPushButton('Нова гра', self)
        ng.clicked.connect(self.warship)
        ng.resize(300, 100)
        ng.move(250, 120)

        hg = QPushButton('Інструкція до гри', self)
        hg.clicked.connect(self.help)
        hg.resize(300, 100)
        hg.move(250, 220)

        self.setGeometry(280, 50, 800, 600)
        self.setWindowTitle('Меню')
        self.show()


    def warship(self):
        warships(self)

    def help(self):
        f=open("help.txt","r")
        #print(f.read())
        t=f.read()
        msg = QMessageBox()
        msg.setText(t)
        #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.show()
        retval = msg.exec_()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Вихід з гри',
            "Ви точно хочете покинути гру?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())