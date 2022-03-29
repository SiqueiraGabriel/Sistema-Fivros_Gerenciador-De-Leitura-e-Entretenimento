from Modulos.Banco import *

class BD_Documento:

    def __init__(self):
        print()

    def searchIdDocument(self, name):
        sql = f"SELECT idDocumento from Documento where titulo = '{name}'"
        result = dbSelect(sql)
        for item in result:
            return item[0]

    def returnAllUpdateDocument(self, idDocumento):
        sql = f"SELECT situacao, observacoes, dataInicio, dataTermino from Documento where idDocumento = '{idDocumento}'"
        result = dbSelect(sql)
        return result[0]

    def updateDocument(self, idDocumento, situacao, dataInicio, dataTermino, observacoes, telaAlteracao):
        txtConfirm = messagebox.askyesno(title="Alteração de Dados Documento", message="Você deseja alterar os dados deste documento")
        
        if txtConfirm:
            sql = f"UPDATE Documento " \
              f"set situacao = '{situacao}', dataInicio = '{dataInicio}', dataTermino = '{dataTermino}', observacoes = '{observacoes}' " \
                  f"where idDocumento = '{idDocumento}';"
            dbUpdate(sql)
            messagebox.showinfo(title="Alteração do Documento", message="Dados atualizados com sucesso!")
            telaAlteracao.destroy()
        else:
            messagebox.showwarning(title="Alteração do Docuemnto", message="Os dados cadastrados forma excluídos e o documento não foi alterado")
            telaAlteracao.destroy()

