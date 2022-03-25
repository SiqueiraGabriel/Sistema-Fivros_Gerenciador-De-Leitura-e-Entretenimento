from Modulos import Banco
from Modulos.Bibliotecas import *
from Modulos.ClasseCategoria import Categoria
from Modulos.TelaPrincipal import *
from Modulos.Banco import *
from sqlite3 import *


caminho = os.path.dirname(__file__)
app = Tk()
app.title("Sistema Fivros - Gerenciamento de Leitura e Entretenimento")
#Dimension of Program
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width}x{height}")
app.configure(background="#ddd")
# --------------------------------------------------------------------------

app.update_idletasks()


user = Usuario()
user.createViewLogar(app)



# --------------------------------------------------------------------------

app.mainloop()