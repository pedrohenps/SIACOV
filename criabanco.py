from conexao import Conexao

def criarBanco():
    conn = Conexao()
    conn.createTables()

criarBanco()