from Modulos.Banco import *

class Genero:

    def __init__(self):
        self.id = 0
        self.nome = ""

    def returnItensGenero(self):
        """
        Método responsável por recuperar os itens da tabela Genero
        :return:
        """
        sql = "SELECT * FROM Genero order by nome;"
        result = dbSelect(sql)
        return result

    def addElementsListBoxGenero(self, lbItens):
        """
        Adicionar os elementos no ListBox de Categoria
        :param lbItens:
        :return:
        """
        valores = self.returnItensGenero()
        for item in valores:
            lbItens.insert(END, item[1])

    def createNewGenero(self, nome, lbItens):
        if nome == "":
            messagebox.showerror(title="Erro Cadastro novo Gênero", message="Por favor, verifique os valores informados!")
        else:
            sqlVerificaExistencia = f"SELECT * FROM Genero where nome = '{nome}'"
            result = dbSelect(sqlVerificaExistencia)
            if result != []:
                messagebox.showerror(title="Erro Cadastro novo Gênero", message=f"Este Gênero já foi cadastrado.\nPor favor, busque-o na lista acima!")
            else:
                sqlInstrucao = "INSERT INTO Genero(nome) values (?);"
                sqlParametro = [nome]
                dbManipulation(sqlInstrucao, sqlParametro)
                messagebox.showinfo(title="Sucesso Cadastro Gênero.", message="Seu novo gênero foi cadastrado com sucesso.")
                lbItens.update()
                self.addElementsListBoxGenero(lbItens)