from Modulos.Banco import *
from Modulos.ClasseCategoria import *
from Modulos.Genero import Genero


class DocumentoGenero:

    def __init__(self):
        print()

    def createNewDocumentoGenero(self, idDocumento, listaGenero):
        listaId = []
        for item in listaGenero:
            listaId.append(Genero().returnIdGenero(item))



        for idGenero in listaId:
            sqlInstrucao = "INSERT INTO DocumentoGenero(idDocumento, idGenero) values (?, ?);"
            sqlParametros = (idDocumento, idGenero)
            dbInsert(sqlInstrucao, sqlParametros)