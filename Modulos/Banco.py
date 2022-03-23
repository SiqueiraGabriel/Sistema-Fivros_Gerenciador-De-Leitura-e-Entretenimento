import os.path
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
from tkinter import *

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp + "\\bd_fivro.db"

def ConexaoBanco():
    con=None

    try:
        con = sqlite3.connect(nomeBanco)
    except Error as erro:
        print(f"Não foi possível conectar-se ao Banco de Dados! {erro}")
    return con


def dbSelect(query):
    vcon = ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res

def dbManipulation(sqlInstrucao, sqlParametros):
    vcon = ConexaoBanco()
    c = vcon.cursor()
    c.execute(sqlInstrucao, sqlParametros)
    vcon.commit()
    vcon.close()