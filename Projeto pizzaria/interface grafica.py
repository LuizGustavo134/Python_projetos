from tkinter import *
from contextlib import closing
from tkinter import ttk
 # Carrega TXT e Salva TXT
###### Carrega TXT
lista=["ovo","uva","pera","frango"]

##Funções
def My_Select():
    tree.delete(*tree.get_children())
    tree.place(x=180,y=25) 
    #Carrega dados na Treview
    for chave,dados in lista.items():        
        i=[chave,dados[0],dados[1],dados[2]]
        tree.insert('', END, values=i)    
#### Instancia a classe TK
Janela = Tk()
Janela.title("Sistema de Cadastro de Funcionários")
Janela.geometry('820x400')
#### Título do Aplicativo - Label
Tit = Label(Janela, text="Selecione uma das opções abaixo")
Tit.place(x=0,y=0)
Tit["font"] = ("Verdana", "10", "italic", "bold",)
Tit["fg"]=("blue")
Tit["bg"]=("white")
#### Botão Select
Botao_Sel = Button(Janela, text="Relatório Geral",width=15)
Botao_Sel.place(x=0,y=25)
Botao_Sel['command']=My_Select
#### TreeView
# define columns Treeview
columns = ('Matricula', 'Nome','Cargo','Salário')
tree = ttk.Treeview(Janela, columns=columns, show='headings')
# define headings
tree.column('#1', width=100)
tree.column('#2', width=200)
tree.column('#3', width=200)
tree.column('#4', width=100)
tree.heading('Matricula', text='Matrícula')
tree.heading('Nome', text='Nome do Funcionário')
tree.heading('Cargo', text='Cargo')
tree.heading('Salário', text='Salário')
#### Botão Sair
Sair= Button(Janela, text="Sair da Aplicação", command=Janela.destroy,width=15)
Sair.place(x=0,y=125)
####
Janela.mainloop()