
# While é um comand de loping precisa ser colocado antes de qualquer parte o código
while True:
    N1= float(input("Entre com a 1º nota: "))
    N2= float(input("Entre com a 2º nota: "))
    N3=float(input("entre com a terceira nota: "))
    op= input(''' entre com a operação desejada
                [1] Adição
                [2] subtração
                [3] multplicação
                [4] divisão
                [5] bhaskára

                ''')
        
    if op not in["1","2","3","4","5"]:
            print("digite uma opção válida")
    elif op=='1':
            ad=N1+N2+N3
            print("resultado: %.2f + = %.2f = %.2f = %.2f" %(N1,N2,N3,ad))
    elif op=='2':
            sub=N1-N2-N3
            print("resultado: %.2f - = %.2f = %.2f = %.2f" %(N1,N2,N3,sub))
    elif op=='3':
            mult=N1*N2*N3
            print("resultado: %.2f * = %.2f = %.2f = %.2f" %(N1,N2,N3,mult))
    elif op=='4':
            div=N1/N2/N3
            print("resultado: %.2f / = %.2f = %.2f = %.2f" %(N1,N2,N3,div))
    elif op=='5':
            BAS=N2*N2-4*N1*N3
            print("o resulto é",BAS)
        #break é o ponto de interrupção do looping
    print("Programa encerrado.")
     