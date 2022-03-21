from tkinter import *


def addElemenFrameDocumento(frame):
    lblLegenda = Label(frame, text="Dados Obra", anchor="w", font=("Arial", 10), foreground="#f6f6f6")
    lblTitulo = Label(frame, text="Nome da Obra: ", anchor="w", background="#635959", foreground="#fff")
    txtTitulo = Entry(frame)
    lblAnoPublicacao = Label(frame, text="Ano de Publicação: ", anchor="w", background="#635959", foreground="#fff")
    txtAnoPublicacao = Entry(frame, borderwidth=1, relief="raised")

    fr_Descricao = Frame(frame, relief="raised", borderwidth=1)
    lblDescricao = Label(fr_Descricao, text="Sinopse da obra: ", anchor="w", background="#635959", foreground="#fff")
    barraLateral1 = Scrollbar(fr_Descricao)
    txtDescricao = Text(fr_Descricao, borderwidth=1, wrap=WORD, undo=True, yscrollcommand=barraLateral1.set)

    fr_Observacao = Frame(frame, relief="raised", borderwidth=1)
    barraLateral2 = Scrollbar(fr_Observacao)
    lblObservacoes = Label(fr_Observacao, text="Observações: ", anchor="w", background="#635959", foreground="#fff")
    txtObservacoes = Text(fr_Observacao, wrap=WORD, undo=True, yscrollcommand=barraLateral2.set)

    lblLegenda.place(x=10, y=10, width=360, height=10)
    lblTitulo.place(x=10, y=30, width=360, height=20)
    txtTitulo.place(x=10, y=50, width=360, height=20)
    lblAnoPublicacao.place(x=10, y=80, width=360, height=20)
    txtAnoPublicacao.place(x=10, y=100, width=360, height=20)

    #Frame de descrição
    fr_Descricao.place(x=10, y=130, width=360, height=170)
    lblDescricao.place(x=0, y=0, width=360, height=20)
    txtDescricao.place(x=0, y=20, width=340, height=145)
    barraLateral1.pack(side=RIGHT, fill=Y, pady=20)

    #Frame de Observações
    fr_Observacao.place(x=10, y=310, width=360, height=150)
    lblObservacoes.place(x=0, y=0, width=360, height=20)
    txtObservacoes.place(x=0, y=20, width=340, height=125)
    barraLateral2.pack(side=RIGHT, fill=Y, pady=20)

    #Configurar Barra Lateral
    barraLateral1.config(command=txtDescricao.yview)
    barraLateral2.config(command=txtObservacoes.yview)


def addElemenFrameCategoria(frame, idCategoria):
    lblLegenda = Label(frame, text="Dados Categoria", anchor="w", font=("Arial", 10), foreground="#f6f6f6")
    fr_TipoCategoria = Frame(frame, relief="raised", borderwidth=1)
    lblItens = Label(fr_TipoCategoria, text="Categoria", anchor="w", background="#635959",font=("Arial", 10), foreground="#f6f6f6")
    barraLateral = Scrollbar(fr_TipoCategoria)
    lbItens = Listbox(fr_TipoCategoria, yscrollcommand=barraLateral)

    fr_NovaCategoria = Frame(frame)
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
    lbItens.place(x=0, y=20, width=340, height=90)
    barraLateral.pack(side=RIGHT, fill=Y, pady=20)
    fr_NovaCategoria.place(x=10, y=130, width=360, height=90)
    lblNome.place(x=0, y=0, width=150, height=25)
    txtNome.place(x=0, y=25, width=150, height=25)
    lblResponsavel.place(x=160, y=0, width=210, height=25)
    fr_ResponsavelButton.place(x=160, y=25, width=200, height=25)
    rb_escritor.place(x=0, y=0, width=80, height=20)
    rb_diretor.place(x=110, y=0, width=80, height=20)
    btnAdicionar.place(x=20, y=65, width=320, height=20)

    #Configurar Barra Lateral
    barraLateral.config(command=lbItens.yview)

    #Deixar item ListBox Marcado
    lbItens.select_set(idCategoria)

