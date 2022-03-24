from tkinter import *
from tkinter import ttk
from datetime import date
from Modulos.Autor import Autor
from Modulos.DimensoesTela.DimensaoDocumento import *
from Modulos.Categoria  import *
from Modulos.Genero import Genero


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
        self.createAllAbas()

        # Configuração da posição dos frames
        DimeCreateFrameDocumento(self.fr_Principal, self.fr_Documento, self.fr_Categoria, self.fr_Genero, self.fr_Autor,
                                 self.fr_Status, self.aba)



    def createTelaCadastro(self, app):
        self.appCadastroDoc = Toplevel()
        self.appCadastroDoc.title("Cadastro de Conteúdo")
        self.appCadastroDoc.geometry("500x700")
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

    def createAllAbas(self):
        self.aba.add(self.fr_Documento, text="Obra")
        self.aba.add(self.fr_Categoria, text="Categoria")
        self.aba.add(self.fr_Genero, text="Gênero")
        self.aba.add(self.fr_Autor, text="Autor")
        self.aba.add(self.fr_Status, text="Finalização")

    def addElementFramePrincipal(self, titulo):
        lblTitulo = Label(self.fr_Principal, text=f"CADASTRO DE {titulo.upper()}", anchor="center", font=("Arial", 14))
        btn_Cadastrar = Button(self.fr_Principal, text="Cadastrar", background="#635959", foreground="#F6F6F6")
        DimeElementFramePrincipal(lblTitulo, btn_Cadastrar)

    def addElemenFrameDocumento(self):
        #Criação dos elementos do Frame
        self.lblTitulo = Label(self.fr_Documento, text="Nome da Obra: ", anchor="w", background="#635959", foreground="#fff")
        self.txtTitulo = Entry(self.fr_Documento , borderwidth=1, relief="raised")
        self.lblAnoPublicacao = Label(self.fr_Documento, text="Ano de Publicação: ", anchor="w", background="#635959", foreground="#fff")
        self.txtAnoPublicacao = Entry(self.fr_Documento, borderwidth=1, relief="raised")
        self.fr_Descricao = Frame(self.fr_Documento, relief="raised", borderwidth=1, )
        self.lblDescricao = Label(self.fr_Descricao, text="Sinopse da obra: ", anchor="w", background="#635959", foreground="#fff")
        self.barraLateral1 = Scrollbar(self.fr_Descricao)
        self.txtDescricao = Text(self.fr_Descricao, borderwidth=1, wrap=WORD, undo=True, yscrollcommand=self.barraLateral1.set)

        # Configurar Barra Lateral
        self.barraLateral1.config(command=self.txtDescricao.yview)

        #Configuração das dimensões
        DimeElementFrameDocumento(self.lblTitulo, self.txtTitulo, self.lblAnoPublicacao, self.txtAnoPublicacao, self.fr_Descricao, self.lblDescricao,self.txtDescricao, self.barraLateral1)



    def addElemenFrameCategoria(self, idCategoria):

        #Frame para informar a categoria existente
        fr_TipoCategoria = Frame(self.fr_Categoria, relief="raised", borderwidth=1)
        barraLateral = Scrollbar(fr_TipoCategoria)
        lblItens = Label(fr_TipoCategoria, text="Categoria", anchor="w", background="#635959",font=("Arial", 10), foreground="#f6f6f6")
        self.lb_Itens = Listbox(fr_TipoCategoria, yscrollcommand=barraLateral.set, relief="raised", borderwidth=1)

        #Configurar barra lateral
        barraLateral.config(command=self.lb_Itens.yview)

        #Frame para informar nova categoria
        fr_NovaCategoria = Frame(self.fr_Categoria, background="#D1CDCD")
        val_responsavel = StringVar()

        #Elementos frame Nova Categoria
        lblNome = Label(fr_NovaCategoria, text="Nova Categoria", anchor="w", background="#635959",font=("Arial", 10), foreground="#f6f6f6")
        txtNome = Entry(fr_NovaCategoria, relief="raised", borderwidth=1)
        lblResponsavel = Label(fr_NovaCategoria, text="Indíviduo Responsável", anchor="w", background="#635959",font=("Arial", 10), foreground="#f6f6f6")

        #Frame secundário de Nova Categoria - Radio Button
        fr_ResponsavelButton = Frame(fr_NovaCategoria, relief="raised", borderwidth=1)
        rb_escritor = Radiobutton(fr_ResponsavelButton, text="Escritor", value="ESCRITOR", variable=val_responsavel)
        rb_diretor = Radiobutton(fr_ResponsavelButton, text="Diretor", value="DIRETOR", variable=val_responsavel)

        btnAdicionar = Button(fr_NovaCategoria, text="Adicionar Nova Categoria", command=lambda:Categoria().createNewCategoria(txtNome.get(), val_responsavel.get(), self.lb_Itens))

        #Configurar dimensões do Frame Categoria
        DimeElementFrameCategoria(fr_TipoCategoria, lblItens, self.lb_Itens, barraLateral, fr_NovaCategoria, lblNome, txtNome, lblResponsavel, fr_ResponsavelButton, rb_escritor, rb_diretor, btnAdicionar)

        #Adicionar as opções no ListBox da Categoria
        cat = Categoria()
        cat.addElementListBoxCadastroDoc(self.lb_Itens)


    def addElementFrameGenero(self):

        #Frame para informar o gênero existente
        fr_TipoGenero = Frame(self.fr_Genero, relief="raised", borderwidth=1)
        lblItens = Label(fr_TipoGenero, text="Gênero", anchor="w", background="#635959", font=("Arial", 10),
                         foreground="#f6f6f6")
        barraLateral = Scrollbar(fr_TipoGenero)
        lbItens = Listbox(fr_TipoGenero, yscrollcommand=barraLateral.set, selectmode="multiple")

        # Frame para criação de novo gênero
        fr_NovoGenero = Frame(self.fr_Genero, background="#D1CDCD")
        lblNome = Label(fr_NovoGenero, text="Novo Gênero", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        txtNome = Entry(fr_NovoGenero, relief="raised", borderwidth=1)
        btnAdicionar = Button(fr_NovoGenero, text="Adicionar Novo Gênero", command=lambda:Genero().createNewGenero(txtNome.get(), lbItens))

        #Configurar dimensões da frame Genero
        DimeElementFrameGenero(fr_TipoGenero, lblItens, lbItens, barraLateral, fr_NovoGenero, lblNome, txtNome, btnAdicionar)

        # Configurar Barra Lateral
        barraLateral.config(command=lbItens.yview)

        #Adicionar as opções no ListBox do Genero
        genero = Genero()
        genero.addElementsListBoxGenero(lbItens)

    def addElementAutor(self):
        anoAtual = date.today().year
        fr_TipoAutor = Frame(self.fr_Autor, relief="raised", borderwidth=1)
        lblAutor = Label(fr_TipoAutor, text="Nome dos Responsáveis (Escritor ou Diretor)", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        barraLateral = Scrollbar(fr_TipoAutor)
        lb_Autor = Listbox(fr_TipoAutor, selectmode="multiple", yscrollcommand=barraLateral.set, borderwidth=1, relief="raised")

        fr_NovoAutor = Frame(self.fr_Autor, background="#D1CDCD")
        lblNome = Label(fr_NovoAutor, text="Nome Novo Autor", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        txtNomeAutor = Entry(fr_NovoAutor, borderwidth=1, relief="raised")
        lblPaisOrigem = Label(fr_NovoAutor, text="País de Origem", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        txtPaisOrigem = Entry(fr_NovoAutor, borderwidth=1, relief="raised")

        fr_Biografia = Frame(fr_NovoAutor)
        barraLateral2 = Scrollbar(fr_Biografia)
        lblBiografia = Label(fr_Biografia, text="Biografia", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        txtBiografia = Text(fr_Biografia, borderwidth=1, relief="raised", yscrollcommand=barraLateral2.set, wrap=WORD)
        lblNascimento = Label(fr_NovoAutor, text="Ano de Nascimento", anchor="w", background="#635959", font=("Arial", 10),
                              foreground="#f6f6f6")
        txtNascimento = Spinbox(fr_NovoAutor, relief="raised", from_=-2000, to=anoAtual)
        lblFalescimento = Label(fr_NovoAutor, text="Ano de Falescimento", anchor="w", background="#635959", font=("Arial", 10),
                           foreground="#f6f6f6")
        txtFalescimento = Spinbox(fr_NovoAutor, relief="raised", from_=-2000, to=anoAtual)


        btnAdicionar = Button(fr_NovoAutor, text="Adicionar Novo Responsável", command=lambda:Autor().createNewAutor(txtNomeAutor.get(), txtBiografia.get(1.0, END), txtNascimento.get(), txtFalescimento.get(), txtPaisOrigem.get(), lb_Autor) )

        # Adicionar as opções no ListBox da Categoria
        autor = Autor()
        autor.addElementListBoxAutor(lb_Autor)

        #Configuração Barra Lateral
        barraLateral.config(command=lb_Autor.yview)
        barraLateral2.config(command=txtBiografia.yview)

        #Configuração de Dimensões
        DimeElementFrameAutor(self.fr_Autor, btnAdicionar,fr_TipoAutor, lblAutor, lb_Autor, barraLateral, barraLateral2, fr_NovoAutor, fr_Biografia, lblNome, txtNomeAutor, lblPaisOrigem, txtPaisOrigem, lblNascimento, txtNascimento, lblFalescimento, txtFalescimento, lblBiografia, txtBiografia)


    def addElementStatus(self):
        #Criação dos Elementos
        vStatus = StringVar()
        listaStatus = ["Recomendado", "Iniciado", "Finalizado", "Fantasma na Memória"]
        fr_Status = Frame(self.fr_Status, relief="raised", borderwidth=1)
        lblStatus = Label(fr_Status, text="Status da obra", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
        om_Status = OptionMenu(fr_Status, vStatus, *listaStatus)

        #Criação dos sub-elementos de Observações do Frame Status
        fr_Observacao = Frame(self.fr_Status)
        barraLateral2 = Scrollbar(fr_Observacao)
        lblObservacoes = Label(fr_Observacao, text="Observações: ", anchor="w", background="#635959", foreground="#fff")
        txtObservacoes = Text(fr_Observacao, wrap=WORD, undo=True, yscrollcommand=barraLateral2.set)


        #Criação dos sub-elementos do Frame Status
        fr_StatusData = Frame(self.fr_Status)
        lblDataInicio = Label(fr_StatusData, text="Data Início", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
        txtDataInicio = Entry(fr_StatusData, relief="raised")
        lblDataFim = Label(fr_StatusData, text="Data Conclusão", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
        txtDataFim = Entry(fr_StatusData, relief="raised")
        lblInfo = Label(fr_StatusData, text="Obs: formato da data: dd/mm/aaaa", font=("Arial", 8))

        btnCadastrarBD = Button(self.fr_Status, text="Salvar Informações")


        #Configuração das dimensões
        DimeElementFrameStatus(btnCadastrarBD, fr_Status, lblStatus, om_Status, fr_StatusData, lblDataInicio, txtDataInicio, lblDataFim, txtDataFim, lblInfo,fr_Observacao, barraLateral2, lblObservacoes, txtObservacoes)

        #Configuração das barraLateral
        barraLateral2.config(command=txtObservacoes.yview)














