from tkinter import *


class Usuario:

    def createViewLogar(self):
        appLogin = Tk()
        appLogin.title("Login de Usuários")
        appLogin.configure(background="#ddd")
        appLogin.geometry("300x200")
        appLogin.resizable(0, 0)
        fr_Login = Frame(appLogin, borderwidth=1, relief="ridge")
        lblTitulo = Label(fr_Login, text="LOGIN DE USUÁRIO", font=("Arial", 14), anchor="center")
        lblUser = Label(fr_Login, text="Usuário: ")
        txtUser = Entry(fr_Login)
        lblPassword = Label(fr_Login, text="Senha: ")
        txtPassword = Entry(fr_Login, show="*")
        btnLogar = Button(fr_Login, text="Entrar", background="#635959", foreground="#F6F6F6")

        lblTitulo.place(x=0, y=10, width=270, height=20)
        lblUser.place(x=10, y=50, width=60, height=20)
        txtUser.place(x=80, y=50, width=180, height=20)
        lblPassword.place(x=10, y=80, width=60, height=20)
        txtPassword.place(x=80, y=80, width=180, height=20)
        btnLogar.place(x=20, y=120, width=240, height=40)

        fr_Login.place(y=10, x=10, width=280, height=180)

        appLogin.mainloop()

    def createViewCadastro(self):
        appCadastroUser = Tk()
        appCadastroUser.title("Cadastro de Usuário")
        appCadastroUser.configure(background="#ddd")
        appCadastroUser.geometry("400x260")
        appCadastroUser.resizable(0,0)

        fr_CadastroUser = Frame(appCadastroUser, borderwidth=1, relief="raised")

        lblTitulo = Label(fr_CadastroUser, text="CADASTRO DE USUÁRIO", font=("Arial", 14), anchor="center")
        lblNome = Label(fr_CadastroUser, text="Nome:", anchor="w")
        txtNome = Entry(fr_CadastroUser)
        lblEmail = Label(fr_CadastroUser, text="Email:", anchor="w")
        txtEmail = Entry(fr_CadastroUser)
        lblSenha = Label(fr_CadastroUser, text="Senha", anchor="w")
        txtSenha = Entry(fr_CadastroUser, show="*")
        lblConfirmSenha = Label(fr_CadastroUser, text="Confirmar Senha:", anchor="w")
        txtConfirmSenha = Entry(fr_CadastroUser, show="*")
        btnCadastrar = Button(fr_CadastroUser, text="Cadastrar", background="#635959", foreground="#F6F6F6")

        lblTitulo.place(x=10, y=10, width=360, height=20)
        lblNome.place(x=10, y=50, width=80, height=20)
        txtNome.place(x=135, y=50, width=225, height=20)
        lblEmail.place(x=10, y=80, width=80, height=20)
        txtEmail.place(x=135, y=80, width=225, height=20)
        lblSenha.place(x=10, y=110, width=80, height=20)
        txtSenha.place(x=135, y=110, width=225, height=20)
        lblConfirmSenha.place(x=10, y=140, width=125, height=20)
        txtConfirmSenha.place(x=135, y=140, width=225, height=20)
        btnCadastrar.place(x=20, y=180, width=340, height=40)
        fr_CadastroUser.place(x=10, y=10, width=380, height=240)

        appCadastroUser.mainloop()


user = Usuario()
user.createViewCadastro()
#user.createViewLogar()