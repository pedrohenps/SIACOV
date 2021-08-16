from sqlite3.dbapi2 import Date, DateFromTicks
import tkinter as tk
from tkinter import Tk, ttk
from tkinter import messagebox as mb

from cidadao import Cidadao


class CidadaoView:

    def __init__(self,win):
        self.cidadaoCRUD = Cidadao()

        #Criar os componentes de tela
        
        #Label - Label do input / Entry - Input
        self.cpfLabel = tk.Label(win, text='CPF:') 
        self.cpfEdit = tk.Entry(win, width = 32, bd=3) 
        self.nomeLabel = tk.Label(win, text='Nome:') 
        self.nomeEdit = tk.Entry(win, width = 32, bd=3)
        self.emailLabel = tk.Label(win, text='E-mail:') 
        self.emailEdit = tk.Entry(win, width = 32, bd=3)
        self.telefoneLabel = tk.Label(win, text='Telefone:') 
        self.telefoneEdit = tk.Entry(win, width = 32, bd=3)
        self.cepLabel = tk.Label(win, text='CEP:') 
        self.cepEdit = tk.Entry(win, width = 32, bd=3)
        self.data_nascimentoLabel = tk.Label(win, text='Data Nascimento:') 
        self.data_nascimentoEdit = tk.Entry(win, width = 32, bd=3)
        #Lista de profissões na Combobox
        listProfissoes = ["Médico","Enfermeiro","Dentista","Bombeiro","Policial","Professor","Motorista Público"]
        self.profissaoLabel = tk.Label(win, text='Profissão:') 
        self.profissaoEdit = ttk.Combobox(win, width = 29, values = listProfissoes)
        #self.profissaoEdit = tk.Entry(width = 32, bd=3)

        #Button - Botões
        self.btnCadastrar = tk.Button(win, text = 'Cadastrar', width = 7, command=self._on_cadastrar_clicked)
        self.btnAlterar = tk.Button(win, text = 'Alterar', width = 7, command=self._on_atualizar_clicked)
        self.btnExcluir = tk.Button(win, text = 'Excluir', width = 7, command=self._on_deletar_clicked)

        #Treeview - Tabela
        self.cidadaoList = ttk.Treeview(win, columns=(1,2,3,4,5,6,7,8), show='headings')

        #Scrollbar - Barra de rolagem
        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.cidadaoList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.cidadaoList.configure(yscrollcommand = self.verscrlbar.set)

        #heading - Atributo da Treeview, cabeçalho da tabela nome de cada coluna
        self.cidadaoList.heading(1, text='Código')
        self.cidadaoList.heading(2, text='CPF')
        self.cidadaoList.heading(3, text='Nome')
        self.cidadaoList.heading(4, text='E-mail')
        self.cidadaoList.heading(5, text='Telefone')
        self.cidadaoList.heading(6, text='CEP')
        self.cidadaoList.heading(7, text='Data Nascimento')
        self.cidadaoList.heading(8, text='Profissão')

        #column - Atributo da Treeview, tamanhos e configuração das colunas
        self.cidadaoList.column(1, minwidth=0, width=50)
        self.cidadaoList.column(2, minwidth=0, width=90)
        self.cidadaoList.column(3, minwidth=0, width=120)
        self.cidadaoList.column(4, minwidth=0, width=160)
        self.cidadaoList.column(5, minwidth=0, width=100)
        self.cidadaoList.column(6, minwidth=0, width=70)
        self.cidadaoList.column(7, minwidth=0, width=100)
        self.cidadaoList.column(8, minwidth=0, width=80)
        
        self.cidadaoList.pack()
        self.cidadaoList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)


        #Posicionar os componentes na tela
        self.cpfLabel.place(x=10,y=10)
        self.cpfEdit.place(x=60,y=10)
        self.nomeLabel.place(x=10,y=40)
        self.nomeEdit.place(x=60,y=40)
        self.emailLabel.place(x=10,y=70)
        self.emailEdit.place(x=60,y=70)
        self.telefoneLabel.place(x=10,y=100)
        self.telefoneEdit.place(x=60,y=100)
        self.cepLabel.place(x=270,y=10)
        self.cepEdit.place(x=370,y=10)
        self.data_nascimentoLabel.place(x=270,y=40)
        self.data_nascimentoEdit.place(x=370,y=40)
        self.profissaoLabel.place(x=270,y=70)
        self.profissaoEdit.place(x=370,y=70)

        self.btnCadastrar.place(x=600,y=10)
        self.btnAlterar.place(x=600,y=50)
        self.btnExcluir.place(x=600,y=90)
        self.cidadaoList.place(x=10,y=280)
        self.verscrlbar.place(x=785,y=280, height=200)

        self.carregar_dados_iniciais_treeView()

    def _on_mostrar_clicked(self, event):
        #Selecionando a linha que o usuário clicou
        selection = self.cidadaoList.selection()
        item = self.cidadaoList.item(selection)
        #Selecionando colunas
        cpf,nome,email,telefone,cep,data_nascimento,profissao = item["values"] [1:8]
           
        self.cpfEdit.delete(0, tk.END)   
        self.cpfEdit.insert(0, cpf)
        
        self.nomeEdit.delete(0, tk.END)
        self.nomeEdit.insert(0, nome)

        self.emailEdit.delete(0, tk.END)
        self.emailEdit.insert(0, email)

        self.telefoneEdit.delete(0, tk.END)
        self.telefoneEdit.insert(0, telefone)
        
        self.cepEdit.delete(0, tk.END)
        self.cepEdit.insert(0, cep)

        self.data_nascimentoEdit.delete(0, tk.END)
        self.data_nascimentoEdit.insert(0, data_nascimento)

        self.profissaoEdit.delete(0, tk.END)
        self.profissaoEdit.insert(0, profissao)

        print("Selecionando")


    def carregar_dados_iniciais_treeView(self):
        registros = self.cidadaoCRUD.consultar()

        count = 0
        for item in registros:
            cod_cidadao = item[0]
            cpf = item[1]
            nome = item[2]
            email = item[3]
            telefone = item[4]
            cep = item[5]
            data_nascimento = item[6]
            profissao = item[7]

            self.cidadaoList.insert('','end',iid=count, values=(str(cod_cidadao),cpf,nome,email,telefone,cep,data_nascimento,profissao))
            count = count + 1


    def _on_cadastrar_clicked(self):
        #Recuperar os dados dos campos texto
        cpf = self.cpfEdit.get()
        nome = self.nomeEdit.get()
        email = self.emailEdit.get()
        telefone = self.telefoneEdit.get()
        cep = self.cepEdit.get()
        data_nascimento = self.data_nascimentoEdit.get()
        profissao = self.profissaoEdit.get()
       

        #Chamar o cadastrar do cidadao.py para cadastrar no banco
        if self.cidadaoCRUD.cadastrar(cpf,nome,email,telefone,cep,data_nascimento,profissao):
            #Atualizar a TreeView
            numeroLinhas = len(self.cidadaoList.get_children())
            cod_cidadao = self.cidadaoCRUD.consultar_ultimo_id()
            self.cidadaoList.insert('','end',iid = numeroLinhas, values=(str(cod_cidadao),cpf,nome,email,telefone,cep,data_nascimento,profissao))

            #Mostrar mensagem para usuário
            mb.showinfo("Mensagem", "Cadastro executado com sucesso!")

            #Limpar os campos texto
            self.cpfEdit.delete(0,tk.END)
            self.nomeEdit.delete(0,tk.END)
            self.emailEdit.delete(0,tk.END)
            self.telefoneEdit.delete(0,tk.END)
            self.cepEdit.delete(0,tk.END)
            self.data_nascimentoEdit.delete(0,tk.END)
            self.profissaoEdit.delete(0,tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no cadastro!")
            #Retornando o foco
            self.cpfEdit.focus_set(0,tk.END)
            self.nomeEdit.focus_set(0,tk.END)
            self.emailEdit.focus_set(0,tk.END)
            self.telefoneEdit.focus_set(0,tk.END)
            self.cepEdit.focus_set(0,tk.END)
            self.data_nascimentoEdit.focus_set(0,tk.END)
            self.profissaoEdit.focus_set(0,tk.END)


    def _on_atualizar_clicked(self):
        linhaSelecionada = self.cidadaoList.selection()
      
        if len(linhaSelecionada) != 0:
            cod_cidadao = self.cidadaoList.item(linhaSelecionada[0])["values"][0]
            cpf = self.cpfEdit.get()
            nome = self.nomeEdit.get()
            email = self.emailEdit.get()
            telefone = self.telefoneEdit.get()
            cep = self.cepEdit.get()
            data_nascimento = self.data_nascimentoEdit.get()
            profissao = self.profissaoEdit.get()

            if  self.cidadaoCRUD.atualizar(cod_cidadao,cpf,nome,email,telefone,cep,data_nascimento,profissao):

                self.cidadaoList.item(self.cidadaoList.focus(), values=(str(cod_cidadao),cpf,nome,email,telefone,cep,data_nascimento,profissao))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")

                self.cpfEdit.delete(0, tk.END)
                self.nomeEdit.delete(0, tk.END)
                self.emailEdit.delete(0, tk.END)
                self.telefoneEdit.delete(0, tk.END)
                self.cepEdit.delete(0, tk.END)
                self.data_nascimentoEdit.delete(0, tk.END)
                self.profissaoEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")

                self.cpfEdit.focus_set()
                self.nomeEdit.focus_set()
                self.emailEdit.focus_set()
                self.telefoneEdit.focus_set()
                self.cepEdit.focus_set()
                self.data_nascimentoEdit.focus_set()
                self.profissaoEdit.focus_set()


    def _on_deletar_clicked(self):
        linhaSelecionada = self.cidadaoList.selection()

        if len(linhaSelecionada) != 0:
            cod_cidadao = self.cidadaoList.item(linhaSelecionada[0])["values"][0]

            if  self.cidadaoCRUD.excluir(cod_cidadao):
                self.cidadaoList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                
                self.cpfEdit.delete(0, tk.END)
                self.nomeEdit.delete(0, tk.END)
                self.emailEdit.delete(0, tk.END)
                self.telefoneEdit.delete(0, tk.END)
                self.cepEdit.delete(0, tk.END)
                self.data_nascimentoEdit.delete(0, tk.END)
                self.profissaoEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                
                self.cpfEdit.focus_set()
                self.nomeEdit.focus_set()
                self.emailEdit.focus_set()
                self.telefoneEdit.focus_set()
                self.cepEdit.focus_set()
                self.data_nascimentoEdit.focus_set()
                self.profissaoEdit.focus_set()

""""
janela = tk.Tk()
principal = CidadaoView(janela)
janela.title("Cadastro de Cidadãos")
janela.geometry("810x560+0+0")
janela.mainloop()"""

#Autor de feature: André e Linda