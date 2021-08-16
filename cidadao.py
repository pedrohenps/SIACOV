import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Cidadao:

    def cadastrar(self,cpf,nome,email,telefone,cep,data_nascimento,profissao):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Cidadao (cpf,nome,email,telefone,cep,data_nascimento,profissao) VALUES (?,?,?,?,?,?,?)'
            cursor.execute(sql,(cpf,nome,email,telefone,cep,data_nascimento,profissao))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de cidadãos: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False



    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()
        
        try:
            resultset =  cursor.execute('SELECT * FROM cidadao').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset

    def consultar_detalhes(self, cod_cidadao):  
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()


        try:
            resultset =  cursor.execute('SELECT * FROM Cidadao WHERE cod_cidadao = ?', (cod_cidadao,)).fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        

        cursor.close()
        conexao.close()
        return resultset

    def consultar_ultimo_id(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset = cursor.execute('SELECT MAX(cod_cidadao) FROM cidadao').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]

    def atualizar(self,cod_cidadao,cpf,nome,email,telefone,cep,data_nascimento,profissao):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE Cidadao SET cpf = ?, nome = ?, email = ?, telefone = ?, cep = ?, data_nascimento = ?, profissao = ? WHERE cod_cidadao = (?)'
            cursor.execute(sql,(cpf,nome,email,telefone,cep,data_nascimento,profissao,cod_cidadao))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de cidadãos: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def excluir(self,cod_cidadao):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM Cidadao WHERE cod_cidadao = (?)'
            cursor.execute(sql,[cod_cidadao])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de cidadão: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

#Autor de feature: André