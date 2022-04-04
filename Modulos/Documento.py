from tkinter import *
from tkinter import ttk, messagebox
from datetime import date
from Modulos.Autor import Autor
from Modulos.DimensoesTela.DimensaoDocumento import *
from Modulos.ClasseCategoria import *
from Modulos.Genero import Genero
from Modulos.Calendario import *
from Modulos.Banco import *
from Modulos.DocumentoGenero import *
from Modulos.Controller.BD_Documento import *


class Documento:

    def __init__(self):
        self.anoAtual = date.today().year



    def createViewDocumento(self, titulo="Conteúdo", idCategoria=0, app=None, idUsuario=0):
        #Criação da tela de cadastro
        self.createTelaCadastro(app)
        self.idUsuario = idUsuario

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
        self.aba.add(self.fr_Autor, text="Autor")
        self.aba.add(self.fr_Genero, text="Gênero")
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
        self.txtAnoPublicacao = Spinbox(self.fr_Documento, from_=-3000, to=self.anoAtual, borderwidth=1, relief="raised")
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
        self.lb_ItensCategoria = Listbox(fr_TipoCategoria, yscrollcommand=barraLateral.set, relief="raised", borderwidth=1)

        #Configurar barra lateral
        barraLateral.config(command=self.lb_ItensCategoria.yview)

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

        btnAdicionar = Button(fr_NovaCategoria, text="Adicionar Nova Categoria", command=lambda:Categoria().createNewCategoria(txtNome.get(), val_responsavel.get(),  self.lb_ItensCategoria))

        #Configurar dimensões do Frame Categoria
        DimeElementFrameCategoria(fr_TipoCategoria, lblItens, self.lb_ItensCategoria, barraLateral, fr_NovaCategoria, lblNome, txtNome, lblResponsavel, fr_ResponsavelButton, rb_escritor, rb_diretor, btnAdicionar)

        #Adicionar as opções no ListBox da Categoria
        cat = Categoria()
        cat.addElementListBoxCadastroDoc(self.lb_ItensCategoria)


    def addElementFrameGenero(self):

        #Frame para informar o gênero existente
        fr_TipoGenero = Frame(self.fr_Genero, relief="raised", borderwidth=1)
        lblItens = Label(fr_TipoGenero, text="Gênero", anchor="w", background="#635959", font=("Arial", 10),
                         foreground="#f6f6f6")
        barraLateral = Scrollbar(fr_TipoGenero)
        self.lbItensGenero = Listbox(fr_TipoGenero, yscrollcommand=barraLateral.set, selectmode="multiple")

        # Frame para criação de novo gênero
        fr_NovoGenero = Frame(self.fr_Genero, background="#D1CDCD")
        lblNome = Label(fr_NovoGenero, text="Novo Gênero", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        txtNome = Entry(fr_NovoGenero, relief="raised", borderwidth=1)
        btnAdicionar = Button(fr_NovoGenero, text="Adicionar Novo Gênero", command=lambda:Genero().createNewGenero(txtNome.get(), self.lbItensGenero))

        #Configurar dimensões da frame Genero
        DimeElementFrameGenero(fr_TipoGenero, lblItens, self.lbItensGenero, barraLateral, fr_NovoGenero, lblNome, txtNome, btnAdicionar)

        # Configurar Barra Lateral
        barraLateral.config(command=self.lbItensGenero.yview)

        #Adicionar as opções no ListBox do Genero
        genero = Genero()
        genero.addElementsListBoxGenero(self.lbItensGenero)

    def addElementAutor(self):
        fr_TipoAutor = Frame(self.fr_Autor, relief="raised", borderwidth=1)
        lblAutor = Label(fr_TipoAutor, text="Nome do principal Responsável (Escritor ou Diretor)", anchor="w", background="#635959", font=("Arial", 10),
                        foreground="#f6f6f6")
        barraLateral = Scrollbar(fr_TipoAutor)
        self.lb_Autor = Listbox(fr_TipoAutor, yscrollcommand=barraLateral.set, borderwidth=1, relief="raised")

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
        txtNascimento = Spinbox(fr_NovoAutor, relief="raised", from_=-2000, to=self.anoAtual)
        lblFalescimento = Label(fr_NovoAutor, text="Ano de Falescimento", anchor="w", background="#635959", font=("Arial", 10),
                           foreground="#f6f6f6")
        txtFalescimento = Spinbox(fr_NovoAutor, relief="raised", from_=-2000, to=self.anoAtual)


        btnAdicionar = Button(fr_NovoAutor, text="Adicionar Novo Responsável", command=lambda:Autor().createNewAutor(txtNomeAutor.get(), txtBiografia.get(1.0, END), txtNascimento.get(), txtFalescimento.get(), txtPaisOrigem.get(), self.lb_Autor) )

        # Adicionar as opções no ListBox da Categoria
        autor = Autor()
        autor.addElementListBoxAutor(self.lb_Autor)

        #Configuração Barra Lateral
        barraLateral.config(command=self.lb_Autor.yview)
        barraLateral2.config(command=txtBiografia.yview)

        #Configuração de Dimensões
        DimeElementFrameAutor(self.fr_Autor, btnAdicionar,fr_TipoAutor, lblAutor, self.lb_Autor, barraLateral, barraLateral2, fr_NovoAutor, fr_Biografia, lblNome, txtNomeAutor, lblPaisOrigem, txtPaisOrigem, lblNascimento, txtNascimento, lblFalescimento, txtFalescimento, lblBiografia, txtBiografia)


    def addElementStatus(self):
        #Criação dos Elementos
        self.vStatus = StringVar()
        listaStatus = ["Recomendado", "Iniciado", "Finalizado", "Fantasma na Memória"]
        fr_Status = Frame(self.fr_Status, relief="raised", borderwidth=1)
        lblStatus = Label(fr_Status, text="Status da obra", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
        om_Status = OptionMenu(fr_Status, self.vStatus, *listaStatus)

        #Criação dos sub-elementos de Observações do Frame Status
        fr_Observacao = Frame(self.fr_Status)
        barraLateral2 = Scrollbar(fr_Observacao)
        lblObservacoes = Label(fr_Observacao, text="Observações: ", anchor="w", background="#635959", foreground="#fff")
        self.txtObservacoes = Text(fr_Observacao, wrap=WORD, undo=True, yscrollcommand=barraLateral2.set)


        #Criação dos sub-elementos do Frame Status
        fr_StatusData = Frame(self.fr_Status)
        lblDataInicio = Label(fr_StatusData, text="Data Início", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
        self.txtDataInicio = Entry(fr_StatusData, relief="raised")
        btnSelecionar = Button(fr_StatusData, text="Inserir Data", command=lambda:Calendario(fr_StatusData).inserirData(self.txtDataInicio, 1))


        lblDataFim = Label(fr_StatusData, text="Data Conclusão", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
        self.txtDataFim = Entry(fr_StatusData, relief="raised")
        btnSelecionar2 = Button(fr_StatusData, text="Inserir Data", command=lambda:Calendario(fr_StatusData).inserirData(self.txtDataFim, 2))


        btnCadastrarBD = Button(self.fr_Status, text="Salvar Informações", command=self.createNewDocumento)


        #Configuração das dimensões
        DimeElementFrameStatus(btnSelecionar, btnSelecionar2, btnCadastrarBD, fr_Status, lblStatus, om_Status, fr_StatusData, lblDataInicio, self.txtDataInicio, lblDataFim, self.txtDataFim,fr_Observacao, barraLateral2, lblObservacoes, self.txtObservacoes)

        #Configuração das barraLateral
        barraLateral2.config(command=self.txtObservacoes.yview)


    def createNewDocumento(self):
        if self.idUsuario == 0:
            messagebox.showerror(title="Usuário Não Cadastrado", message="Para realizar a publicação de um conteúdo é necessário estar logado.")
            self.appCadastroDoc.destroy()
        else:
            idUsuario = self.idUsuario
            titulo = self.txtTitulo.get()
            descricao = self.txtDescricao.get(1.0, END)
            anoPublicacao = self.txtAnoPublicacao.get()
            idCategoria = Categoria().returnIdCategoria(self.lb_ItensCategoria.get(ACTIVE))
            observacao = self.txtObservacoes.get(1.0, END)
            dataInicio = self.txtDataInicio.get()
            dataFim = self.txtDataFim.get()
            situacao = self.vStatus.get()
            generosSelecionados = [self.lbItensGenero.get(i) for i in self.lbItensGenero.curselection()]
            idAutor = Autor().returnIdCategoria(self.lb_Autor.get(ACTIVE))

            if titulo == "" or descricao == "" or situacao == "":
                messagebox.showerror(title="Erro Cadastro Documento", message="Por favor, verifique os valores informados!\n Legenda: * (obrigatório preenchimento)")
            else:
                if anoPublicacao == "-3000":
                    messagebox.showerror(title="Erro Cadastro Documento", message=f"Por favor, verifique os valores informado no campo Ano de Publicação!\nIntervalo disponível de -2999 (A.c) - {self.anoAtual}")
                else:
                    if idCategoria == 17 or idAutor == 10:
                        messagebox.showerror(title="Erro Cadastro Documento", message="Por favor, informe a categoria e autor da qual o Documento pertence.")
                    else:
                        if generosSelecionados == []:
                            messagebox.showerror(title="Erro Cadastro Documento", message="Por favor, verifique os valores informado em Gênero.\nObs: Em relação ao Autor e Categoria, o Gênero deve ser o último a ser marcado.")
                        else:
                            sqlInstrucao = "INSERT INTO Documento(titulo, descricao, dataInicio, dataTermino, anoPublicacao, observacoes, situacao, idAutor, idCategoria, idUsuario) values(?,?,?,?,?,?,?,?,?, ?);"
                            sqlParametros = (titulo, descricao, dataInicio, dataFim, anoPublicacao, observacao, situacao, idAutor, idCategoria, idUsuario)
                            dbInsert(sqlInstrucao, sqlParametros)
                            
                            #Recuperar ID do Documento
                            sql = f"SELECT idDocumento FROM Documento where titulo = '{titulo}' and idUsuario = '{idUsuario}';"
                            idDocumento = dbSelect(sql)[0][0]

                            #Adicionar as categorias do Documento
                            DocumentoGenero().createNewDocumentoGenero(idDocumento, generosSelecionados)
                            
                            messagebox.showinfo(title="Sucesso Cadastro Documento", message="Documento cadastrado com sucesso!")
                            self.appCadastroDoc.destroy()

    def createTelaAlteracao(self, app):
        self.appAlteraDoc = Toplevel()
        self.appAlteraDoc.title("Alteração de Conteúdo")
        self.appAlteraDoc.geometry("500x720")
        self.appAlteraDoc.resizable(0,0)
        self.appAlteraDoc.configure(background="#ddd")
        self.appAlteraDoc.transient(app)



    def createViewAlteraDoc(self, app, idUsuario = 0, idDocumento=0):
        self.createTelaAlteracao(app)
        self.idUsuario = idUsuario

        if idUsuario != 0:
            #Criar o Frame Principal da Tela de Alterações
            fr_Alteracao = Frame(self.appAlteraDoc, borderwidth=1, relief="raised")

            lblTitulo = Label(fr_Alteracao, text="ALTERAÇÃO DE CONTEÙDO", anchor="center", font=("Arial", 14))

            #Elementos relacionado a alteração do Conetúdo

            #Consulta no DB, todos Documento
            listaDocumento = []
            sql = f"SELECT titulo from Documento where idUsuario = '{self.idUsuario}' and situacao != 'Lixeira'"
            result = dbSelect(sql)

            for item in result:
                listaDocumento.append(item[0])

            self.varDocumentoSelecionado = StringVar()

            lblDocumentoSelecionado = Label(fr_Alteracao, text="Identificar Documento para alteração", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            self.documentoAlterar = OptionMenu(fr_Alteracao, self.varDocumentoSelecionado, *listaDocumento)
            btnDocumentoEscolhido = Button(fr_Alteracao, text="Selecionar", command=lambda:self.createViewAltera(BD_Documento().searchIdDocument(name=self.varDocumentoSelecionado.get())))


            self.fr_ElementUpdate = Frame(fr_Alteracao, borderwidth=1, relief="raised")


            fr_Alteracao.place(x=10, y=10, width=480, height=700)
            lblTitulo.place(x=0, y=10, width=460, height=20)
            lblDocumentoSelecionado.place(x=10, y=60, width=460, height=20)
            self.documentoAlterar.place(x=10, y=80, width=460, height=30)
            btnDocumentoEscolhido.place(x=20, y=120, width=440, height=25)

    def createViewAltera(self, idDocumento=0):

        if idDocumento == None:
            messagebox.showerror(title="ERRO Alteração Documento", message="Por favor, selecione o documento que deseja realizar as alterações!")
        else:

            #Campo de Situacao
            listaStatus = ["Recomendado", "Iniciado", "Finalizado", "Fantasma na Memória"]
            varStatus = StringVar()
            lblAlteraStatus = Label(self.fr_ElementUpdate, text="Status da Obra",  anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            om_alteraStatus = OptionMenu(self.fr_ElementUpdate, varStatus, *listaStatus)

            # Campo Observações
            fr_ObservacaoAltera = Frame(self.fr_ElementUpdate)
            lblAlteraObservacao = Label(fr_ObservacaoAltera, text="Observações", anchor="w", background="#635959", font=("Arial", 10), foreground="#f6f6f6")
            barraLateralObservacao = Scrollbar(fr_ObservacaoAltera)
            txtAlteraObservacao = Text(fr_ObservacaoAltera, wrap=WORD, undo=True, yscrollcommand=barraLateralObservacao.set)



            # Configurar Barra LAteral
            barraLateralObservacao.config(command=txtAlteraObservacao.yview)

            #Campos de Data
            fr_alteraData = Frame(self.fr_ElementUpdate)
            lblAlteraDataInicio = Label(fr_alteraData, text="Data Início", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            self.txtAlteraDataInicio = Entry(fr_alteraData, relief="raised")
            btnSelecionar = Button(fr_alteraData, text="Inserir Data", command=lambda: Calendario(fr_alteraData).inserirData(self.txtAlteraDataInicio, 1))

            lblAlteraDataFim = Label(fr_alteraData, text="Data Conclusão", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            self.txtAlteraDataFim = Entry(fr_alteraData, relief="raised")
            btnSelecionar2 = Button(fr_alteraData, text="Inserir Data", command=lambda: Calendario(fr_alteraData).inserirData(self.txtAlteraDataFim, 2))


            btnAlterarDados = Button(self.fr_ElementUpdate, text="Salvar Modificações", command=lambda:BD_Documento().updateDocument(idDocumento, varStatus.get(), self.txtAlteraDataInicio.get(), self.txtAlteraDataFim.get(), txtAlteraObservacao.get(1.0, END), self.appAlteraDoc))

            #Recuperar os valores do BD
            dadosCadastrados = BD_Documento().returnAllUpdateDocument(idDocumento)
            varStatus.set(dadosCadastrados[0])
            txtAlteraObservacao.delete(1.0, END)
            txtAlteraObservacao.insert(1.0, dadosCadastrados[1])
            self.txtAlteraDataInicio.insert(1, dadosCadastrados[2])
            self.txtAlteraDataFim.insert(1, dadosCadastrados[3])







            self.fr_ElementUpdate.place(x=10, y=170, width=460, heigh=520)
            lblAlteraStatus.place(x=10, y=10, width=440, height=20)
            om_alteraStatus.place(x=10, y=30, width=440, height=25)
            fr_ObservacaoAltera.place(x=10, y=70, width=440, height= 120)
            lblAlteraObservacao.place(x=0, y=0, width=440, height=20)
            txtAlteraObservacao.place(x=0, y=20, width=420, height=100)
            barraLateralObservacao.pack(side=RIGHT, fill=Y, pady=20)

            fr_alteraData.place(x=10, y=200, width=440, height=270)
            lblAlteraDataInicio.place(x=0, y=0, width=200, height=20)
            self.txtAlteraDataInicio.place(x=0, y=20, width=200, height=20)
            btnSelecionar.place(x=20, y=45, width=160, height=25)

            lblAlteraDataFim.place(x=228, y=0, width=200, height=20)
            self.txtAlteraDataFim.place(x=228, y=20, width=200, height=20)
            btnSelecionar2.place(x=248, y=45, width=160, height=25)

            btnAlterarDados.place(x=20, y=480, width=420, height=30)

    def createTelaDelete(self, app):
        self.appDeleteDoc = Toplevel()
        self.appDeleteDoc.title("Exclusão de Conetúdo")
        self.appDeleteDoc.geometry("400x250")
        self.appDeleteDoc.resizable(0,0)
        self.appDeleteDoc.configure(background="#ddd")
        self.appDeleteDoc.transient(app)


    def createViewDelete(self, app, idUsuario, idDocumento=0):
        self.createTelaDelete(app)
        self.idUsuario = idUsuario

        fr_Principal = Frame(self.appDeleteDoc)
        txtTitulo = Label(fr_Principal, text="EXCLUSÃO DE CONTEÚDO", anchor="center", font=("Arial", 14))

        # Consulta no DB, todos Documento
        listaDocumento = []
        sql = f"SELECT titulo from Documento where idUsuario = '{self.idUsuario}' and situacao != 'Lixeira'"
        result = dbSelect(sql)

        for item in result:
            listaDocumento.append(item[0])

        self.varDocumentoSelecionado = StringVar()

        lblDocumentoSelecionado = Label(fr_Principal, text="Identificar Documento para exclusão", anchor="w",background="#635959", font=("Arial", 10), foreground="#f6f6f6")
        self.documentoExcluir = OptionMenu(fr_Principal, self.varDocumentoSelecionado, *listaDocumento)
        btnDocumentoExcluir = Button(fr_Principal, text="Selecionar", command=lambda:BD_Documento().deleteDocument(BD_Documento().searchIdDocument(self.varDocumentoSelecionado.get()), self.appDeleteDoc))

        fr_Principal.place(x=10, y=10, width=380, height=230)
        txtTitulo.place(x=0, y=10, width=380, height=20)
        lblDocumentoSelecionado.place(x=10, y=100, width=360, height=20)
        self.documentoExcluir.place(x=10, y=120, width=360, height=30)
        btnDocumentoExcluir.place(x=20, y=170, width=320, height=30)




    def createViewVisualisar(self,app, idUsuario, idDocumento=0):



        if idDocumento != 0:
            appTelaVisu = Toplevel()
            appTelaVisu.config(background="#ddd")
            appTelaVisu.geometry("500x650")
            appTelaVisu.resizable(0, 0)
            appTelaVisu.transient(app)

            #Criação dos elementos principais
            fr_Principal = Frame(appTelaVisu, borderwidth=1, relief="raised")
            fr_Cabecalho = Frame(fr_Principal)
            fr_Sinopse = Frame(fr_Principal)
            fr_Caracteristicas = Frame(fr_Principal)
            fr_Observacao = Frame(fr_Principal)

            #Itens do Frame Cabecalho
            fr_Icone = Frame(fr_Cabecalho, borderwidth=1, relief="raised", background="#323232")
            lblTitulo = Label(fr_Cabecalho, text="Título da Obra", anchor="center", font=("Arial", 12, "bold"))
            lblDescricao = Label(fr_Cabecalho, text=f"Autor - Data Publicação", anchor="center", font=("Arial", 9))

            #Itens do Frame Sinopse
            txtSinopse = Label(fr_Sinopse, text="Sinopse", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            barraLateralSinopse = Scrollbar(fr_Sinopse)
            lblSinopse = Text(fr_Sinopse, state="disabled", wrap=WORD, yscrollcommand=barraLateralSinopse.set, borderwidth=1, relief="raised")
            barraLateralSinopse.config(command=lblSinopse.yview)

            #Itens do Frame Caracteristicas
            lblCategoria = Label(fr_Caracteristicas, text="Categoria", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            txtCategoria = Label(fr_Caracteristicas, text="Livro", background="#fff", borderwidth=1, relief="raised", anchor="center")
            lblGenero = Label(fr_Caracteristicas, text="Gênero",  anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            txtGenero = Label(fr_Caracteristicas, text="Aventura, Ficção", background="#fff", borderwidth=1, relief="raised", anchor="center")
            lblSituacao = Label(fr_Caracteristicas, text="Situação", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            txtSituacao = Label(fr_Caracteristicas, text="Finalizado", background="#fff", borderwidth=1, relief="raised", anchor="center")


            #Itens do Frane Observações
            barraLateralObservacao = Scrollbar(fr_Observacao, borderwidth=1, relief="solid")
            txtObservacao = Label(fr_Observacao, text="Observações", anchor="w", background="#635959", font=("Arial", 10),foreground="#f6f6f6")
            lblObservacao = Text(fr_Observacao, state="disabled", wrap=WORD, yscrollcommand=barraLateralObservacao.set, borderwidth=1, relief="raised")
            barraLateralObservacao.config(command=lblSinopse.yview)


            fr_Principal.place(x=10, y=10, width=480, height=630)
            #------------------------------------------------------
            fr_Cabecalho.place(x=0, y=10, width=460, height=180)
            fr_Icone.place(x=180, y=0, width=100, height=120)
            lblTitulo.place(x=0, y=130, width=460, height=20)
            lblDescricao.place(x=0, y=160, width=460, height=20)
            #------------------------------------------------------
            fr_Sinopse.place(x=10, y=200, width=440, height=120)
            txtSinopse.place(x=0, y=0, width=440, height=20)
            lblSinopse.place(x=0, y=20, width=420, height=100)
            barraLateralSinopse.pack(fill=Y, side="right", pady=20)
            #----------------------------------------------
            fr_Caracteristicas.place(x=10, y=350, width=440, height=100)
            lblCategoria.place(x=0, y=0, width=210, height=20)
            txtCategoria.place(x=0, y=20, width=210, height=30)
            lblGenero.place(x=220, y=0, width=220, height=20)
            txtGenero.place(x=220, y=20, width=220, height=30)
            lblSituacao.place(x=0, y=60, width=440, height=20)
            txtSituacao.place(x=0, y=80, width=440, height=20)
            #------------------------------------------------------
            fr_Observacao.place(x=10, y=470, width=440, height=120)
            txtObservacao.place(x=0, y=0, width=440, height=20)
            lblObservacao.place(x=0, y=20, width=420, height=100)
            barraLateralObservacao.pack(fill=Y, side="right", pady=20)
