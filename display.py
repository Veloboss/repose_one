class Display:

    def __init__(self, x=1, y=1, met='X'):
        self.x = x
        self.y = y
        self.met = met
        self.lst_table = ['               -------', ['                              |', ' ', '|', ' ', '|', ' ', '|'],
             '               -------', ['                              |', ' ', '|', ' ', '|', ' ', '|'],
             '               -------', ['                              |', ' ', '|', ' ', '|', ' ', '|'],
             '               -------']

    def disp_x(self):
        lst = self.lst_table
        mas = lst[self.x]  # 
        mas.pop(self.y)
        mas.insert(self.y, self.met)
        return lst

    def enter_(self):
        lst = self.lst_table
        mas = lst[self.x]
        mas.pop(self.y)
        mas.insert(self.y, self.met)
        print(f"""                         Нажал ENTER {self.x} {self.y}""")
        return lst


    def veisible_disp(self, lst):

        print(f"""

                      "К Р Е С Т И К И   Н О Л И К И"
                      версия 0.1а made in "Veloboss"

                        """)

        for item in lst:
            print(*item) # Отображает таблицу

        print(f"""
                        положение курсора
                        x - {self.x}, y - {self.y}
                """)



