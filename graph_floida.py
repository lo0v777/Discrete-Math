from PyQt5 import QtCore, QtWidgets
import numpy as np
#работает с отрицательными ребрами
#Алгоритм Флойда-Уоршалла находит кратчайшие пути между каждой парой вершин в графе.


class Floid(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit.setGeometry(QtCore.QRect(230, 50, 41, 31))
        # self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.lineEdit.setObjectName("lineEdit")

        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(30, 320, 341, 251))
        self.label_output.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_output.setObjectName("label_output")

        self.label_output2 = QtWidgets.QLabel(self.centralwidget)
        self.label_output2.setGeometry(QtCore.QRect(444, 315, 261, 231))
        self.label_output2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_output2.setObjectName("label_output2")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 280, 801, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(30, 50, 181, 31))
        # self.label.setStyleSheet("background-color: rgb(0, 170, 0);")
        # self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 181, 31))
        self.label_2.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 190, 151, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 60, 181, 111))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.addfunc()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", " Введите вершину графа"))
        self.label_2.setText(_translate("MainWindow", " Введите матрицу смежности"))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))

    def addfunc(self):
        def button_clicked():
            matr = self.textEdit.toPlainText()
            adjacency_matrix = np.array([[int(j) for j in i.split(' ')] for i in matr.strip().split('\n')])
            matrix, path_matrix = self.floid(adjacency_matrix)

            result_text = ""
            result_text += "Матрица расстояний:\n"
            result_text += str(matrix) + "\n\n"
            result_text2 = ""
            result_text2 += "Матрица путей: \n"
            for row in path_matrix:
                result_text2 += str(row) + "\n"
            self.label_output2.setText(result_text2)
            self.label_output.setText(result_text)

        self.pushButton.clicked.connect(button_clicked)

    def floid(self, matrix):
        n = len(matrix)
        # Создаем матрицу путей
        path_matrix = [[j for j in range(n)] for i in range(n)]
        path = [[j for j in range(n)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    matrix[i][j] = 9999

        for k in range(n): #перебор всех вершин графа
            #перебор пар вершин
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
                        path_matrix[i][j] = k

        for i in range(n): #обработка полученных путей
            path_matrix[i][i] = None
            matrix[i][i] = 0
            for j in range(n):
                s = self.rout(path_matrix, i, j) #вызов метода для каждой пары вершин
                s.reverse() #получаем путь от начала к концу
                path[i][j] = s
        path_matrix = path
        return matrix, path_matrix

    def rout(self, P, end, start):
        path = [end]
        while end != start:
            end = P[end][start]
            if end is None:
                return None
            path.append(end)
        return path


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Floid()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
