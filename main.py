import View.Main.AbaPrincipal, View.Main.Menu
from tkinter import *
import os.path

caminho = os.path.dirname(__file__)


app = Tk()
app.title("Sistema Fivros - Gerenciamento de Leitura e Entretenimento")
#Dimension of Program
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width}x{height}")
app.configure(background="#ddd")
# --------------------------------------------------------------------------

View.Main.Menu.criarMenu(app) #Adição menu
View.Main.AbaPrincipal.criar(app)


# --------------------------------------------------------------------------
app.mainloop()