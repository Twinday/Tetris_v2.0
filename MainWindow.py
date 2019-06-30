from GameLogics import Level
from Game_interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

import colors


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        # мои переменные
        self.g = Level(0)
        self.g.create_level()
        self.lup = self.g.get_lup()
        self.score = self.g.get_score()
        self.level = 1

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_tick)

        self.buttonStart.clicked.connect(self.start)
        self.btn_info.clicked.connect(self.information)


    def keyPressEvent(self, event):
        dict = {
            QtCore.Qt.Key_W: self.up,
            QtCore.Qt.Key_S: self.down,
            QtCore.Qt.Key_A: self.left,
            QtCore.Qt.Key_D: self.right,
            QtCore.Qt.Key_F: self.update
        }
        try:
            dict[event.key()]()
        except:
            pass

    def show_matrix_in_table(self):
        self.lup = self.g.get_lup()
        self.score = self.g.get_score()
        for row in range(self.g.height):
            for col in range(self.g.width):
                item = self.g[row, col]
                cellinfo = QTableWidgetItem(' ')
                if row == self.lup[0] and col == self.lup[1]:
                    cellinfo = QTableWidgetItem('o')
                # Только для чтения
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                cellinfo.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                cellinfo.setFont(QtGui.QFont('SansSerif', 22))
                self.tableWidget.setItem(row, col, cellinfo)
                color = colors.my_color[item]
                self.tableWidget.item(row, col).setBackground(QtGui.QColor(color[0], color[1], color[2]))

        self.label_score.setText("Score: " + str(self.score))
        self.label_level.setText("Level " + str(self.level))
        self.label_score.setFont(QtGui.QFont('SansSerif', 14))
        self.label_level.setFont(QtGui.QFont('SansSerif', 14))


    def decor_update_view(func):
        def wrapped(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.show_matrix_in_table(*args, **kwargs)
        return wrapped

    # Описываем функции
    @decor_update_view
    def left(self):
        self.g.move_border('left')


    @decor_update_view
    def right(self):
        self.g.move_border('right')


    @decor_update_view
    def down(self):
        self.g.move_border('down')


    @decor_update_view
    def up(self):
        self.g.move_border('up')


    @decor_update_view
    def update(self):
        self.g.update()
        self.score = self.g.get_score()
        self.check_new_level()


    @decor_update_view
    def timer_tick(self):
        self.g.add_row()
        if self.g.check_game_over():
            self.timer.stop()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Game Over!")
            msg.setInformativeText("Your level " + str(self.level))
            msg.setWindowTitle("Game")
            msg.addButton('Ok', QMessageBox.AcceptRole)
            msg.exec()
            self.start()


    def start(self):
        self.g = Level(0)
        self.g.create_level()
        self.lup = self.g.get_lup()
        self.score = self.g.get_score()
        self.level = 1

        self.show_matrix_in_table()
        self.timer.start(2500)


    def check_new_level(self):
        if self.score >= 20000:
            self.new_level()


    def new_level(self):
        self.level += 1
        self.g = Level(0)
        self.g.create_level()
        self.score = self.g.get_score()
        self.lup = self.g.get_lup()


    def information(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Цель игры: удалять по 4 и больше соеденённых блоков.")
        msg.setInformativeText("Управление: (WASDF)\n"
                               "W, A, S, D - двигаемся по полю вверх/влево/вниз/вправо соответственно,\n"
                               "F - удаляем блоки, если это возможно.")
        msg.setWindowTitle("Game")
        msg.addButton('Ok', QMessageBox.AcceptRole)
        msg.exec()
