from sqlite3.dbapi2 import Date, DateFromTicks
import tkinter as tk
from tkinter import StringVar, Tk, ttk
from tkinter import messagebox as mb

from vacinado import Vacinado


class VacinadoView:

    def __init__(self,win):
        self.vacinadoCRUD = Vacinado()

        #Criar os componentes de tela
        self.status_vacinadoLabel = tk.Label(win, text='Vacinado:')
        self.vacinadoSimNao = StringVar()
        self.status_vacinadoEdit = tk.Radiobutton(win, text = "Não", value="N", variable = self.vacinadoSimNao)
        self.status_vacinadoEdit2 = tk.Radiobutton(win, text = "Sim", value="S", variable = self.vacinadoSimNao)
        self.data_vacinadoLabel = tk.Label(win, text='Data Vacinação:') 
        self.data_vacinadoEdit = tk.Entry(win, width = 32, bd=3)
        self.fk_Cidadao_cod_cidadaoLabel = tk.Label(win, text='Código Cidadão:') 
        self.fk_Cidadao_cod_cidadaoEdit = tk.Entry(win, width = 32, bd=3)
        self.fk_Vacina_cod_vacinaLabel = tk.Label(win, text='Código Vacina:') 
        self.fk_Vacina_cod_vacinaEdit = tk.Entry(win, width = 32, bd=3)
  


        self.btnCadastrar = tk.Button(win, 
                text = 'Cadastrar', width = 7, command=self._on_cadastrar_clicked)

        self.btnAlterar = tk.Button(win, 
                text = 'Alterar', width = 7, command=self._on_atualizar_clicked)

        self.btnExcluir = tk.Button(win, 
                text = 'Excluir', width = 7, command=self._on_deletar_clicked)


        self.vacinadoList = ttk.Treeview(win, columns=(1,2,3,4,5), show='headings')

        self.verscrlbar = ttk.Scrollbar(win, 
                orient="vertical", command=self.vacinadoList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.vacinadoList.configure(yscrollcommand = self.verscrlbar.set)

        self.vacinadoList.heading(1, text='Protocolo')
        self.vacinadoList.heading(2, text='Status Vacinado')
        self.vacinadoList.heading(3, text='Data de Vacinação')
        self.vacinadoList.heading(4, text='Cidadão')
        self.vacinadoList.heading(5, text='Vacina')
    

        self.vacinadoList.column(1, minwidth=0, width=50)
        self.vacinadoList.column(2, minwidth=0, width=90)
        self.vacinadoList.column(3, minwidth=0, width=120)
        self.vacinadoList.column(4, minwidth=0, width=160)
        self.vacinadoList.column(5, minwidth=0, width=100)

        
        self.vacinadoList.pack()
        self.vacinadoList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)


        #Posicionar os componentes na tela
        self.status_vacinadoLabel.place(x=10,y=10)
        self.status_vacinadoEdit.place(x=120,y=10)
        self.status_vacinadoEdit2.place(x=180,y=10)
        self.data_vacinadoLabel.place(x=10,y=40)
        self.data_vacinadoEdit.place(x=120,y=40)
        self.fk_Cidadao_cod_cidadaoLabel.place(x=10,y=70)
        self.fk_Cidadao_cod_cidadaoEdit.place(x=120,y=70)
        self.fk_Vacina_cod_vacinaLabel.place(x=10,y=100)
        self.fk_Vacina_cod_vacinaEdit.place(x=120,y=100)

        self.btnCadastrar.place(x=600,y=10)
        self.btnAlterar.place(x=600,y=50)
        self.btnExcluir.place(x=600,y=90)
        self.vacinadoList.place(x=10,y=280)
        self.verscrlbar.place(x=785,y=280, height=200)

        self.carregar_dados_iniciais_treeView()


    def _on_mostrar_clicked(self, event):
        #Selecionando a linha que o usuário clicou
        selection = self.vacinadoList.selection()
        item = self.vacinadoList.item(selection)
        #Selecionando colunas
        data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina = item["values"] [2:5]
     
        self.data_vacinadoEdit.delete(0, tk.END)
        self.data_vacinadoEdit.insert(0, data_vacinado)

        self.fk_Cidadao_cod_cidadaoEdit.delete(0, tk.END)
        self.fk_Cidadao_cod_cidadaoEdit.insert(0, fk_Cidadao_cod_cidadao)

        self.fk_Vacina_cod_vacinaEdit.delete(0, tk.END)
        self.fk_Vacina_cod_vacinaEdit.insert(0, fk_Vacina_cod_vacina)


        print("Selecionando")


    def carregar_dados_iniciais_treeView(self):
        registros = self.vacinadoCRUD.consultar()

        count = 0
        for item in registros:
            protocolo = item[0]
            status_vacinado = item[1]
            data_vacinado = item[2]
            fk_Cidadao_cod_cidadao = item[3]
            fk_Vacina_cod_vacina = item[4]


            self.vacinadoList.insert('','end',iid=count, values=(str(protocolo),status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina))
            count = count + 1

    
    def _on_cadastrar_clicked(self):
        #Recuperar os dados dos campos texto
        status_vacinado = self.vacinadoSimNao.get()
        data_vacinado = self.data_vacinadoEdit.get()
        fk_Cidadao_cod_cidadao = self.fk_Cidadao_cod_cidadaoEdit.get()
        fk_Vacina_cod_vacina = self.fk_Vacina_cod_vacinaEdit.get()
               

        #Chamar o cadastrar do vacinado.py para cadastrar no banco
        if self.vacinadoCRUD.cadastrar(status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina):
            #Atualizar a TreeView
            numeroLinhas = len(self.vacinadoList.get_children())
            protocolo = self.vacinadoCRUD.consultar_ultimo_id()
            self.vacinadoList.insert('','end',iid = numeroLinhas, values=(str(protocolo),status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina))

            #Mostrar mensagem para usuário
            mb.showinfo("Mensagem", "Cadastro executado com sucesso!")

            #Limpar os campos texto
            self.data_vacinadoEdit.delete(0,tk.END)
            self.fk_Cidadao_cod_cidadaoEdit.delete(0,tk.END)
            self.fk_Vacina_cod_vacinaEdit.delete(0,tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no cadastro!")
            #Retornando o foco
            self.data_vacinadoEdit.focus_set(0,tk.END)
            self.fk_Cidadao_cod_cidadaoEdit.focus_set(0,tk.END)
            self.fk_Vacina_cod_vacinaEdit.focus_set(0,tk.END)


    def _on_atualizar_clicked(self):
        linhaSelecionada = self.vacinadoList.selection()
      
        if len(linhaSelecionada) != 0:
            protocolo = self.vacinadoList.item(linhaSelecionada[0])["values"][0]
            status_vacinado = self.vacinadoSimNao.get()
            data_vacinado = self.data_vacinadoEdit.get()
            fk_Cidadao_cod_cidadao = self.fk_Cidadao_cod_cidadaoEdit.get()
            fk_Vacina_cod_vacina = self.fk_Vacina_cod_vacinaEdit.get()

            if  self.vacinadoCRUD.atualizar(protocolo,status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina):

                self.vacinadoList.item(self.vacinadoList.focus(), values=(str(protocolo),status_vacinado,data_vacinado,fk_Cidadao_cod_cidadao,fk_Vacina_cod_vacina))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")

                
                self.data_vacinadoEdit.delete(0, tk.END)
                self.fk_Cidadao_cod_cidadaoEdit.delete(0, tk.END)
                self.fk_Vacina_cod_vacinaEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")

                self.data_vacinadoEdit.focus_set()
                self.fk_Cidadao_cod_cidadaoEdit.focus_set()
                self.fk_Vacina_cod_vacinaEdit.focus_set()


    def _on_deletar_clicked(self):
        linhaSelecionada = self.vacinadoList.selection()

        if len(linhaSelecionada) != 0:
            protocolo = self.vacinadoList.item(linhaSelecionada[0])["values"][0]

            if  self.vacinadoCRUD.excluir(protocolo):
                self.vacinadoList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                
                self.status_vacinadoEdit.delete(0, tk.END)
                self.data_vacinadoEdit.delete(0, tk.END)
                self.fk_Cidadao_cod_cidadaoEdit.delete(0, tk.END)
                self.fk_Vacina_cod_vacinaEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                
                self.status_vacinadoEdit.focus_set()
                self.data_vacinadoEdit.focus_set()
                self.fk_Cidadao_cod_cidadaoEdit.focus_set()
                self.fk_Vacina_cod_vacinaEdit.focus_set()

"""
janela = tk.Tk()
principal = VacinadoView(janela)
janela.title("Vacinados")
janela.geometry("810x560+0+0")
janela.mainloop()"""

#Autor de feature: André , Vitor Dilluca, Pedro Henrique e Wendel