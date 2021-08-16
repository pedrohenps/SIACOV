import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from cidadao_view import CidadaoView
from etapa_view import EtapaView
from vacina_view import VacinaView
from vacinado_view import VacinadoView

#FUNÇÕES BOTÕES


class Aplicativo:
    def __init__(self):
        
        app = Tk()
        app.minsize(1024, 1024)
        app.title("Sistema de Vacinação COVID-19 (SIVACOV)")
        app.geometry('{}x{}+0+0'.format(*app.maxsize()))
        app.iconbitmap("images/corona.ico")
        app.configure(background='lightblue')

        #FUNÇÕES DOS BOTÕES             
        def open_cidadao(): 
            janela = tk.Toplevel(background="lightblue")
            telaCidadao = CidadaoView
            principal = telaCidadao(janela)
            janela.title("Cadastro de Cidadãos")
            janela.geometry("810x560+0+0")
            janela.focus_force()
            janela.transient(app)
            janela.iconbitmap("images/corona.ico")
            janela.mainloop() 

        def open_vacinado():
            janela2 = tk.Toplevel(background="lightblue")
            telaCidadao = VacinadoView
            principal = telaCidadao(janela2)
            janela2.title("Campanha de Vacinação")
            janela2.geometry("810x560+0+0")
            janela2.focus_force()
            janela2.transient(app)
            janela2.iconbitmap("images/corona.ico")
            janela2.mainloop() 

        def open_vacina(): 
            janela3 = tk.Toplevel(background="lightblue")
            telaVacina = VacinaView
            principal = telaVacina(janela3)
            janela3.title("Controle de Vacinas")
            janela3.geometry("810x560+0+0")
            janela3.focus_force()
            janela3.transient(app)
            janela3.iconbitmap("images/corona.ico")
            janela3.mainloop() 

        def open_etapa(): 
            janela4 = tk.Toplevel(background="lightblue")
            telaEtapa = EtapaView
            principal = telaEtapa(janela4)
            janela4.title("Controle de Etapas")
            janela4.geometry("810x560+0+0")
            janela4.focus_force()
            janela4.transient(app)
            janela4.iconbitmap("images/corona.ico")
            janela4.mainloop() 

        def close_app():
            app.destroy()
        
        #QUADRO MENU
        quadro2 = Frame(app,borderwidth = 1, relief = "solid")
        quadro2.pack()
        quadro2.place(x = 10, y = 10, width = 350, height = 750)

        #MENU LABEL
        menu_fonte = Font(
            size=14      
        )
        btn_fonte = Font(
            size=14
        )

        titulo_menu = Label(quadro2, text = "Menu", font = menu_fonte, width = 29)
        titulo_menu.place(x = 10, y = 20)

        #BOTÕES DO MENU
        btn1 = Button(quadro2, text = "Painel do Cidadão", font = btn_fonte, command = open_cidadao)
        btn1.place(x = 85, y = 120)
        btn2 = Button(quadro2, text = "Campanha de Vacinação", font = btn_fonte, command = open_vacinado)
        btn2.place(x = 58, y = 180)
        btn3 = Button(quadro2, text = "Controle de Vacinas", font = btn_fonte, command = open_vacina)
        btn3.place(x = 76, y = 240)
        btn4 = Button(quadro2, text = "Controle de Etapas", font = btn_fonte, command = open_etapa)
        btn4.place(x = 80, y = 300)
        btn5 = Button(quadro2, text = "Sair", font = btn_fonte, command = close_app)
        btn5.place(x = 145, y = 600)
          
        

        app.mainloop()
if __name__ == '__main__': 
    Aplicativo() 


#Autor de feature: André
