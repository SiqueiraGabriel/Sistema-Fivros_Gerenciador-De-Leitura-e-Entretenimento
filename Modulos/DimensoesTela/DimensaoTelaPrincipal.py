def DimeElemetCriacaoAbas(fr_Conteudo, fr_Menu, fr_VisualizarCategoria, lblCategoria, optMenuCategoria, btnSelecionarCategoria, fr_Titulo, titulo):
    fr_Conteudo.place(x=270, y=10, width=1050, height=600)
    fr_Menu.place(x=10, y=10, width=260, height=670)
    fr_VisualizarCategoria.place(x=500, y=10, width=200, height=120)
    lblCategoria.place(x=0, y=0, width=200, height=20)
    optMenuCategoria.place(x=0, y=20, width=200, height=30)
    btnSelecionarCategoria.place(x=20, y=55, width=160, height=30)
    fr_Titulo.place(x=270, y=10, width=700, height=150)
    titulo.place(x=10, y=0, width=400, height=120)


def DimeElementMenuLateral(btnFecharMenu, lblMenuTitulo, btnAdicionar, btnAlterar, btnExcluir, btnVisualizar, btnRelatorio):
    btnFecharMenu.place(y=10, x=10, width=30, height=30)
    lblMenuTitulo.place(y=10, x=60, width=180, height=30)
    btnAdicionar.place(y=90, x=10, width=240, height=30)
    btnAlterar.place(y=130, x=10, width=240, height=30)
    btnExcluir.place(y=170, x=10, width=240, height=30)
    btnVisualizar.place(y=210, x=10, width=240, height=30)
    btnRelatorio.place(y=250, x=10, width=240, height=30)



def DimeElementAbrirMenu(fr_Menu, fr_Conteudo, btnAbrirMenu, fr_Titulo, titulo, fr_VisualizarCategoria, fr_ApresentaAba):
    fr_Menu.place(width=260)
    fr_Conteudo.place(x=270, width=1050)
    btnAbrirMenu.place(width=0, height=0)

    # ConfiguraçãoTopo
    fr_Titulo.place(x=270, y=10, width=700, height=100)
    titulo.place(x=10, y=0, width=450, height=40)
    fr_VisualizarCategoria.place(x=500, y=10, width=200, height=120)
    fr_ApresentaAba.place(x=25, y=150, width=1000, height=150)


def DimeElementFecharMenu(fr_Menu, fr_Principal, fr_Conteudo, fr_ApresentaAba, btnAbrirMenu, fr_Titulo, fr_VisualizarCategoria):
    fr_Menu.place(width=-10)
    fr_Principal.place(width=1310)
    fr_Conteudo.place(x=10, width=1320)
    fr_ApresentaAba.place(x=25, y=150, width=1275, height=150)
    btnAbrirMenu.place(width=30, height=30)
    fr_Titulo.place(width=1000)
    fr_VisualizarCategoria.place(x=780, y=10, width=200, height=120)
