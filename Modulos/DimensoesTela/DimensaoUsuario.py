def DimeCriarViewLogar(fr_Login, lblTitulo, lblUser, txtUser, lblPassword, txtPassword, btnLogar):
    lblTitulo.place(x=0, y=10, width=270, height=20)
    lblUser.place(x=10, y=50, width=60, height=20)
    txtUser.place(x=80, y=50, width=180, height=20)
    lblPassword.place(x=10, y=80, width=60, height=20)
    txtPassword.place(x=80, y=80, width=180, height=20)
    btnLogar.place(x=20, y=120, width=240, height=40)
    fr_Login.place(y=10, x=10, width=280, height=210)

def DimeCriarViewCadastro(fr_CadastroUser, lblTitulo, lblNome, txtNomeCadastro, lblEmail, txtEmailCadastro, lblSenha, txtSenhaCadastro, lblConfirmSenha, txtConfirmSenhaCadastro, btnCadastrar):
    lblTitulo.place(x=10, y=10, width=360, height=20)
    lblNome.place(x=10, y=50, width=80, height=20)
    txtNomeCadastro.place(x=135, y=50, width=225, height=20)
    lblEmail.place(x=10, y=80, width=80, height=20)
    txtEmailCadastro.place(x=135, y=80, width=225, height=20)
    lblSenha.place(x=10, y=110, width=80, height=20)
    txtSenhaCadastro.place(x=135, y=110, width=225, height=20)
    lblConfirmSenha.place(x=10, y=140, width=125, height=20)
    txtConfirmSenhaCadastro.place(x=135, y=140, width=225, height=20)
    btnCadastrar.place(x=20, y=180, width=340, height=40)
    fr_CadastroUser.place(x=10, y=10, width=380, height=240)