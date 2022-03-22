from tkinter import *
from tkinter import ttk

class Categoria:

    def __init__(self):
        print()

    def createViewCadastro(self, app):
        self.appLogin = Toplevel()
        self.appLogin.title("Login de Usuários")
        self.appLogin.configure(background="#ddd")
        self.appLogin.geometry("300x200")
        self.appLogin.resizable(0, 0)
        self.appLogin.transient(app)





