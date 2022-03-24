from tkinter import *
from Modulos.Banco import *

class Autor:

    def __init__(self):
        print()

    def returnItensAutor(self):
        """
        Método responsável por retornar todos os autores cadastrados no BD
        :return:
        """
        sql =  "SELECT * FROM Autor order by nome;"
        result = dbSelect(sql)
        return result

    def returnIdCategoria(self, nome):
        sql = f"SELECT * FROM Autor where nome = '{nome}'"
        result = dbSelect(sql)
        return result[0][0]

    def addElementListBoxAutor(self, listbox=""):
        """
        Método responsável por adicionar os autores no ListBox
        :param listbox:
        :return:
        """
        listbox.delete(0, END)
        valores = self.returnItensAutor()
        for item in valores:
            listbox.insert(END, item[1])

    def createNewAutor(self, nome, biografia, anoNasc, anoFales, paisOrigem, listBox):
        if nome == "" or biografia == "" or paisOrigem == "":
            messagebox.showerror(title="Erro Cadastro Autor", message="Por favor, verifique os valores informados!")
        else:
            sqlVerificaAutor = f"SELECT * FROM Autor where nome = '{nome}';"
            result = dbSelect(sqlVerificaAutor)
            if result != []:
                messagebox.showerror(title="Erro Cadastro Autor", message=f"Este Autor já foi cadastrado.\nPor favor, busque-o na lista acima!")
            else:
                sqlInstrucao = "INSERT INTO Autor(nome, biografia, anoNascimento, anoFalescimento,paisOrigem) values (?, ?, ?, ?, ?);"
                sqlParametros = (nome, biografia, anoNasc, anoFales, paisOrigem)
                dbManipulation(sqlInstrucao, sqlParametros)
                self.addElementListBoxAutor(listBox)
