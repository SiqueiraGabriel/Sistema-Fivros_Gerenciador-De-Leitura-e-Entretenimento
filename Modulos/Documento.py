from tkinter import *
from tkinter import ttk
from Modulos.DimensoesTela.DimensaoDocumento import *

class Documento:

    def __init__(self):
        print()


    def createViewDocumento(self, titulo="Conteúdo", idCategoria=0, app=None):
        #Criação da tela de cadastro
        self.createTelaCadastro(app)

        #Criação do Frame Principal
        self.fr_Principal = Frame(self.appCadastroDoc, borderwidth=1, relief="raised")

        #Criação do Notebook
        self.aba = ttk.Notebook(self.fr_Principal)

        #Adição dos frames
        self.createAllFrames()

        #Adição dos elementos do Frame
        self.addAllElement(titulo, idCategoria)

        #Criação das abas principais
        self.aba.add(self.fr_Documento, text="Obra")
        self.aba.add(self.fr_Categoria, text="Categoria")
        self.aba.add(self.fr_Genero, text="Gênero")
        self.aba.add(self.fr_Autor, text="Autor")
        self.aba.add(self.fr_Status, text="Status")

        # Configuração da posição dos frames
        DimeCreateFrameDocumento(self.fr_Principal, self.fr_Documento, self.fr_Categoria, self.fr_Genero, self.fr_Autor,
                                 self.fr_Status, self.aba)



    def createTelaCadastro(self, app):
        self.appCadastroDoc = Toplevel()
        self.appCadastroDoc.title("Cadastro de Conteúdo")
        self.appCadastroDoc.geometry("500x650")
        self.appCadastroDoc.resizable(0, 0)
        self.appCadastroDoc.configure(background="#ddd")
        self.appCadastroDoc.transient(app)


    def createAllFrames(self):
        self.fr_Documento = Frame(self.aba, borderwidth=1, relief="raised")
        self.fr_Categoria = LabelFrame(self.aba, borderwidth=1, relief="raised")
        self.fr_Genero = LabelFrame(self.aba, borderwidth=1, relief="raised")
        self.fr_Autor = LabelFrame(self.aba, borderwidth=1, relief="raised")
        self.fr_Status = LabelFrame(self.aba, borderwidth=1, relief="raised")

    def addAllElement(self, titulo, idCategoria):
        self.addElementFramePrincipal(titulo)
        self.addElemenFrameDocumento()
        self.addElemenFrameCategoria(idCategoria)
        self.addElementFrameGenero()
        self.addElementAutor()
        self.addElementStatus()

    def addElementFramePrincipal(self, titulo):
        lblTitulo = Label(self.fr_Principal, text=f"CADASTRO DE {titulo.upper()}", anchor="center", font=("Arial", 14))
        btn_Cadastrar = Button(self.fr_Principal, text="Cadastrar", background="#635959", foreground="#F6F6F6")
        DimeElementFramePrincipal(lblTitulo, btn_Cadastrar)

    def addElemenFrameDocumento(self):
        self.lblTitulo = Label(self.fr_Documento, text="Nome da Obra: ", anchor="w", background="#635959", foreground="#fff")
        self.txtTitulo = Entry(self.fr_Documento)
        self.lblAnoPublicacao = Label(self.fr_Documento, text="Ano de Publicação: ", anchor="w", background="#635959", foreground="#fff")
        self.txtAnoPublicacao = Entry(self.fr_Documento, borderwidth=1, relief="raised")

        self.fr_Descricao = Frame(self.fr_Documento, relief="raised", borderwidth=1, )
        self.lblDescricao = Label(self.fr_Descricao, text="Sinopse da obra: ", anchor="w", background="#635959", foreground="#fff")
        self.barraLateral1 = Scrollbar(self.fr_Descricao)
        self.txtDescricao = Text(self.fr_Descricao, borderwidth=1, wrap=WORD, undo=True, yscrollcommand=self.barraLateral1.set)

        self.fr_Observacao = Frame(self.fr_Documento, relief="raised", borderwidth=1)
        self.barraLateral2 = Scrollbar(self.fr_Observacao)
        self.lblObservacoes = Label(self.fr_Observacao, text="Observações: ", anchor="w", background="#635959", foreground="#fff")
        self.txtObservacoes = Text(self.fr_Observacao, wrap=WORD, undo=True, yscrollcommand=self.barraLateral2.set)

        DimeElementFrameDocumento(self.lblTitulo, self.txtTitulo, self.lblAnoPublicacao, self.txtAnoPublicacao, self.fr_Descricao, self.lblDescricao,self.txtDescricao, self.barraLateral1, self.fr_Observacao, self.lblObservacoes, self.txtObservacoes, self.barraLateral2)

        #Configurar Barra Lateral
        self.barraLateral1.config(command=self.txtDescricao.yview)
        self.barraLateral2.config(command=self.txtObservacoes.yview)

    def addElemenFrameCategoria(self, idCategoria):
        lblLegenda = Label(self.fr_Categoria, text="Dados Categoria", anchor="w", font=("Arial", 10), foreground="#f6f6f6")
        fr_TipoCategoria = Frame(self.fr_Categoria, relief="raised", borderwidth=1)
        lblItens = Label(fr_TipoCategoria, text="Categoria", anchor="w", background="#635959",font=("Arial", 10), foreground="#f6f6f6")
        listaCategoria = ["Ex1", "Ex2"]
        varCategoria = StringVar()
        om_categoria = OptionMenu(fr_TipoCategoria, varCategoria, *listaCategoria)

        fr_NovaCategoria = Frame(self.fr_Categoria)
        lblNome = Label(fr_NovaCategoria, text="Nova Categoria", anchor="w", background="#635959",font=("Arial", 10), foreground="#f6f6f6")
        txtNome = Entry(fr_NovaCategoria, relief="raised", borderwidth=1)

        val_responsavel = StringVar()
        lblResponsavel = Label(fr_NovaCategoria, text="Indíviduo Responsável", anchor="w", background="#635959",font=("Arial", 10), foreground="#f6f6f6")
        fr_ResponsavelButton = Frame(fr_NovaCategoria, relief="raised", borderwidth=1)
        rb_escritor = Radiobutton(fr_ResponsavelButton, text="Escritor", value="ESCRITOR", variable=val_responsavel)
        rb_diretor = Radiobutton(fr_ResponsavelButton, text="Diretor", value="DIRETOR", variable=val_responsavel)

        btnAdicionar = Button(fr_NovaCategoria, text="Adicionar Nova Categoria")

        lblLegenda.place(x=10, y=10, width=360, height=20)
        fr_TipoCategoria.place(x=10, y=30, width=360, height=90)
        lblItens.place(x=0, y=0, width=360, height=20)
        om_categoria.place(x=0, y=20, width=340, height=90)
        fr_NovaCategoria.place(x=10, y=130, width=360, height=90)
        lblNome.place(x=0, y=0, width=150, height=25)
        txtNome.place(x=0, y=25, width=150, height=25)
        lblResponsavel.place(x=160, y=0, width=210, height=25)
        fr_ResponsavelButton.place(x=160, y=25, width=200, height=25)
        rb_escritor.place(x=0, y=0, width=80, height=20)
        rb_diretor.place(x=110, y=0, width=80, height=20)
        btnAdicionar.place(x=20, y=65, width=320, height=20)


        #Deixar item ListBox Marcado
        #om_categoria.select_set(idCategoria)

    def addElementFrameGenero(self):
        fr_TipoGenero = Frame(self.fr_Genero, relief="raised", borderwidth=1)
        lblItens = Label(fr_TipoGenero, text="Gênero", anchor="w", background="#635959", font=("Arial", 10),
                         foreground="#f6f6f6")
        barraLateral = Scrollbar(fr_TipoGenero)
        lbItens = Listbox(fr_TipoGenero, yscrollcommand=barraLateral)

        fr_NovoGenero = Frame(self.fr_Genero)
        lblNome = Label(fr_NovoGenero, text="Novo Gênero", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        txtNome = Entry(fr_NovoGenero, relief="raised", borderwidth=1)


        btnAdicionar = Button(fr_NovoGenero, text="Adicionar Novo Gênero")

        fr_TipoGenero.place(x=10, y=10, width=360, height=110)
        lblItens.place(x=0, y=0, width=360, height=20)
        lbItens.place(x=0, y=20, width=340, height=70)
        barraLateral.pack(side=RIGHT, fill=Y, pady=20)
        fr_NovoGenero.place(x=10, y=110, width=360, height=90)
        lblNome.place(x=0, y=0, width=360, height=20)
        txtNome.place(x=0, y=25, width=360, height=20)
        btnAdicionar.place(x=20, y=55, width=320, height=25)

        # Configurar Barra Lateral
        barraLateral.config(command=lbItens.yview)

    def addElementAutor(self):
        fr_Autor = Frame(self.fr_Autor, relief="raised", borderwidth=1)
        lblAutor = Label(fr_Autor, text="Nome dos Responsáveis (Escritor ou Diretor)", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        barraLateral = Scrollbar(fr_Autor)
        lb_Autor = Listbox(fr_Autor, selectmode="multiple", yscrollcommand=barraLateral)
        btnAdicionar = Button(self.fr_Autor, text="Adicionar Novo Responsável")

        fr_Autor.place(x=10, y=20, width=360, height=140)
        lblAutor.place(x=0,y=0, width=360, height=20)
        lb_Autor.place(x=0, y=20, width=340, height=118)
        barraLateral.pack(side=RIGHT, fill=Y, pady=20)
        btnAdicionar.place(x=20, y=180, width=320, height=25)

    def addElementStatus(self):
        vStatus = StringVar()
        listaStatus = ["Recomendado", "Iniciado", "Finalizado", "Fantasma na Memória"]
        fr_Status = Frame(self.fr_Status, relief="raised", borderwidth=1)
        lblStatus = Label(fr_Status, text="Status da obra", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        om_Status = OptionMenu(fr_Status, vStatus, *listaStatus)

        data = StringVar()
        fr_StatusData = Frame(self.fr_Status, borderwidth=1, relief="raised")
        lblDataInicio = Label(fr_StatusData, text="Data Início", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        txtDataInicio = Entry(fr_StatusData, relief="raised")
        lblDataFim = Label(fr_StatusData, text="Data Conclusão", anchor="w", background="#635959", font=("Arial", 10),
                              foreground="#f6f6f6")
        txtDataFim = Entry(fr_StatusData, relief="raised")
        lblInfo = Label(fr_StatusData, text="Obs: formato da data: dd/mm/aaaa", font=("Arial", 8))


        fr_Status.place(x=10, y=10, width=360, height=50)
        lblStatus.place(x=0,y=0, width=360, height=20)
        om_Status.place(x=0, y=20, width=360, height=30)
        fr_StatusData.place(x=10, y=70, width=360, height=100)
        lblDataInicio.place(x=0, y=0, width=175, height=20)
        txtDataInicio.place(x=0, y=20, width=175, height=20)
        lblDataFim.place(x=185, y=0, width=175, height=20)
        txtDataFim.place(x=185, y=20, width=175, height=20)
        lblInfo.place(x=10, y=60, width=360, height=10)












