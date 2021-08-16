import sqlite3
#import psycopg2
class Conexao:

    def conectar(self):
        conexao = None
        db_path = 'sivacov.db'
        try:
            conexao = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            #conexao = sqlite3.connect(db_path)
        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")
        return conexao

        #conexao = None
        #try:
        #  conexao = psycopg2.connect(user="postgres",
        #                          password="t1fas777",
        #                          host="127.0.0.1",
        #                          port="5432",
        #                          database="postgres")
        #except (Exception, psycopg2.Error) as error :
        #    print(f"Erro ao conectar o banco de dados.")
        #return conexao

    def createTableCidadao(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Cidadao (cod_cidadao INTEGER PRIMARY KEY AUTOINCREMENT,cpf varchar NOT NULL UNIQUE,nome varchar NOT NULL,email varchar NOT NULL, telefone varchar NOT NULL, cep varchar NOT NULL, data_nascimento date NOT NULL, profissao varchar NOT NULL);'
        cursor.execute(sql)
        conexao.commit()

    def createTableVacinado(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Vacinado (protocolo INTEGER PRIMARY KEY AUTOINCREMENT, status_vacinado char NOT NULL, data_vacinado date NOT NULL,fk_Cidadao_cod_cidadao int, fk_Vacina_cod_vacina int, FOREIGN KEY (fk_Cidadao_cod_cidadao) REFERENCES Cidadao (cod_cidadao),FOREIGN KEY (fk_Vacina_cod_vacina) REFERENCES Vacina (cod_vacina));'
        cursor.execute(sql)
        conexao.commit()

    def createTableVacina(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Vacina (cod_vacina INTEGER PRIMARY KEY AUTOINCREMENT, descricao varchar NOT NULL, laboratorio varchar NOT NULL);'
        cursor.execute(sql)
        conexao.commit()

    def createTableVacinacao(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Vacinacao (fk_Vacina_cod_vacina int, fk_Etapa_id_etapa int,PRIMARY KEY (fk_Vacina_cod_vacina, fk_Etapa_id_etapa),FOREIGN KEY (fk_Vacina_cod_vacina) REFERENCES Vacina (cod_vacina),FOREIGN KEY (fk_Etapa_id_etapa) REFERENCES Etapa (id_etapa));'
        cursor.execute(sql)
        conexao.commit()

    def createTableEtapa(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Etapa (id_etapa INTEGER PRIMARY KEY AUTOINCREMENT,nome_etapa varchar NOT NULL,idade INTEGER NOT NULL,categoria varchar NOT NULL,periodo_dose_1 date NOT NULL,periodo_dose_2 date NOT NULL);'
        cursor.execute(sql) 
        conexao.commit()

    def createTables(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        self.createTableCidadao(conexao,cursor)
        self.createTableVacinado(conexao,cursor)
        self.createTableVacina(conexao,cursor)
        self.createTableVacinacao(conexao,cursor)
        self.createTableEtapa(conexao,cursor)

#Autor de feature: André