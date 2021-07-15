from display import Display
import os


class Coord:

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def left(self):
        os.system('cls||clear')
        # функция перемещения влево keyboard.add_hotkey('left', s_left) при нажатии влево перемещается на 2 позиции
        # во вложенном списке self.lst_table класса Display (display.py) из которой формируется таблица
        self.y -= 2
        if self.y == 7:
            self.y = 1
        if self.y == -1:
            self.y = 5
        disp = Display(self.x, self.y) # вызов класса
        disp.veisible_disp(disp.disp_x()) # отображает изменение при нажатии клавиши влево и отображает там Х


    def right(self):
        os.system('cls||clear')
        # анологично функции left
        self.y += 2
        if self.y == 7:
            self.y = 1
        if self.y == -1:
            self.y = 5
        disp = Display(self.x, self.y)
        disp.veisible_disp(disp.disp_x())

    def down(self):
        os.system('cls||clear')
        # анологично функции left
        self.x += 2
        if self.x == 7:
            self.x = 1
        if self.x == -1:
            self.x = 5
        disp = Display(self.x, self.y)
        disp.veisible_disp(disp.disp_x())


    def up(self):
        os.system('cls||clear')
        # анологично функции left
        self.x -= 2
        if self.x == 7:
            self.x = 1
        if self.x == -1:
            self.x = 5
        disp = Display(self.x, self.y)
        disp.veisible_disp(disp.disp_x())

    def enter_(self):
        os.system('cls||clear')
        # Должна записывать в self.lst_table X или O
        disp = Display(self.x, self.y)
        disp.veisible_disp(disp.disp_x())
        disp.enter_()
