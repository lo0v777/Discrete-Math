from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from collections import deque
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Вreadth(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 50, 41, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 181, 31))
        self.label.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 181, 31))
        self.label_2.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 151, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 100, 181, 111))
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
        self.label.setText(_translate("MainWindow", " Введите вершину графа"))
        self.label_2.setText(_translate("MainWindow", " Введите матрицу смежности"))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))

    def addfunc(self):
        def button_clicked():
            matrix = self.textEdit.toPlainText()
            adjacency_matrix = np.array([[int(j) for j in i.split(' ')] for i in matrix.strip().split('\n')])
            for i in adjacency_matrix:
                for j in i:
                    if j != 1 and j != 0:
                        self.show_error_message('Данные введены неверно')
                        return
            start_vertex = int(self.lineEdit.text())
            self.bfs_work(start_vertex, adjacency_matrix)

        self.pushButton.clicked.connect(button_clicked)

    def show_error_message(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Error")
        error_box.setText("An error occurred:")
        error_box.setInformativeText(message)
        error_box.exec()

    def bfs_work(self, start_vertex, adjacency_matrix):
        num_vert = len(adjacency_matrix)  # задаем количество вершин
        visited = [False] * num_vert  # отслеживается посещяли ли мы вершину или нет
        parents = [None] * num_vert  # родительские вершины
        distances = [0] * num_vert  # расстояния от начальной вершины до каждой вершины

        queue = deque([start_vertex])  # задаем очередь
        visited[start_vertex] = True  # определяем начльную вершину как посещенную

        while queue:
            u = queue.popleft()  # извлекаем первый элемент
            for v in range(num_vert):  # перебираем все вершины графа
                if adjacency_matrix[u][v] != 0 and not visited[v]:  # проверяем, есть ли ребро между текущей вершиной u и вершиной v,не посещали ли мы вершину v ранее
                    visited[v] = True  # помечаем вершину v как посещенную
                    parents[v] = u  # указываем, что вершина u является родительской для вершины v.
                    distances[v] = distances[u] + 1  # устанавливаем расстояние от начальной вершины до вершины v как расстояние до вершины u плюс единица.
                    queue.append(v)  # добавляем вершину v в очередь для дальнейшего обхода
        spanning_tree_vertices = [i for i in range(num_vert) if visited[i]]  # содержатся индексы вершин, которые были посещены во время обхода графа
        spanning_tree_matrix = np.zeros((num_vert, num_vert))  # инициализируем матрицу смежности покрывающего дерева нулями

        for v in range(num_vert):
            if parents[v] is not None:
                u = parents[v]
                spanning_tree_matrix[u][v] = 1
                spanning_tree_matrix[v][u] = 1

        result_text = ""
        result_text += "Вершины покрывающего дерева:\n"
        result_text += str(spanning_tree_vertices) + "\n\n"
        result_text += "Матрица смежности покрывающего дерева:\n"
        result_text += str(spanning_tree_matrix) + "\n\n"
        self.label_output.setText(result_text)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Вreadth()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
