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
        abaPrincipal = ttk.Notebook(app)
        Modulos.Menu.criarMenu(app, idUsuario=idUsuario)
        abaPrincipal.place(x=10, y=10, width=1340, height=700)
        self.addFrames(abaPrincipal)



    def addFrames(self, aba):
        #Criação dos Frames - utilizando um dicionário


        frameLivro = self.criacaoAbas(aba, "Livros", "MEUS LIVROS")
        #frameFilme = self.criacaoAbas(aba, "Filmes", "MEUS FILMES")
        #frameSerie = self.criacaoAbas(aba, "Séries", "MINHAS SÉRIES")
        #frameAnime = self.criacaoAbas(aba, "Animes", "MEUS ANIMES")
        #frameDocumentario = self.criacaoAbas(aba, "Documentário", "MEUS DOCUMENTÁRIOS")

        #Adição dos itens ao Frame
        #tv_Livro = self.addTreView(frameLivro[0], "AUTOR")
        #tv_Filme = self.addTreView(frameFilme[0], "DIRETOR")
        #tv_Serie = self.addTreView(frameSerie[0], "DIRETOR")
        #tv_Anime = self.addTreView(frameAnime[0], "DIRETOR")
        #tv_Documentario = self.addTreView(frameDocumentario[0], "Diretor")


    def criacaoAbas(self, aba, nome, titulo):

        #Criação do Frames principais
        fr_Principal = Frame(aba, borderwidth=1, relief='ridge')
        fr_Principal.place(x=0, y=0, width=1300)
        aba.add(fr_Principal, text=nome)

        #Criação dos Frames Secundários
        fr_Conteudo = Frame(fr_Principal, borderwidth=1, relief='ridge')
        fr_Menu = Frame(fr_Principal, borderwidth=1, relief='ridge')
        fr_AbaSecundaria = Frame(fr_Conteudo)

        #Adição dos Frames
        fr_Conteudo.place(x=10, y=10,width=1050, height=600)
        fr_Menu.place(x=1060, y=10, width=260, height=600)
        Label(fr_Conteudo, text=titulo, anchor="center", font=("Arial",15)).pack(padx=10)
        self.addMenuLateral(fr_Menu)

        #Criação da Aba Dentro aba
        self.abaSituacao = ttk.Notebook(fr_Conteudo)


        #Apenas até estabeelecer BD
        autor ="Escritor"

        #Frames da Aba Situacao
        fr_Todos = Frame(fr_Conteudo)
        fr_Recomendado = Frame(fr_Conteudo)
        fr_Iniciado = Frame(fr_Conteudo)
        fr_Finalizado = Frame(fr_Conteudo)
        fr_FantasmaMemoria = Frame(fr_Conteudo)

        #Aba Todos
        self.abaSituacao.add(fr_Todos, text="Todos")
        self.addTreView(fr_Todos, autor, "Todos", "Livro")

        #Aba Recomendado
        self.abaSituacao.add(fr_Recomendado, text="Recomendado")
        self.addTreView(fr_Recomendado, autor, "Recomendado", "Livro")

        #aba Iniciado
        self.abaSituacao.add(fr_Iniciado, text="Iniciado")
        self.addTreView(fr_Iniciado, autor, "Iniciado", "Livro")

        #aba Finalizado
        self.abaSituacao.add(fr_Finalizado, text="Finalizado")
        self.addTreView(fr_Finalizado, autor, "Finalizado", "Livro")

        #aba FantasmaMemoria
        self.abaSituacao.add(fr_FantasmaMemoria, text="Fantasma na Memória")
        self.addTreView(fr_FantasmaMemoria, autor, "Fantasma na Memória", "Livro")


        #Retorno dos frames de Conteúdo e Menu
        self.abaSituacao.place(x=25, y=70, width=1000, height=150)
        return [fr_Conteudo, fr_Menu]



    def addTreView(self, fr_Responsavel, colunaAutor, status, nomeTabela):
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
        tv.insert("", 'end', values=('1', 'A Volta ao Mundo em 80 dias','Julio Verne','Aventura','Finalizado'))
        return tv


    def addMenuLateral(self, fr_Menu):
        caminho = os.path.dirname(__file__)



        btnAdicionar = Button(fr_Menu, text="Adicionar", command=self.semAcao)
        btnAlterar = Button(fr_Menu, text="Alterar", command=self.semAcao)
        btnExcluir = Button(fr_Menu, text="Excluir ", command=self.semAcao)
        btnVisualizar = Button(fr_Menu, text="Visualização Completa", command=self.semAcao)
        btnRelatorio = Button(fr_Menu, text="Gerar Relatório em PDF", command=self.semAcao)
        Label(fr_Menu, text="MENU", anchor="center").place(width=240)
        btnAdicionar.place(y=50, x=10, width=240, height=30)
        btnAlterar.place(y=90, x=10, width=240, height=30)
        btnExcluir.place(y=130, x=10, width=240, height=30)
        btnVisualizar.place(y=170, x=10, width=240, height=30)
        btnRelatorio.place(y=210, x=10, width=240, height=30)



