#luiz gustavo da silva melo
#Ads
#Umc
import os
#====================================
def chk_mat (Nome,Lista):
    for i,db in enumerate(Lista):
        if db[0]==Lista:
            return i
    return "None"
#====================================
def New_name ():
    Menu2=input(''' O que deseja alterar? 
    (1) Nome
    (2) Metodo de pagamento
    (3) Endereço
    (4) Sabor   ''')
    if Menu2 not in ["1","2","3","4"]:
        print("digite uma opção válida! ")
        input("")      
    elif "1" in Menu2:
        Nnome=input("Novo nome: ")  
        L0[0]=Nnome,Xf,Ac,Xk
        print(L0[0])
        print("concluido")
    elif "2" in Menu2:
        Nsabor=input('''Novo sabor: ''')  
        L0[0]=Nm,Nsabor,Ac,Xk
        print(L0[0])
        print("concluido")   
    else:
        input ("pressione enter para voltar ao menu ")
#===  de alterar nome ==================
def ver_indice():
    for indice in range(len(L0)):
        print(f'Índice: [1]')
#====================================
def temporizador():
    import time 
    time.sleep(0.3)
#====================================
        

L0=[]

os.system("cls")
while True:
    os.system("cls")
    print("Olá bem-vindo a pizzaria pipe o que podemos te ajudar? ")
    import time
    time.sleep(0.5)
    opt=input(''' Selecione uma opção
(1) fazer pedido
(2) modificar pedido
(3) ver comandas
(4) Saída
==> ''')
    temporizador()
    if opt not in ["1","2","3","4","5"]:
        input ("Opção inválida - pressione enter para voltar ao menu ")
    elif opt == "1":
        Nm=input(f"Nome: ")  
        temporizador()    
        Val_Func = chk_mat(Nm,L0)
        if Val_Func == "None":
            str(1)
            str(2)
            str(3)
            Sa=input(''' selecione o sabor
            (1)Calabresa 
            (2) Queijo e bacon
            (3)frango e catupiry
            ''')
            temporizador()
            if "1" in Sa:
                Xf="Calabresa"
            elif "2" in Sa:
                Xf="Queijo e bacon"
            elif "3" in Sa:
                Xf="frango e catupiry"
            #O comando In faz uma busca e verifica um item na lista"
            Ac=int(input(" Endereço *CEP* : "))
            temporizador()
            #é importante definir e converter o tipo de dado durante a execução do comando
            #str converte o numero em string#
            Pg=input('''Como deseja pagar? 
            (1)Debito
            (2)Pix
            (3)Dinheiro 
            apenas uma opção:  ''')
            temporizador()
            if "1" in Pg:
                Xk="debito"
            elif "2" in Pg:
                Xk="pix"
            elif "3" in Pg:
                Xk="dinheiro"
                #O comando In faz uma busca e verifica um item na lista"
            L0.append( [Nm,Xf,Ac,Xk,])
            print("Pedido feito")
            temporizador()
        else:
            print ("Registro Existente")
            input ("pressione enter para voltar ao menu ")
            temporizador() 
    elif opt=="2":
         New_name()
    
        
        
                
    elif opt=="3":
        #sempre use o a função enumerate para imprimir o conteudo da lista incluindo os indices também!
        for i, item in enumerate(L0):
            print(i,item)
            temporizador()
    input ("Pressione enter para voltar ao menu ")
