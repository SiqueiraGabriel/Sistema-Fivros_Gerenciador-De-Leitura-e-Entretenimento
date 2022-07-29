from PIL import ImageTk, Image

from Modulos.ClasseCategoria import *
import os.path
from tkinter import *
from tkinter import ttk
from Modulos.Documento import Documento
import Modulos.Menu
from Modulos.DimensoesTela.DimensaoTelaPrincipal import *


class TelaPrincipal:

    def __init__(self, app):
        self.app = app

    def semAcao(self):
        print()

    def criar(self, app, idUsuario):
        self.idUsuario = idUsuario
        self.app = app
        framePrincipal = Frame(app)
        Modulos.Menu.criarMenu(app, idUsuario=idUsuario)
        framePrincipal.place(x=10, y=30, width=1340, height=670)
        self.criacaoAbas(framePrincipal)




    def criacaoAbas(self, aba):

        #Criação do Frames principais
        self.fr_Principal = Frame(aba, borderwidth=1, relief='ridge')

        #Teste
        my_pic = ImageTk.PhotoImage(file="LogoFivros-Menu.png")
        my_label = Label(self.fr_Principal, image=my_pic)
        my_label.place(x=10, y=10, width=200, height=200)


        #Criação dos Frames Secundários
        self.fr_Conteudo = Frame(aba, borderwidth=1, relief='ridge')
        self.fr_Menu = Frame(aba, borderwidth=1, relief='ridge')
        self.fr_Titulo = Frame(self.fr_Conteudo)
        self.fr_ApresentaAba = Frame(self.fr_Conteudo)


        #Adição do Menu Lateral
        self.btnAbrirMenu = Button(self.fr_Conteudo, text="|||", background="#8C1018", foreground="#fff", command=self.abrirMenu)
        self.addMenuLateral(self.fr_Menu)

        #Criação do Topo da Página
        self.criarTopoPagina()

        #Configuração das dimensões
        DimeElemetCriacaoAbas(self.fr_Conteudo, self.fr_Menu, self.fr_VisualizarCategoria, self.lblCategoria, self.optMenuCategoria, self.btnSelecionarCategoria, self.fr_Titulo, self.titulo)


        #Adicionar os valores de Situação
        self.addAppCategoriaSituacao()


        #Retorno dos frames de Conteúdo e Menu



    def criarTopoPagina(self):
        listaCategoria = Categoria().returnAllCategoria()
        self.varCategoria = StringVar()
        self.titulo = Label(self.fr_Titulo, text="MEUS CONTEÚDOS CADASTRADOS", anchor="center", font=("Arial", 15))
        self.fr_VisualizarCategoria = Frame(self.fr_Titulo)
        self.lblCategoria = Label(self.fr_VisualizarCategoria, text="Visualizar Categoria", background="#635959",
                                  font=("Arial", 10), foreground="#f6f6f6")
        self.optMenuCategoria = OptionMenu(self.fr_VisualizarCategoria, self.varCategoria, *listaCategoria)
        self.btnSelecionarCategoria = Button(self.fr_VisualizarCategoria, text="Selecionar", command=self.addAppCategoriaSituacao)


    def addTreView(self, fr_Responsavel, colunaAutor, status, idCategoria):

        if(status == "Todos"):
            tv = ttk.Treeview(fr_Responsavel, columns=('id','nome','autor','genero', 'status'), show="headings")
            tv.column('genero', minwidth=50, width=400)
            tv.column('status', minwidth=100, width=120)
            tv.heading('status', text="STATUS")
        else:
            tv = ttk.Treeview(fr_Responsavel, columns=('id','nome','autor','genero'), show="headings")
            tv.column('genero', minwidth=300, width=400)

        self.addMenuLateral(self.fr_Menu, tv)

        btnAbrir = Button(fr_Responsavel, text="Ver", command=lambda:self.ver(tv, 1)).pack()
        btnExcluir = Button(fr_Responsavel, text="Excluir", command=lambda:self.ver(tv, 2)).pack()

        tv.column('id', minwidth=0, width=0)
        tv.column('nome', minwidth=150, width=500)
        tv.column('autor', minwidth=50, width=160)
        tv.heading('id', text="ID")
        tv.heading('nome',text="TÍTULO DA OBRA")
        tv.heading('autor', text=colunaAutor.upper())
        tv.heading('genero', text="GÊNERO")


        tv.pack(pady=10)

        self.insertValuesOfCategoria(tv, idCategoria, status)


    def ver(self, tv, opcao):
        """

        :param tv:
        :param opcao: identificar a tela a qual será aberta - 1: Visualizacao, 2: Exclusao, 3: Alteração
        :return:
        """
        try:
            items = tv.selection()[0]
            idDocument = (tv.item(items, "values"))[0]
            if opcao == 1:
                Documento().createViewVisualisar(self.app, self.idUsuario, idDocument)
            elif opcao == 2:
                Documento().createViewDelete(self.app, self.idUsuario, idDocument)
        except:
            messagebox.showerror(title="ERRO", message="Por favor, selecione o item que deseja visualizar")

    def addAppCategoriaSituacao(self):

        #Valor após escolher a Categoria
        if self.varCategoria.get() != []:
            idCategoria = Categoria().returnIdCategoria(self.varCategoria.get())
            autor = Categoria().returnAutorCategoria(idCategoria)


        #Valor Padrão da Categoria
        if idCategoria == None:
            idCategoria = 17
            autor = Categoria().returnAutorCategoria(idCategoria)


        # Criação da Aba Dentro aba
        self.fr_ApresentaAba.destroy()
        self.fr_ApresentaAba = Frame(self.fr_Conteudo)
        self.abaSituacao = ttk.Notebook(self.fr_ApresentaAba, padding=2)
        self.fr_ApresentaAba.place(x=25, y=150, width=1000, height=150)
        self.abaSituacao.pack(fill=X, expand=True)

        #Frames da Aba Situacao
        fr_Todos = Frame(self.fr_ApresentaAba)
        fr_Recomendado = Frame(self.fr_ApresentaAba)
        fr_Iniciado = Frame(self.fr_ApresentaAba)
        fr_Finalizado = Frame(self.fr_ApresentaAba)
        fr_FantasmaMemoria = Frame(self.fr_ApresentaAba)


        #Aba Todos
        self.abaSituacao.add(fr_Todos, text="Todos")
        self.addTreView(fr_Todos, autor, "Todos", idCategoria)

        #Aba Recomendado
        self.abaSituacao.add(fr_Recomendado, text="Recomendado")
        self.addTreView(fr_Recomendado, autor, "Recomendado", idCategoria)

        #aba Iniciado
        self.abaSituacao.add(fr_Iniciado, text="Iniciado")
        self.addTreView(fr_Iniciado, autor, "Iniciado", idCategoria)

        #aba Finalizado
        self.abaSituacao.add(fr_Finalizado, text="Finalizado")
        self.addTreView(fr_Finalizado, autor, "Finalizado", idCategoria)

        #aba FantasmaMemoria
        self.abaSituacao.add(fr_FantasmaMemoria, text="Fantasma na Memória")
        self.addTreView(fr_FantasmaMemoria, autor, "Fantasma na Memória", idCategoria)


    def insertValuesOfCategoria(self, abaCategoria, idCategoria, status):

        if status == "Todos":
            print("Aqui")
            if idCategoria == 17:
                #Recuperar os Valores do documento
                sql = "SELECT d.idDocumento, d.titulo, a.nome, d.situacao FROM Documento d " \
                        f"join Autor a on d.idAutor = a.idAutor where idUsuario = '{self.idUsuario}' and situacao != 'Lixeira'; "
            else:
                sql = "SELECT d.idDocumento, d.titulo, a.nome, d.situacao FROM Documento d " \
                      f"join Autor a on d.idAutor = a.idAutor where d.idUsuario = '{self.idUsuario}' and d.idCategoria = '{idCategoria}' and situacao != 'Lixeira';"
        elif status != "Todos":
            print("EStou aqui")
            if idCategoria == 17:
                # Recuperar os Valores do documento
                sql = "SELECT d.idDocumento, d.titulo, a.nome, d.situacao FROM Documento d " \
                      f"join Autor a on d.idAutor = a.idAutor where idUsuario = '{self.idUsuario}' and situacao = '{status}'; "
            else:
                sql = "SELECT d.idDocumento, d.titulo, a.nome, d.situacao FROM Documento d " \
                      f"join Autor a on d.idAutor = a.idAutor where d.idUsuario = '{self.idUsuario}' and d.idCategoria = '{idCategoria}' and situacao = '{status}';"


        itensDocumento = dbSelect(sql)

        for item in itensDocumento:
            sql = f"SELECT g.nome from DocumentoGenero dg join Genero g on dg.idGenero = g.idGenero where dg.idDocumento = {item[0]};"
            listaGenero = ""
            genero = dbSelect(sql)

            for nomeGenero in genero:
                listaGenero += f"- {nomeGenero[0]} "

            abaCategoria.insert("", 'end', values=(item[0],item[1], item[2], listaGenero, item[3]))

        
    def addMenuLateral(self, fr_Menu, tv=""):
        print(tv)
        #Adição dos elementos
        self.btnFecharMenu = Button(fr_Menu, text="|||", background="#8C1018", foreground="#fff", command=self.fecharMenu)
        btnAdicionar = Button(fr_Menu, text="Adicionar", command=lambda:Documento().createViewDocumento("Conteúdo", idUsuario=self.idUsuario))
        btnAlterar = Button(fr_Menu, text="Alterar", command=lambda:Documento().createViewAlteraDoc(self.app, self.idUsuario))
        btnExcluir = Button(fr_Menu, text="Excluir ", command=lambda:Documento().createViewDelete(self.app, self.idUsuario))
        self.btnVisualizar = Button(fr_Menu)
       # btnRelatorio = Button(fr_Menu, text="Gerar Relatório em PDF", command=self.semAcao)
        lblMenuTitulo = Label(fr_Menu, text="Fivros", anchor="center", font=("Arial", 16, "bold"))

        #Configuração das dimensões
        DimeElementMenuLateral(self.btnFecharMenu, lblMenuTitulo, btnAdicionar, btnAlterar, btnExcluir, self.btnVisualizar)


    def abrirMenu(self):
        DimeElementAbrirMenu(self.fr_Menu, self.fr_Conteudo, self.btnAbrirMenu, self.fr_Titulo, self.titulo, self.fr_VisualizarCategoria, self.fr_ApresentaAba)


    def fecharMenu(self):
        DimeElementFecharMenu(self.fr_Menu, self.fr_Principal, self.fr_Conteudo, self.fr_ApresentaAba, self.btnAbrirMenu, self.fr_Titulo, self.fr_VisualizarCategoria)


