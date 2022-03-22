from tkinter import *

def DimeCreateFrameDocumento(fr_Principal, fr_Documento, fr_Categoria, fr_Genero, fr_Autor, fr_Status, aba):
    """
    Esta função tem como objetivo configurar as dimensões do método createViewDocumento da classe Documento
    :return:
    """
    aba.place(x=10, y=50, width=460, height=500)
    fr_Principal.place(x=10, y=10, width=480, height=630)
    #fr_Documento.pack()
    #fr_Categoria.place(x=400, y=60, width=380, height=230)
   # fr_Genero.place(x=400, y=305, width=380, height=230)
    #fr_Autor.place(x=790, y=60, width=380, height=230)
    #fr_Status.place(x=790, y=305, width=380, height=230)


def DimeElementFramePrincipal(lblTitulo, btn_Cadastrar):
    lblTitulo.place(x=0, y=10, width=460, height=20)
    # btn_Cadastrar.place(x=20, y=100, width=400, height=40)


def DimeElementFrameDocumento(lblTitulo, txtTitulo,lblAnoPublicacao, txtAnoPublicacao, fr_Descricao, lblDescricao, txtDescricao,
                              barraLateral1, fr_Observacao, lblObservacoes, txtObservacoes, barraLateral2):
    lblTitulo.place(x=10, y=0, width=360, height=20)
    txtTitulo.place(x=10, y=50, width=360, height=20)
    lblAnoPublicacao.place(x=10, y=80, width=360, height=20)
    txtAnoPublicacao.place(x=10, y=100, width=360, height=20)

    # Frame de descrição
    fr_Descricao.place(x=10, y=130, width=360, height=170)
    lblDescricao.place(x=0, y=0, width=360, height=20)
    txtDescricao.place(x=0, y=20, width=340, height=145)
    barraLateral1.pack(side=RIGHT, fill=Y, pady=20)

    # Frame de Observações
    fr_Observacao.place(x=10, y=310, width=360, height=150)
    lblObservacoes.place(x=0, y=0, width=360, height=20)
    txtObservacoes.place(x=0, y=20, width=340, height=125)
    barraLateral2.pack(side=RIGHT, fill=Y, pady=20)