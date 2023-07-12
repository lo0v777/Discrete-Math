from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from collections import deque
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Ford(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 50, 41, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
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
        self.label_2.setGeometry(QtCore.QRect(30, 110, 191, 31))
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
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(30, 320, 341, 251))
        self.label_output.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(444, 315, 261, 251))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 50, 181, 31))
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(640, 50, 41, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.addfunc()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Введите вершину истока "))
        self.label_2.setText(_translate("MainWindow", " Введите взвешенную матрицу"))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))
        self.label_4.setText(_translate("MainWindow", " Введите вершину стока "))

    def addfunc(self):
        def button_clicked():
            matrix = self.textEdit.toPlainText()
            adjacency_matrix = np.array([[int(j) for j in i.split(' ')] for i in matrix.strip().split('\n')])
            start_vertex = int(self.lineEdit.text())
            last_vertex = int(self.lineEdit_2.text())
            self.calculateMaxFlow(start_vertex, last_vertex, adjacency_matrix)

        self.pushButton.clicked.connect(button_clicked)

    def calculateMaxFlow(self, start_vertex, last_vertex, adjacency_matrix):
        # Преобразование матрицы смежности в граф NetworkX
        graph = nx.from_numpy_matrix(adjacency_matrix, create_using=nx.DiGraph())

        # Алгоритм Форда-Фалкерсона
        def ford_fulkerson(graph, start_vertex, last_vertex):
            # Создание остаточного графа
            residual_graph = graph.copy()

            # Инициализация потока
            max_flow = 0

            # Поиск увеличивающего пути с помощью поиска в ширину
            def bfs(graph, start_vertex, last_vertex, parent):
                visited = [False] * graph.number_of_nodes()
                queue = deque()
                queue.append(start_vertex)
                visited[start_vertex] = True

                while queue:
                    current_vertex = queue.popleft()
                    for neighbor in graph.edges(current_vertex):
                        capacity = graph[current_vertex][neighbor]['capacity']
                        if not visited[neighbor] and capacity > 0:
                            queue.append(neighbor)
                            visited[neighbor] = True
                            parent[neighbor] = current_vertex
                            if neighbor == last_vertex:
                                return True
                return False

            parent = [-1] * graph.number_of_nodes()

            while bfs(residual_graph, start_vertex, last_vertex, parent):
                path_flow = float('inf')
                s = last_vertex
                while s != start_vertex:
                    path_flow = min(path_flow, residual_graph[parent[s]][s]['capacity'])
                    s = parent[s]

                max_flow += path_flow

                v = last_vertex
                while v != start_vertex:
                    u = parent[v]
                    residual_graph[u][v]['capacity'] -= path_flow
                    residual_graph[v][u]['capacity'] += path_flow
                    v = parent[v]

            # Визуализация графа
            pos = nx.spring_layout(graph)
            plt.figure(figsize=(8, 6))
            nx.draw_networkx(graph, pos=pos, with_labels=True, node_color='lightblue')
            nx.draw_networkx_edges(graph, pos=pos, edgelist=residual_graph.edges(), edge_color='gray',
                                   width=1.0, style='dashed')
            plt.title("Residual Graph")
            plt.axis('off')
            plt.show()

            # Вывод результата
            message_box = QMessageBox()
            message_box.setWindowTitle("Ford-Fulkerson Algorithm")
            message_box.setText("Максимальный поток: {}".format(max_flow))
            message_box.exec_()

        ford_fulkerson(graph, start_vertex, last_vertex)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ford()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())