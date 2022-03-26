from Modulos.ClasseCategoria import *
import os.path
from tkinter import *
from tkinter import ttk

import Modulos.Menu


class TelaPrincipal:

    def __init__(self, app):
        print()

    def semAcao(self):
        print()

    def criar(self, app, idUsuario):
        self.idUsuario = idUsuario
        framePrincipal = Frame(app)
        Modulos.Menu.criarMenu(app, idUsuario=idUsuario)
        framePrincipal.place(x=10, y=30, width=1340, height=670)
        self.criacaoAbas(framePrincipal)



    def addFrames(self, aba):

        #Criação dos Frames - utilizando um dicionário
        listaCategoria = Categoria().returnAllCategoria()

        #Criação das Abas
        for itemCategoria in listaCategoria:
            self.criacaoAbas(aba, itemCategoria[1], itemCategoria[1], itemCategoria[0], itemCategoria[2])


        #Adição dos itens ao Frame
        #tv_Livro = self.addTreView(frameLivro[0], "AUTOR")
        #tv_Filme = self.addTreView(frameFilme[0], "DIRETOR")
        #tv_Serie = self.addTreView(frameSerie[0], "DIRETOR")
        #tv_Anime = self.addTreView(frameAnime[0], "DIRETOR")
        #tv_Documentario = self.addTreView(frameDocumentario[0], "Diretor")


    def criacaoAbas(self, aba, nome="", titulo="Teste", idCategoria="", autor=""):

        #Criação do Frames principais
        self.fr_Principal = Frame(aba, borderwidth=1, relief='ridge')
        #fr_Principal.place(x=0, y=0, width=1300)
        #aba.add(fr_Principal, text=nome)

        #Criação dos Frames Secundários
        self.fr_Conteudo = Frame(aba, borderwidth=1, relief='ridge')
        self.fr_Menu = Frame(aba, borderwidth=1, relief='ridge')
        #fr_AbaSecundaria = Frame(fr_Conteudo)

        #Adição dos Frames
        self.fr_Conteudo.place(x=270, y=10,width=1050, height=600)
        self.fr_Menu.place(x=10, y=10, width=260, height=670)
        Label(self.fr_Conteudo, text=titulo, anchor="center", font=("Arial",15)).pack(padx=10)
        self.btnAbrirMenu = Button(self.fr_Conteudo, text="|||",  background="#8C1018", foreground="#fff", command=self.abrirMenu)
        self.addMenuLateral(self.fr_Menu)

        #Criação da Aba Dentro aba
        self.abaSituacao = ttk.Notebook(self.fr_Conteudo)


        #Adicionar os valores de Situação
        self.addAppCategoriaSituacao(self.fr_Conteudo, idCategoria, autor=autor)


        #Retorno dos frames de Conteúdo e Menu
        self.abaSituacao.place(x=25, y=70, width=1000, height=150)
        return [self.fr_Conteudo, self.fr_Menu]



    def addTreView(self, fr_Responsavel, colunaAutor, status, idCategoria):
        if(status == "Todos"):
            tv = ttk.Treeview(fr_Responsavel, columns=('id','nome','autor','genero', 'status'), show="headings")
            tv.column('genero', minwidth=50, width=150)
            tv.column('status', minwidth=25, width=80)
            tv.heading('status', text="STATUS")
        else:
            tv = ttk.Treeview(fr_Responsavel, columns=('id','nome','autor','genero'), show="headings")
            tv.column('genero', minwidth=150, width=230)


        tv.column('id', minwidth=25, width=50)
        tv.column('nome', minwidth=150, width=550)
        tv.column('autor', minwidth=50, width=160)
        tv.heading('id', text="ID")
        tv.heading('nome',text="NOME")
        tv.heading('autor', text=colunaAutor.upper())
        tv.heading('genero', text="GÊNERO")


        tv.pack(pady=10)

        self.insertValuesOfCategoria(tv, idCategoria, status)


    def addAppCategoriaSituacao(self, fr_Conteudo, idCategoria, autor):

        #Frames da Aba Situacao
        fr_Todos = Frame(fr_Conteudo)
        fr_Recomendado = Frame(fr_Conteudo)
        fr_Iniciado = Frame(fr_Conteudo)
        fr_Finalizado = Frame(fr_Conteudo)
        fr_FantasmaMemoria = Frame(fr_Conteudo)

        #Aba Todos
        self.abaSituacao.add(fr_Todos, text="Todos")
        self.addTreView(fr_Todos, autor, "Todos", idCategoria)

        #Aba Recomendado
        self.abaSituacao.add(fr_Recomendado, text="Recomendado")
        #self.addTreView(fr_Recomendado, autor, "Recomendado", "Livro")

        #aba Iniciado
        self.abaSituacao.add(fr_Iniciado, text="Iniciado")
        #self.addTreView(fr_Iniciado, autor, "Iniciado", "Livro")

        #aba Finalizado
        self.abaSituacao.add(fr_Finalizado, text="Finalizado")
        #self.addTreView(fr_Finalizado, autor, "Finalizado", "Livro")

        #aba FantasmaMemoria
        self.abaSituacao.add(fr_FantasmaMemoria, text="Fantasma na Memória")
        #self.addTreView(fr_FantasmaMemoria, autor, "Fantasma na Memória", "Livro")


    def insertValuesOfCategoria(self, abaCategoria, idCategoria, status):
        abaCategoria.insert("", 'end', values=('1', 'A Volta ao Mundo em 80 dias', 'Julio Verne', 'Aventura', 'Finalizado'))

    def addMenuLateral(self, fr_Menu):
        caminho = os.path.dirname(__file__)


        self.btnFecharMenu = Button(fr_Menu, text="|||", background="#8C1018", foreground="#fff", command=self.fecharMenu)
        btnAdicionar = Button(fr_Menu, text="Adicionar", command=self.semAcao)
        btnAlterar = Button(fr_Menu, text="Alterar", command=self.semAcao)
        btnExcluir = Button(fr_Menu, text="Excluir ", command=self.semAcao)
        btnVisualizar = Button(fr_Menu, text="Visualização Completa", command=self.semAcao)
        btnRelatorio = Button(fr_Menu, text="Gerar Relatório em PDF", command=self.semAcao)
        lblMenuTitulo = Label(fr_Menu, text="Fivros", anchor="center", font=("Arial", 16, "bold"))


        self.btnFecharMenu.place(y=10, x=10, width=30, height=30)
        lblMenuTitulo.place(y=10, x=60, width=180, height=30)
        btnAdicionar.place(y=90, x=10, width=240, height=30)
        btnAlterar.place(y=130, x=10, width=240, height=30)
        btnExcluir.place(y=170, x=10, width=240, height=30)
        btnVisualizar.place(y=210, x=10, width=240, height=30)
        btnRelatorio.place(y=250, x=10, width=240, height=30)


    def abrirMenu(self):
        self.fr_Menu.place(width=260)
        self.fr_Conteudo.place(x=270, width=1050)
        self.btnAbrirMenu.place(width=0, height=0)

    def fecharMenu(self):
        self.fr_Menu.place(width=-10)
        self.fr_Principal.place(width=1310)
        self.fr_Conteudo.place(x=10, width=1320)
        self.btnAbrirMenu.place(width=30, height=30)
