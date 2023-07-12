from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Dijkstra(object):
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
        self.label_output_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_output_2.setGeometry(QtCore.QRect(440, 110, 321, 151))
        self.label_output_2.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_output_2.setText("")
        self.label_output_2.setObjectName("label_output_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.addfunc()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.addfunc()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Введите начальную вершину "))
        self.label_2.setText(_translate("MainWindow", " Введите матрицу смежности"))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))
        self.label_4.setText(_translate("MainWindow", " Введите конечную вершину "))

    def addfunc(self):
        def button_clicked():
            matrix = self.textEdit.toPlainText()
            adjacency_matrix = np.array([[int(j) for j in i.split(' ')] for i in matrix.strip().split('\n')])
            start_vertex = int(self.lineEdit.text()) - 1
            last_vertex = int(self.lineEdit_2.text()) - 1
            self.dijkstra(start_vertex, last_vertex, adjacency_matrix)

        self.pushButton.clicked.connect(button_clicked)

    def get_all_short_paths(self, start_vertex, previous_vertices, num_vertices):
        all_paths = []

        for v in range(num_vertices):
            if v != start_vertex:
                path = self.get_short_path(start_vertex, v, previous_vertices)
                all_paths.append((v + 1, path))

        return all_paths

    def dijkstra(self, start_vertex, last_vertex, adjacency_matrix):
        num_vertices = len(adjacency_matrix)
        dist = [float('inf')] * num_vertices
        dist[start_vertex] = 0
        visited = [False] * num_vertices
        previous_vertices = [-1] * num_vertices

        while not visited[last_vertex]:
            min_dist = float('inf')
            current_vertex = -1

            for v in range(num_vertices):
                if not visited[v] and dist[v] < min_dist:
                    min_dist = dist[v]
                    current_vertex = v

            if current_vertex == -1:
                break

            visited[current_vertex] = True

            for v in range(num_vertices):
                if (
                        not visited[v]
                        and adjacency_matrix[current_vertex][v] > 0
                        and dist[current_vertex] + adjacency_matrix[current_vertex][v] < dist[v]
                ):
                    dist[v] = dist[current_vertex] + adjacency_matrix[current_vertex][v]
                    previous_vertices[v] = current_vertex

        if not visited[last_vertex]:
            self.label_output.setText("Маршрут не существует")
        else:
            all_paths = self.get_all_short_paths(start_vertex, previous_vertices, num_vertices)
            label_text = f"Длина маршрута: {dist[last_vertex]}\n"
            label_text += "Маршруты:\n"

            for vertex, path in all_paths:
                label_text += f"{vertex}: {path}\n"

            self.label_output.setText(label_text)

            distances = [f"Расстояние до вершины {v+ 1}: {dist[v]}" for v in range(num_vertices)]
            self.label_output_2.setText('\n'.join(distances))

    def get_short_path(self, start_vertex, last_vertex, previous_vertices):
        path = []
        current_vertex = last_vertex

        while current_vertex != -1:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]

        if path[0] == start_vertex:
            return ' -> '.join(str(vertex + 1) for vertex in path)
        else:
            return "Маршрут не найден"


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Dijkstra()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())