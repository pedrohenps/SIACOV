from sqlite3.dbapi2 import Date, DateFromTicks
import tkinter as tk
from tkinter import Tk, ttk
from tkinter import messagebox as mb

from etapa import Etapa


class EtapaView:

    def __init__(self,win):
        self.etapaCRUD = Etapa()

        #nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2

        #Criar os componentes de tela
        self.nome_etapaLabel = tk.Label(win, text='Nome da Etapa:')
        self.nome_etapaEdit = tk.Entry(win, width = 32, bd=3)
        self.idadeLabel = tk.Label(win, text='Idade:') 
        self.idadeEdit = tk.Entry(win, width = 32, bd=3)
        listProfissoes = ["Médico, Enfermeiro","Dentista, Bombeiro, Policial","Professor, Motorista Público"]
        
        self.categoriaLabel = tk.Label(win, text='Categoria:') 
        #self.categoriaEdit = tk.Entry(width = 32, bd=3)
        self.categoriaEdit = ttk.Combobox(win, width = 29, values = listProfissoes)
        self.periodo_dose_1Label = tk.Label(win, text='Período Dose 1:') 
        self.periodo_dose_1Edit = tk.Entry(win, width = 32, bd=3)
        self.periodo_dose_2Label = tk.Label(win, text='Período Dose 2:') 
        self.periodo_dose_2Edit = tk.Entry(win, width = 32, bd=3)
        


        self.btnCadastrar = tk.Button(win, 
                text = 'Cadastrar', width = 7, command=self._on_cadastrar_clicked)

        self.btnAlterar = tk.Button(win, 
                text = 'Alterar', width = 7, command=self._on_atualizar_clicked)

        self.btnExcluir = tk.Button(win, 
                text = 'Excluir', width = 7, command=self._on_deletar_clicked)


        self.etapaList = ttk.Treeview(win, columns=(1,2,3,4,5,6), show='headings')

        self.verscrlbar = ttk.Scrollbar(win, 
                orient="vertical", command=self.etapaList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.etapaList.configure(yscrollcommand = self.verscrlbar.set)

        self.etapaList.heading(1, text='Código')
        self.etapaList.heading(2, text='Nome da Etapa')
        self.etapaList.heading(3, text='Idade')
        self.etapaList.heading(4, text='Categoria')
        self.etapaList.heading(5, text='Período Dose 1')
        self.etapaList.heading(6, text='Período Dose 2')
        
 

        self.etapaList.column(1, minwidth=0, width=50)
        self.etapaList.column(2, minwidth=0, width=90)
        self.etapaList.column(3, minwidth=0, width=120)
        self.etapaList.column(4, minwidth=0, width=160)
        self.etapaList.column(5, minwidth=0, width=100)
        self.etapaList.column(6, minwidth=0, width=100)
        
        self.etapaList.pack()
        self.etapaList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)


        #Posicionar os componentes na tela
        self.nome_etapaLabel.place(x=10,y=10)
        self.nome_etapaEdit.place(x=250,y=10)
        self.idadeLabel.place(x=10,y=40)
        self.idadeEdit.place(x=250,y=40)
        self.categoriaLabel.place(x=10,y=70)
        self.categoriaEdit.place(x=250,y=70)
        self.periodo_dose_1Label.place(x=10,y=100)
        self.periodo_dose_1Edit.place(x=250,y=100)
        self.periodo_dose_2Label.place(x=10,y=130)
        self.periodo_dose_2Edit.place(x=250,y=130)

        self.btnCadastrar.place(x=600,y=10)
        self.btnAlterar.place(x=600,y=50)
        self.btnExcluir.place(x=600,y=90)
        self.etapaList.place(x=10,y=280)
        self.verscrlbar.place(x=785,y=280, height=200)

        self.carregar_dados_iniciais_treeView()


    def _on_mostrar_clicked(self, event):
        #Selecionando a linha que o usuário clicou
        selection = self.etapaList.selection()
        item = self.etapaList.item(selection)
        #Selecionando colunas
        nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2 = item["values"] [1:6]
           
        self.nome_etapaEdit.delete(0, tk.END)   
        self.nome_etapaEdit.insert(0, nome_etapa)
        
        self.idadeEdit.delete(0, tk.END)
        self.idadeEdit.insert(0, idade)

        self.categoriaEdit.delete(0, tk.END)
        self.categoriaEdit.insert(0, categoria)

        self.periodo_dose_1Edit.delete(0, tk.END)
        self.periodo_dose_1Edit.insert(0, periodo_dose_1)

        self.periodo_dose_2Edit.delete(0, tk.END)
        self.periodo_dose_2Edit.insert(0, periodo_dose_2)

        print("Selecionando")


    def carregar_dados_iniciais_treeView(self):
        registros = self.etapaCRUD.consultar()

        count = 0
        for item in registros:
            id_etapa = item[0]
            nome_etapa = item[1]
            idade = item[2]
            categoria = item[3]
            periodo_dose_1 = item[4]
            periodo_dose_2 = item[5]

            self.etapaList.insert('','end',iid=count, values=(str(id_etapa),nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2))
            count = count + 1

    
    def _on_cadastrar_clicked(self):
        #Recuperar os dados dos campos texto
        nome_etapa = self.nome_etapaEdit.get()
        idade = self.idadeEdit.get()
        categoria = self.categoriaEdit.get()
        periodo_dose_1 = self.periodo_dose_1Edit.get()
        periodo_dose_2 = self.periodo_dose_2Edit.get()
       

        #Chamar o cadastrar do etapa.py para cadastrar no banco
        if self.etapaCRUD.cadastrar(nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2):
            #Atualizar a TreeView
            numeroLinhas = len(self.etapaList.get_children())
            id_etapa = self.etapaCRUD.consultar_ultimo_id()
            self.etapaList.insert('','end',iid = numeroLinhas, values=(str(id_etapa),nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2))

            #Mostrar mensagem para usuário
            mb.showinfo("Mensagem", "Cadastro executado com sucesso!")

            #Limpar os campos texto
            self.nome_etapaEdit.delete(0,tk.END)
            self.idadeEdit.delete(0,tk.END)
            self.categoriaEdit.delete(0,tk.END)
            self.periodo_dose_1Edit.delete(0,tk.END)
            self.periodo_dose_2Edit.delete(0,tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no cadastro!")
            #Retornando o foco
            self.nome_etapaEdit.focus_set(0,tk.END)
            self.idadeEdit.focus_set(0,tk.END)
            self.categoriaEdit.focus_set(0,tk.END)
            self.periodo_dose_1Edit.focus_set(0,tk.END)
            self.periodo_dose_2Edit.focus_set(0,tk.END)


    def _on_atualizar_clicked(self):
        linhaSelecionada = self.etapaList.selection()
      
        if len(linhaSelecionada) != 0:
            id_etapa = self.etapaList.item(linhaSelecionada[0])["values"][0]
            nome_etapa = self.nome_etapaEdit.get()
            idade = self.idadeEdit.get()
            categoria = self.categoriaEdit.get()
            periodo_dose_1 = self.periodo_dose_1Edit.get()
            periodo_dose_2 = self.periodo_dose_2Edit.get()

            if  self.etapaCRUD.atualizar(id_etapa,nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2):

                self.etapaList.item(self.etapaList.focus(), values=(str(id_etapa),nome_etapa,idade,categoria,periodo_dose_1,periodo_dose_2))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")

                self.nome_etapaEdit.delete(0, tk.END)
                self.idadeEdit.delete(0, tk.END)
                self.categoriaEdit.delete(0, tk.END)
                self.periodo_dose_1Edit.delete(0, tk.END)
                self.periodo_dose_2Edit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")

                self.nome_etapaEdit.focus_set()
                self.idadeEdit.focus_set()
                self.categoriaEdit.focus_set()
                self.periodo_dose_1Edit.focus_set()
                self.periodo_dose_2Edit.focus_set()


    def _on_deletar_clicked(self):
        linhaSelecionada = self.etapaList.selection()

        if len(linhaSelecionada) != 0:
            id_etapa = self.etapaList.item(linhaSelecionada[0])["values"][0]

            if  self.etapaCRUD.excluir(id_etapa):
                self.etapaList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                
                self.nome_etapaEdit.delete(0, tk.END)
                self.idadeEdit.delete(0, tk.END)
                self.categoriaEdit.delete(0, tk.END)
                self.periodo_dose_1Edit.delete(0, tk.END)
                self.periodo_dose_2Edit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                
                self.nome_etapaEdit.focus_set()
                self.idadeEdit.focus_set()
                self.categoriaEdit.focus_set()
                self.periodo_dose_1Edit.focus_set()
                self.periodo_dose_2Edit.focus_set()

"""
janela = tk.Tk()
principal = EtapaView(janela)
janela.title("Cadastro de Etapa")
janela.geometry("810x560+0+0")
janela.mainloop()"""

#Autor de feature: Vitor Dilluca e Pedro Capuzzo