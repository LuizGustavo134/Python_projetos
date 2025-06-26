
while True:
    N1=float (input("entre com a 1ºnota: "))
    N2=float(input("entre com a 2ºnota: "))
    N3=float(input("entre com a 3ºnota: "))
    #Digite os coeficientes A,B e C # 
    X=N2*N2-4*N1*N3
    print("o resulto é",X)

    # fórmula do delta, delta=b²-4.a.c 
    # B²-x
    # x #
    break
P1=input("Deseja continuar? (sim/não/): ")
if " sim" in P1:
    B1=float(input("entre com -b ")) 
    B2=float(input("entre com delta ")) 
    B3=float(input("proxima nota "))
    B4=float(input("entre com a "))
    #cálculo do x1 e x2
    # -b +ou- delta/2.a #
while True:
    import math

    num = float(B2)
    raiz = math.sqrt(num)
    print(f"A raiz quadrada de {num} é {raiz}")
    X1=raiz
        #raiz quadrada#
    X2=-N2+X1
        #-b + delta#
    X3= 2*N1
        #2.a#
    X4= X2/X3
    if X4>=-1:
        print("resultado inválido")
        #resultado da primeira equacação  dividido por 2.a #
    print("o resulto é",X2)
    break



