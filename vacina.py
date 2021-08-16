import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Vacina:

    def cadastrar(self,descricao,laboratorio):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Vacina (descricao,laboratorio) VALUES (?,?)'
            cursor.execute(sql,(descricao,laboratorio))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de vacinas: {}".format(e))
            return False


    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()
        
        try:
            resultset =  cursor.execute('SELECT * FROM vacina').fetchall()
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
            resultset = cursor.execute('SELECT MAX(cod_vacina) FROM vacina').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]

    def atualizar(self,cod_vacina,descricao,laboratorio):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE vacina SET descricao = ?, laboratorio = ? WHERE cod_vacina = (?)'
            cursor.execute(sql,(descricao,laboratorio,cod_vacina))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de vacinas: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def excluir(self,cod_vacina):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM vacina WHERE cod_vacina = (?)'
            cursor.execute(sql,[cod_vacina])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de vacina: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

# Autor de feature: Pedro Henrique e Wendel