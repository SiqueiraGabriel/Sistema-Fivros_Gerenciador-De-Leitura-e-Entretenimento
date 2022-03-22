from Modulos.Bibliotecas import *
from Modulos.Categoria import Categoria
from Modulos.TelaPrincipal import *

caminho = os.path.dirname(__file__)


app = Tk()
app.title("Sistema Fivros - Gerenciamento de Leitura e Entretenimento")
#Dimension of Program
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width}x{height}")
app.configure(background="#ddd")
# --------------------------------------------------------------------------

criarMenu(app)
TelaPrincipal().criar(app)


# --------------------------------------------------------------------------
app.mainloop()