def addElementFrameGenero(frame):
    fr_TipoGenero = Frame(frame, relief="raised", borderwidth=1)
    lblItens = Label(fr_TipoGenero, text="Gênero", anchor="w", background="#635959", font=("Arial", 10),
                     foreground="#f6f6f6")
    barraLateral = Scrollbar(fr_TipoGenero)
    lbItens = Listbox(fr_TipoGenero, yscrollcommand=barraLateral)

    fr_NovoGenero = Frame(frame)
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


def addElementAutor(frame):
    fr_Autor = Frame(frame, relief="raised", borderwidth=1)
    lblAutor = Label(fr_Autor, text="Nome dos Responsáveis (Escritor ou Diretor)", anchor="w", background="#635959", font=("Arial", 10),
                    foreground="#f6f6f6")
    barraLateral = Scrollbar(fr_Autor)
    lb_Autor = Listbox(fr_Autor, selectmode="multiple", yscrollcommand=barraLateral)
    btnAdicionar = Button(frame, text="Adicionar Novo Responsável")

    fr_Autor.place(x=10, y=20, width=360, height=140)
    lblAutor.place(x=0,y=0, width=360, height=20)
    lb_Autor.place(x=0, y=20, width=340, height=118)
    barraLateral.pack(side=RIGHT, fill=Y, pady=20)
    btnAdicionar.place(x=20, y=180, width=320, height=25)


def addElementStatus(frame):
    vStatus = StringVar()
    listaStatus = ["Recomendado", "Iniciado", "Finalizado", "Fantasma na Memória"]
    fr_Status = Frame(frame, relief="raised", borderwidth=1)
    lblStatus = Label(fr_Status, text="Status da obra", anchor="w", background="#635959", font=("Arial", 10),
                    foreground="#f6f6f6")
    om_Status = OptionMenu(fr_Status, vStatus, *listaStatus)

    data = StringVar()
    fr_StatusData = Frame(frame, borderwidth=1, relief="raised")
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






def createViewDocumento(titulo, idCategoria=0):
    appCadastroDoc = Tk()
    appCadastroDoc.title("Cadastro de Conteúdo")
    appCadastroDoc.geometry("1200x620")
    appCadastroDoc.resizable(0, 0)
    appCadastroDoc.configure(background="#ddd")

    fr_Principal = Frame(appCadastroDoc, borderwidth=1, relief="raised")
    fr_Principal.place(x=10, y=10, width=1180, height=600)

    lblTitulo = Label(fr_Principal, text=f"CADASTRO DE {titulo.upper()}", anchor="center", font=("Arial", 14))

    fr_Documento = Frame(fr_Principal, borderwidth=1, relief="raised")
    addElemenFrameDocumento(fr_Documento)
    fr_Categoria = LabelFrame(fr_Principal, borderwidth=1, relief="raised")
    addElemenFrameCategoria(fr_Categoria, idCategoria)
    fr_Genero = LabelFrame(fr_Principal, borderwidth=1, relief="raised")
    addElementFrameGenero(fr_Genero)
    fr_Autor = LabelFrame(fr_Principal, borderwidth=1, relief="raised")
    addElementAutor(fr_Autor)
    fr_Status = LabelFrame(fr_Principal, borderwidth=1, relief="raised")
    addElementStatus(fr_Status)
    btn_Cadastrar = Button(fr_Principal, text="Cadastrar", background="#635959", foreground="#F6F6F6")

    lblTitulo.place(x=10, y=10, width=1160, height=20)
    fr_Documento.place(x=10, y=60, width=380, height=470)
    fr_Categoria.place(x=400, y=60, width=380, height=230)
    fr_Genero.place(x=400, y=305, width=380, height=230)
    fr_Autor.place(x=790, y=60, width=380, height=230)
    fr_Status.place(x=790, y=305, width=380, height=230)
    btn_Cadastrar.place(x=20, y=545, width=1120, height=40)

    appCadastroDoc.mainloop()





createViewDocumento("conteúdo")