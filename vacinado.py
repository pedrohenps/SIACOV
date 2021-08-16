import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Vacinado:

    def cadastrar(self,status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Vacinado (status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina) VALUES (?,?,?,?)'
            cursor.execute(sql,(status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de vacinado: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False



    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()
        
        try:
            resultset =  cursor.execute('SELECT * FROM Vacinado').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset


    def consultar_detalhes(self, protocolo):  
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = 'SELECT * FROM Vacinado WHERE protocolo = ?'

        try:
            resultset =  cursor.execute(sql,[protocolo]).fetchall()
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
            resultset = cursor.execute('SELECT MAX(protocolo) FROM Vacinado').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]

    def atualizar(self,protocolo,status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE Vacinado SET status_vacinado = ?, data_vacinado = ?, fk_Cidadao_cod_cidadao = ?, fk_Vacina_cod_vacina = ? WHERE protocolo = (?)'
            cursor.execute(sql,(status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina,protocolo))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização vacinado: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False
    

    def excluir(self,protocolo):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM Vacinado WHERE protocolo = (?)'
            cursor.execute(sql,[protocolo])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de vacinado: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

#Autor de feature: Andre, Vitor Dilluca e Wendel