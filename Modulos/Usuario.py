from tkinter import *
from tkinter import messagebox
from Modulos.DimensoesTela.DimensaoUsuario import *
from Modulos.Banco import *
from Modulos.TelaPrincipal import TelaPrincipal


class Usuario:

    def __init__(self):
        self.idUsuario = ""
        self.nome = ""
        self.email = ""
        self.senha = ""
        self.admin = None
        self.logado = False


    def createViewLogar(self, app):
        appLogin = Toplevel()
        appLogin.title("Login de Usuários")
        appLogin.configure(background="#ddd")
        appLogin.geometry("300x230")
        appLogin.resizable(0, 0)
        appLogin.transient(app)
        appLogin.focus_force()
        appLogin.grab_set()

        fr_Login = Frame(appLogin, borderwidth=1, relief="ridge")

        #Elementos da Tela de Login
        lblTitulo = Label(fr_Login, text="LOGIN DE USUÁRIO", font=("Arial", 14), anchor="center")
        lblUser = Label(fr_Login, text="Usuário: ")
        self.txtUserLogin = Entry(fr_Login)
        lblPassword = Label(fr_Login, text="Senha: ")
        self.txtPasswordLogin = Entry(fr_Login, show="*")
        btnLogar = Button(fr_Login, text="Entrar", background="#635959", foreground="#F6F6F6", command=lambda:self.logar(appLogin, app))
        self.btnCadastro = Button(fr_Login, text="Cadastrar-se agora", background="#635959", foreground="#F6F6F6", command=lambda:self.createViewCadastro(appLogin))


        DimeCriarViewLogar(fr_Login, lblTitulo, lblUser, self.txtUserLogin, lblPassword, self.txtPasswordLogin, btnLogar)

    def createViewCadastro(self, app):
        appCadastroUser = Toplevel()
        appCadastroUser.title("Cadastro de Usuário")
        appCadastroUser.configure(background="#ddd")
        appCadastroUser.geometry("400x250")
        appCadastroUser.resizable(0,0)
        appCadastroUser.transient(app)

        fr_CadastroUser = Frame(appCadastroUser, borderwidth=1, relief="raised")

        lblTitulo = Label(fr_CadastroUser, text="CADASTRO DE USUÁRIO", font=("Arial", 14), anchor="center")
        lblNome = Label(fr_CadastroUser, text="Nome:", anchor="w")
        self.txtNomeCadastro = Entry(fr_CadastroUser)
        lblEmail = Label(fr_CadastroUser, text="Email:", anchor="w")
        self.txtEmailCadastro = Entry(fr_CadastroUser)
        lblSenha = Label(fr_CadastroUser, text="Senha", anchor="w")
        self.txtSenhaCadastro = Entry(fr_CadastroUser, show="*")
        lblConfirmSenha = Label(fr_CadastroUser, text="Confirmar Senha:", anchor="w")
        self.txtConfirmSenhaCadastro = Entry(fr_CadastroUser, show="*")
        btnCadastrar = Button(fr_CadastroUser, text="Cadastrar", background="#635959", foreground="#F6F6F6", command=lambda:self.cadastrar(appCadastroUser, app))

        DimeCriarViewCadastro(fr_CadastroUser, lblTitulo, lblNome, self.txtNomeCadastro, lblEmail, self.txtEmailCadastro, lblSenha, self.txtSenhaCadastro, lblConfirmSenha, self.txtConfirmSenhaCadastro, btnCadastrar)



    def cadastrar(self, appCadastro, app):
        if self.txtNomeCadastro.get() == "" or self.txtEmailCadastro.get() == "":
            messagebox.showerror(title="Erro Cadastro", message="Pro favor, preencha corretamente os campos!")
        else:
            if self.txtSenhaCadastro.get() != self.txtConfirmSenhaCadastro.get():
                messagebox.showerror(title="Erro no Cadastro", message="Senha não coinicidem. Por favor, verifique os valores informado!")
            else:
                #Verificar se o email já foi cadastrado no sistema
                sqlVerificaSenha = f"SELECT * FROM Usuario where email = '{self.txtEmailCadastro.get()}';"
                result = dbSelect(sqlVerificaSenha)
                if result != []:
                    messagebox.showerror(title="Erro no Cadastro", message="Email já cadastrado. Por favor, informe um novo email ou tente recuperar sua senha!")
                else:
                    nome = self.txtNomeCadastro.get()
                    email = self.txtEmailCadastro.get()
                    senha = self.txtSenhaCadastro.get()
                    sqlPt1 = """INSERT INTO Usuario(nome, email, senha) values(?, ?, ?);"""
                    sqlPt2 = (nome, email, senha)
                    dbManipulation(sqlPt1, sqlPt2)
                    messagebox.showinfo(title="Sucesso Cadastro", message="Seu cadastro foi realizado com sucesso.\n Você agora será redirecionado para tela de Login")
                    self.createViewLogar(app)
                    appCadastro.destroy()



    def logar(self, appLogin, app):
        app.update()
        if self.txtUserLogin.get() == "" or self.txtPasswordLogin.get() == "":
            messagebox.showerror(title="Erro Login", message="Por favor, preencha corretamente os campos !")
        else:
            nome = self.txtUserLogin.get()
            senha = self.txtPasswordLogin.get()
            sql = f"SELECT * FROM Usuario WHERE nome = '{nome}' and senha = '{senha}';"

            result = dbSelect(sql)
            if result == []:
                messagebox.showerror(title="Erro Login", message="Usuário não cadastrado! Por favor, realize seu cadastro clicando no botão Cadastre-se...")
                self.btnCadastro.place(x=20, y=180, width=240, height=20)
            else:
                self.idUsuario = result[0][0]
                self.nome = result[0][1]
                self.email = result[0][2]
                #self.senha = result[0][3]
                self.admin = result[0][4]
                self.logado = True
                print(self.logado)
                messagebox.showinfo(title="Sucesso Login", message="Login concluído com sucesso")
                # Criar a tela Principal, após o cadastro
                TelaPrincipal().criar(app)
                appLogin.destroy()