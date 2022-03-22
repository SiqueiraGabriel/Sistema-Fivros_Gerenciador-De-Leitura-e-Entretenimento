from tkinter import *

def DimeCreateFrameDocumento(fr_Principal, fr_Documento, fr_Categoria, fr_Genero, fr_Autor, fr_Status, aba):
    """
    Esta função tem como objetivo configurar as dimensões do método createViewDocumento da classe Documento
    :return:
    """
    aba.place(x=10, y=50, width=460, height=620)
    fr_Principal.place(x=10, y=10, width=480, height=680)


def DimeElementFramePrincipal(lblTitulo, btn_Cadastrar):
    """
    Este método tem como objetivo configurar as dimensões do método ElementFramePrincincipal
    :param lblTitulo: String - título da página de configuração
    :param btn_Cadastrar: botão de cadastro da informação
    :return:
    """
    lblTitulo.place(x=0, y=10, width=460, height=20)
    # btn_Cadastrar.place(x=20, y=100, width=400, height=40)


def DimeElementFrameDocumento(lblTitulo, txtTitulo,lblAnoPublicacao, txtAnoPublicacao, fr_Descricao, lblDescricao, txtDescricao,
                              barraLateral1):
    """
        Este método tem como objetivo configurar as dimensões do método ElementFrameDocuemnto
        :param lblTitulo - título da página
        :return:
        """
    lblTitulo.place(x=10, y=30, width=430, height=20)
    txtTitulo.place(x=10, y=50, width=430, height=20)
    lblAnoPublicacao.place(x=10, y=80, width=430, height=20)
    txtAnoPublicacao.place(x=10, y=100, width=430, height=20)

    # Frame de descrição
    fr_Descricao.place(x=10, y=140, width=430, height=170)
    lblDescricao.place(x=0, y=0, width=430, height=20)
    txtDescricao.place(x=0, y=20, width=410, height=120)
    barraLateral1.pack(side=RIGHT, fill=Y, pady=20)


def DimeElementFrameCategoria(fr_TipoCategoria, lblItens, lb_Itens, barraLateral, fr_NovaCategoria, lblNome, txtNome, lblResponsavel, fr_ResponsavelButton, rb_escritor, rb_diretor, btnAdicionar):
    fr_TipoCategoria.place(x=10, y=30, width=430, height=100)
    lblItens.place(x=0, y=0, width=430, height=20)
    lb_Itens.place(x=0, y=20, width=410, height=120)
    barraLateral.pack(side=RIGHT, pady=20, fill=Y)

    fr_NovaCategoria.place(x=10, y=210, width=430, height=200)
    lblNome.place(x=10, y=10, width=400, height=25)
    txtNome.place(x=10, y=35, width=400, height=25)
    lblResponsavel.place(x=10, y=70, width=400, height=25)

    fr_ResponsavelButton.place(x=10, y=95, width=400, height=25)
    rb_escritor.place(x=10, y=0, width=170, height=20)
    rb_diretor.place(x=120, y=0, width=170, height=20)
    btnAdicionar.place(x=20, y=150, width=380, height=30)

def DimeElementFrameGenero(fr_TipoGenero, lblItens, lbItens, barraLateral, fr_NovoGenero, lblNome, txtNome, btnAdicionar):
    fr_TipoGenero.place(x=10, y=30, width=430, height=110)
    lblItens.place(x=0, y=0, width=430, height=20)
    lbItens.place(x=0, y=20, width=410, height=120)
    barraLateral.pack(side=RIGHT, fill=Y, pady=20)

    fr_NovoGenero.place(x=10, y=210, width=430, height=110)
    lblNome.place(x=10, y=10, width=400, height=20)
    txtNome.place(x=10, y=35, width=400, height=20)
    btnAdicionar.place(x=20, y=70, width=380, height=30)

def DimeElementFrameAutor(fr_Autor, btnAdicionar, fr_TipoAutor, lblAutor, lb_Autor, barraLateral, barraLateral2, fr_NovoAutor, fr_Biografia, lblNome, txtNomeAutor, lblPaisOrigem, txtPaisOrigem, lblNascimento, txtNascimento, lblFalescimento, txtFalescimento, lblBiografia, txtBiografia):
    fr_Autor.place(x=10, y=19, width=340, height=670)
    fr_TipoAutor.place(x=10, y=30, width=430, height=140)
    lblAutor.place(x=0, y=0, width=430, height=20)
    lb_Autor.place(x=0, y=20, width=410, height=120)
    barraLateral.pack(side=RIGHT, fill=Y, pady=0)

    fr_NovoAutor.place(x=10, y=210, width=430, height=370)
    lblNome.place(x=10, y=10, width=400, height=20)
    txtNomeAutor.place(x=10, y=30, width=400, height=20)
    lblPaisOrigem.place(x=10, y=60, width=400, height=20)
    txtPaisOrigem.place(x=10, y=80, width=400, height=20)
    fr_Biografia.place(x=10, y=110, width=400, height=140)
    lblBiografia.place(x=0, y=0, width=400, height=20)
    txtBiografia.place(x=0, y=20, width=380, height=120)
    lblNascimento.place(x=10, y=270, width=190, height=20)
    txtNascimento.place(x=10, y=290, width=190, height=20)
    lblFalescimento.place(x=220, y=270, width=190, height=20)
    txtFalescimento.place(x=220, y=290, width=190, height=20)


    barraLateral2.pack(side=RIGHT, fill=Y, pady=20)

    btnAdicionar.place(x=20, y=330, width=380, height=25)

def DimeElementFrameStatus(btnCadastrarBD, fr_Status, lblStatus, om_Status, fr_StatusData, lblDataInicio, txtDataInicio, lblDataFim, txtDataFim, lblInfo,fr_Observacao, barraLateral2, lblObservacoes, txtObservacoes):
    fr_Status.place(x=10, y=30, width=430, height=50)
    lblStatus.place(x=0, y=0, width=430, height=20)
    om_Status.place(x=0, y=20, width=430, height=30)
    fr_Observacao.place(x=10, y=90, width=430, height=150)
    lblObservacoes.place(x=0, y=0, width=430, height=20)
    txtObservacoes.place(x=0, y=20, width=410, height=125)
    barraLateral2.pack(side=RIGHT, fill=Y, pady=20)


    fr_StatusData.place(x=10, y=260, width=430, height=100)
    lblDataInicio.place(x=0, y=0, width=200, height=20)
    txtDataInicio.place(x=0, y=20, width=200, height=20)
    lblDataFim.place(x=228, y=0, width=200, height=20)
    txtDataFim.place(x=228, y=20, width=200, height=20)
    lblInfo.place(x=10, y=60, width=430, height=10)
    # Frame de Observações

    btnCadastrarBD.place(x=20, y=370, width=400, height=30)