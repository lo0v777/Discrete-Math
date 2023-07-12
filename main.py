from graph_shirina import *
from graph_deep import *
from graph_dijkstra import *
from graph_floida import *
from graph_ford import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def openBFS(self):
        self.window = QtWidgets.QMainWindow()
        self.uiBFS = Вreadth()
        self.uiBFS.setupUi(self.window)
        self.window.show()

    def openDFS(self):
        self.window = QtWidgets.QMainWindow()
        self.uiDFS = Deep()
        self.uiDFS.setupUi(self.window)
        self.window.show()

    def openDijkstra(self):
        self.window = QtWidgets.QMainWindow()
        self.uiDijkstra = Dijkstra()
        self.uiDijkstra.setupUi(self.window)
        self.window.show()

    def openFloid(self):
        self.window = QtWidgets.QMainWindow()
        self.uiFloid = Floid()
        self.uiFloid.setupUi(self.window)
        self.window.show()
    def openFord(self):
        self.window = QtWidgets.QMainWindow()
        self.uiFord = Ford()
        self.uiFord.setupUi(self.window)
        self.window.show()


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(874, 472)
        mainWindow.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 30, 341, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openBFS)  # открывается окно BFS
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 240, 341, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openFloid)  # открывается окно Floid
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 170, 341, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openDijkstra)  # открывается окно Dijkstra
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 100, 341, 51))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.openDFS)  # открывается окно DFS
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 380, 341, 51))
        self.pushButton_5.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openFord)  # открывается окно Ford
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 310, 341, 51))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.pushButton.setText(_translate("mainWindow", "ОБХОД ГРАФА В ШИРИНУ"))
        self.pushButton_2.setText(_translate("mainWindow", "АЛГОРИТМ ФЛОЙДА"))
        self.pushButton_3.setText(_translate("mainWindow", "АЛГОРИТМ ДЕЙКСТРЫ"))
        self.pushButton_4.setText(_translate("mainWindow", "ОБХОД ГРАФА В ГЛУБИНУ"))
        self.pushButton_5.setText(_translate("mainWindow", "АЛГОРИТМ ФОРДА-ФАЛКЕРСОНА"))
        self.pushButton_6.setText(_translate("mainWindow", "АЛГОРИТМ ДАНЦИГА"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
