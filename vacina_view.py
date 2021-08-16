from sqlite3.dbapi2 import Date, DateFromTicks
import tkinter as tk
from tkinter import Tk, ttk
from tkinter import messagebox as mb

from vacina import Vacina


class VacinaView:

    def __init__(self,win):
        self.vacinaCRUD = Vacina()

        #Criar os componentes de tela
        
        self.descLabel = tk.Label(win, text='Descrição:') 
        self.descEdit = tk.Entry(win, width = 32, bd=3)

        self.labLabel = tk.Label(win, text='Labolatório:') 
        self.labEdit = tk.Entry(win, width = 32, bd=3)


        self.btnCadastrar = tk.Button(win, 
                text = 'Cadastrar', width = 7, command=self._on_cadastrar_clicked)

        self.btnAlterar = tk.Button(win, 
                text = 'Alterar', width = 7, command=self._on_atualizar_clicked)

        self.btnExcluir = tk.Button(win, 
                text = 'Excluir', width = 7, command=self._on_deletar_clicked)


        self.vacinaList = ttk.Treeview(win, columns=(1,2,3), show='headings')

        self.verscrlbar = ttk.Scrollbar(win, 
                orient="vertical", command=self.vacinaList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.vacinaList.configure(yscrollcommand = self.verscrlbar.set)

        self.vacinaList.heading(1, text='Código da vacina')
        self.vacinaList.heading(2, text='Descrição')
        self.vacinaList.heading(3, text='Laboratório')

        self.vacinaList.column(1, minwidth=0, width=100)
        self.vacinaList.column(2, minwidth=0, width=200)
        self.vacinaList.column(3, minwidth=0, width=120)
        
        self.vacinaList.pack()
        self.vacinaList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)


        #Posicionar os componentes na tela
        self.descLabel.place(x=10,y=10)
        self.descEdit.place(x=95,y=10)

        self.labLabel.place(x=10,y=50)
        self.labEdit.place(x=95,y=50)


        self.btnCadastrar.place(x=320,y=10)
        self.btnAlterar.place(x=320,y=50)
        self.btnExcluir.place(x=320,y=90)
        self.vacinaList.place(x=10,y=280)
        self.verscrlbar.place(x=785,y=280, height=200)

        self.carregar_dados_iniciais_treeView()

    def _on_mostrar_clicked(self, event):
        #Selecionando a linha que o usuário clicou
        selection = self.vacinaList.selection()
        item = self.vacinaList.item(selection)
        
        #Selecionando colunas
        descricao, laboratorio = item["values"] [1:8]
           
        self.descEdit.delete(0, tk.END)   
        self.descEdit.insert(0, descricao)
        
        self.labEdit.delete(0, tk.END)
        self.labEdit.insert(0, laboratorio)


        print("Selecionando")

    def carregar_dados_iniciais_treeView(self):
        registros = self.vacinaCRUD.consultar()

        count = 0
        for item in registros:
            cod_vacina = item[0]
            descricao = item[1]
            laboratorio = item[2]

            self.vacinaList.insert('','end',iid=count, values=(str(cod_vacina),descricao,laboratorio))
            count = count + 1

    
    def _on_cadastrar_clicked(self):
        #Recuperar os dados dos campos texto
        descricao = self.descEdit.get()
        laboratorio = self.labEdit.get()
       

        #Chamar o cadastrar do vacina.py para cadastrar no banco
        if self.vacinaCRUD.cadastrar(descricao,laboratorio):
            #Atualizar a TreeView
            numeroLinhas = len(self.vacinaList.get_children())
            cod_vacina = self.vacinaCRUD.consultar_ultimo_id()
            self.vacinaList.insert('','end',iid = numeroLinhas, values=(str(cod_vacina),descricao,laboratorio))

            #Mostrar mensagem para usuário
            mb.showinfo("Mensagem", "Cadastro executado com sucesso!")

            #Limpar os campos texto
            self.descEdit.delete(0,tk.END)
            self.labEdit.delete(0,tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no cadastro!")
            #Retornando o foco
            self.descEdit.focus_set(0,tk.END)
            self.labEdit.focus_set(0,tk.END)


    def _on_atualizar_clicked(self):
        linhaSelecionada = self.vacinaList.selection()
      
        if len(linhaSelecionada) != 0:
            cod_vacina = self.vacinaList.item(linhaSelecionada[0])["values"][0]
            descricao = self.descEdit.get()
            laboratorio = self.labEdit.get()

            if  self.vacinaCRUD.atualizar(cod_vacina,descricao,laboratorio):

                self.vacinaList.item(self.vacinaList.focus(), values=(str(cod_vacina),descricao,laboratorio))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")

                self.descEdit.delete(0, tk.END)
                self.labEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")

                self.descEdit.focus_set()
                self.labEdit.focus_set()


    def _on_deletar_clicked(self):
        linhaSelecionada = self.vacinaList.selection()

        if len(linhaSelecionada) != 0:
            cod_vacina = self.vacinaList.item(linhaSelecionada[0])["values"][0]

            if  self.vacinaCRUD.excluir(cod_vacina):
                self.vacinaList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                
                self.descEdit.delete(0, tk.END)
                self.labEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                
                self.descEdit.focus_set()
                self.labEdit.focus_set()

"""
janela = tk.Tk()
principal = VacinaView(janela)
janela.title("Cadastro de Vacinas")
janela.geometry("810x560+0+0")
janela.mainloop()"""

#Autor de feature: Pedro Henrique e Wendel