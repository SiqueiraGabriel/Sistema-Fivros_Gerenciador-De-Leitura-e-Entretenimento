from tkinter import *
from tkcalendar2 import *

class Calendario:

    def __init__(self, aba):
        self.aba = aba
        self.cal = Calendar(aba, locale="pt_br")


    def get_data(self, campo):
        campo.delete(0, END)
        campo.insert(1, self.cal.get_date())
        self.cal.destroy()
        self.btnSelecionar.place(width=0)

    def inserirData(self, campo, verificador):
        self.btnSelecionar = Button(self.aba, text="Selecionar Data", command=lambda:self.get_data(campo))

        if verificador == 1:
            self.cal.place(x=0, y=85)
            self.btnSelecionar.place(x=20, y=45, width=160, height=25)

        if verificador == 2:
            self.cal.place(x=180, y=85)
            self.btnSelecionar.place(x=248, y=45, width=160, height=25)


