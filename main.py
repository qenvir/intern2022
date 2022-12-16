'''

Copyright (c) 2022 and later Qenvi.
Developed by Qenvi and affiliates which hold all
intellectual property rights. Use of this software is subject
to a specific license granted by Qenvi.

'''

import serial
import random
from tkinter import Tk, Label

msg_port_serie = serial.Serial(port='COM5', baudrate=57600, timeout=1.0)


class MyWindow(Tk):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.prex = 0
        self.prey = 0
        self.greenx = 0
        self.greeny = 0
        self.direction = "S"
        self.dernieresCases = []
        self.lenght = 5
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(10, weight=1)
        self.grid_rowconfigure(11, weight=1)
        self.grid_rowconfigure(12, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)
        self.grid_columnconfigure(8, weight=1)
        self.grid_columnconfigure(9, weight=1)
        self.grid_columnconfigure(10, weight=1)
        self.grid_columnconfigure(11, weight=1)
        self.grid_columnconfigure(12, weight=1)

        button_dict = {"bg": "#22cbff", "fg": "white", "font": ("Arial", 25, "bold")}
        self.blue_button_dict = {"bg": "#22cbff", "fg": "white", "font": ("Arial", 25, "bold")}
        self.red_button_dict = {"bg": "#eb144c", "fg": "white", "font": ("Arial", 25, "bold")}
        self.green_button_dict = {"bg": "#81c784", "fg": "white", "font": ("Arial", 25, "bold")}
        self.grid_dict = {"sticky": "nswe", "padx": 10, "pady": 10}

        boutton = []
        for i in range(13):
            boutton.append(Label(self, text=" ", **button_dict))
            boutton[i].grid(column=i, row=0, **self.grid_dict)

        boutton2 = []
        for i in range(13):
            boutton2.append(Label(self, text=" ", **button_dict))
            boutton2[i].grid(column=i, row=1, **self.grid_dict)

        boutton3 = []
        for i in range(13):
            boutton3.append(Label(self, text=" ", **button_dict))
            boutton3[i].grid(column=i, row=2, **self.grid_dict)

        boutton4 = []
        for i in range(13):
            boutton4.append(Label(self, text=" ", **button_dict))
            boutton4[i].grid(column=i, row=3, **self.grid_dict)

        boutton5 = []
        for i in range(13):
            boutton5.append(Label(self, text=" ", **button_dict))
            boutton5[i].grid(column=i, row=4, **self.grid_dict)

        boutton6 = []
        for i in range(13):
            boutton6.append(Label(self, text=" ", **button_dict))
            boutton6[i].grid(column=i, row=5, **self.grid_dict)

        boutton7 = []
        for i in range(13):
            boutton7.append(Label(self, text=" ", **button_dict))
            boutton7[i].grid(column=i, row=6, **self.grid_dict)

        boutton8 = []
        for i in range(13):
            boutton8.append(Label(self, text=" ", **button_dict))
            boutton8[i].grid(column=i, row=7, **self.grid_dict)

        boutton9 = []
        for i in range(13):
            boutton9.append(Label(self, text=" ", **button_dict))
            boutton9[i].grid(column=i, row=8, **self.grid_dict)

        boutton10 = []
        for i in range(13):
            boutton10.append(Label(self, text=" ", **button_dict))
            boutton10[i].grid(column=i, row=9, **self.grid_dict)

        boutton11 = []
        for i in range(13):
            boutton11.append(Label(self, text=" ", **button_dict))
            boutton11[i].grid(column=i, row=10, **self.grid_dict)

        boutton12 = []
        for i in range(13):
            boutton12.append(Label(self, text=" ", **button_dict))
            boutton12[i].grid(column=i, row=11, **self.grid_dict)

        boutton13 = []
        for i in range(13):
            boutton13.append(Label(self, text=" ", **button_dict))
            boutton13[i].grid(column=i, row=12, **self.grid_dict)

        self.greenx = random.choice(range(0, 13))
        self.greeny = random.choice(range(0, 13))

        green_button = Label(self, text=" ", **self.green_button_dict)
        green_button.grid(column=self.greenx, row=self.greeny, **self.grid_dict)

        self.attributes('-fullscreen', True)

        self.title("ArduinoSnakeGame")

    def touche_appuyees(self, event):
        if event.keysym == "Escape":
            self.quit()

    def monTimer(self):
        line = msg_port_serie.readline()

        if line:
            string = line.decode()
            string = string[:-2]
            string = string.split(",")
            lectureX = int(string[0])
            lectureY = int(string[1])

            facing = None
            if lectureY == -1:
                facing = "N"
            if lectureY == 1:
                facing = "S"
            if lectureX == -1:
                facing = "W"
            if lectureX == 1:
                facing = "E"

            if facing is not self.direction and facing is not None:
                if (self.direction == "S" and facing == "N") or (self.direction == "N" and facing == "S") or (
                        self.direction == "E" and facing == "W") or (self.direction == "W" and facing == "E"):
                    pass
                else:
                    self.direction = facing

            if self.direction == "N":
                self.y += -1
            if self.direction == "S":
                self.y += 1
            if self.direction == "W":
                self.x += -1
            if self.direction == "E":
                self.x += 1

            if self.x < 0:
                self.x = 12
                self.quit()

            if self.x > 12:
                self.x = 0
                self.quit()

            if self.y < 0:
                self.y = 12
                self.quit()

            if self.y > 12:
                self.y = 0
                self.quit()

            bouton = Label(self, text=" ", **self.red_button_dict)
            bouton.grid(column=self.x, row=self.y, **self.grid_dict)

            if (self.x, self.y) in self.dernieresCases:
                self.quit()

            if len(self.dernieresCases) > self.lenght:
                bouton2 = Label(self, text=" ", **self.blue_button_dict)

                bouton2.grid(column=self.dernieresCases[0][0], row=self.dernieresCases[0][1], **self.grid_dict)

                print(self.dernieresCases[0][0])
                print(self.dernieresCases[0][1])

                self.dernieresCases.remove(self.dernieresCases[0])

            self.dernieresCases.append((self.x, self.y))
            for i in range(0, len(self.dernieresCases)):
                bb = Label(self, text=" ", **self.red_button_dict)
                bb.grid(column=self.dernieresCases[i][0], row=self.dernieresCases[i][1], **self.grid_dict)

            if self.x == self.greenx and self.y == self.greeny:
                self.lenght += 1
                self.dernieresCases.append((self.x, self.y))

                listX = []
                listY = []
                for i in range(0, len(self.dernieresCases)):
                    listX.append(self.dernieresCases[i][0])
                    listY.append(self.dernieresCases[i][1])

                while (self.greenx, self.greeny) in self.dernieresCases:
                    self.greenx = random.choice(range(0, 13))
                    self.greeny = random.choice(range(0, 13))

                green_button = Label(self, text=" ", **self.green_button_dict)
                green_button.grid(column=self.greenx, row=self.greeny, **self.grid_dict)

            if len(self.dernieresCases) < 0:
                if self.prex != self.x or self.prey != self.y:
                    bouton2 = Label(self, text=" ", **self.blue_button_dict)
                    bouton2.grid(column=self.prex, row=self.prey, **self.grid_dict)

                    self.prex = self.x
                    self.prey = self.y

        self.update()
        window.after(10, self.monTimer)


window = MyWindow()
window.bind("<KeyRelease>", window.touche_appuyees)
window.after(10, window.monTimer)
window.mainloop()
