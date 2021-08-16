import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Etapa:

    def cadastrar(self,nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Etapa (nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2) VALUES (?,?,?,?,?)'
            cursor.execute(sql,(nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de etapa de vacinação: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()
        #strftime(data_nascimento) data_nascimento
        try:
            resultset =  cursor.execute('SELECT * FROM etapa').fetchall()
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
            resultset = cursor.execute('SELECT MAX(id_etapa) FROM etapa').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]


    def atualizar(self,id_etapa,nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE Etapa SET nome_etapa = ?, idade = ?, categoria = ?, periodo_dose_1 = ?, periodo_dose_2 = ? WHERE id_etapa = (?)'
            cursor.execute(sql,(nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2,id_etapa))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de Etapas: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def excluir(self,id_etapa):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM Etapa WHERE id_etapa = (?)'
            cursor.execute(sql,[id_etapa])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de Etapa: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

#Autor de feature: Vitor Dilluca