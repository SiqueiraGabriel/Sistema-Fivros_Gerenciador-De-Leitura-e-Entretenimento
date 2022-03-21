import os.path
from tkinter import *
from tkinter import ttk

def semAcao():
    print()

def criar(app):
    abaPrincipal = ttk.Notebook(app)
    abaPrincipal.place(x=10, y=10, width=1340, height=700)
    addFrames(abaPrincipal)



def addFrames(aba):
    #Criação dos Frames
    frameLivro = criacaoAbas(aba, "Livros", "MEUS LIVROS")
    frameFilme = criacaoAbas(aba, "Filmes", "MEUS FILMES")
    frameSerie = criacaoAbas(aba, "Séries", "MINHAS SÉRIES")
    frameAnime = criacaoAbas(aba, "Animes", "MEUS ANIMES")
    frameDocumentario = criacaoAbas(aba, "Documentário", "MEUS DOCUMENTÁRIOS")

    #Adição dos itens ao Frame
    tv_Livro = addTreView(frameLivro[0], "AUTOR")
    tv_Filme = addTreView(frameFilme[0], "DIRETOR")
    tv_Serie = addTreView(frameSerie[0], "DIRETOR")
    tv_Anime = addTreView(frameAnime[0], "DIRETOR")
    tv_Documentario = addTreView(frameDocumentario[0], "Diretor")


def criacaoAbas(aba, nome, titulo):
    #Criação do Frames principais
    fr_Principal = Frame(aba, borderwidth=1, relief='ridge')
    fr_Principal.place(x=0, y=0, width=1300)
    aba.add(fr_Principal, text=nome)

    #Criação dos Frames Secundários
    fr_Conteudo = Frame(fr_Principal, borderwidth=1, relief='ridge')
    fr_Menu = Frame(fr_Principal, borderwidth=1, relief='ridge')

    #Adição dos Frames
    fr_Conteudo.place(x=10, y=10,width=1050, height=600)
    fr_Menu.place(x=1060, y=10, width=260, height=600)
    Label(fr_Conteudo, text=titulo, anchor="center", font=("Arial",15)).pack(padx=10)
    addMenuLateral(fr_Menu)

    #Retorno dos frames de Conteúdo e Menu
    return [fr_Conteudo, fr_Menu]


def addTreView(fr_Conteudo, colunaAutor):
    tv = ttk.Treeview(fr_Conteudo, columns=('id','nome','autor','genero', 'status'), show="headings")
    tv.column('id', minwidth=25, width=50)
    tv.column('nome', minwidth=150, width=550)
    tv.column('autor', minwidth=50, width=160)
    tv.column('genero', minwidth=50, width=150)
    tv.column('status', minwidth=25, width=80)
    tv.heading('id', text="ID")
    tv.heading('nome',text="NOME")
    tv.heading('autor', text=colunaAutor.upper())
    tv.heading('genero', text="GÊNERO")
    tv.heading('status', text="STATUS")


    tv.pack(pady=10)
    tv.insert("", 'end', values=('1', 'A Volta ao Mundo em 80 dias','Julio Verne','Aventura','Finalizado'))
    return tv

def addMenuLateral(fr_Menu):
    btnAdicionar = Button(fr_Menu, text="Adicionar", command=semAcao)
    btnAlterar = Button(fr_Menu, text="Alterar", command=semAcao)
    btnExcluir = Button(fr_Menu, text="Excluir ", command=semAcao)
    btnVisualizar = Button(fr_Menu, text="Visualização Completa", command=semAcao)
    btnRelatorio = Button(fr_Menu, text="Gerar Relatório em PDF", command=semAcao)
    Label(fr_Menu, text="MENU", anchor="center").place(width=240)
    btnAdicionar.place(y=50, x=10, width=240, height=30)
    btnAlterar.place(y=90, x=10, width=240, height=30)
    btnExcluir.place(y=130, x=10, width=240, height=30)
    btnVisualizar.place(y=170, x=10, width=240, height=30)
    btnRelatorio.place(y=210, x=10, width=240, height=30)





