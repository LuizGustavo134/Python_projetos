#empresa#
#nome/data#
#calculo da média#
while True:
    import os
    os.system("cls")
    N1= input ( "entre com a primeira nota ")
    N1 = float(N1)
    N2= input ( "entre com a segunda nota ")
    N2= float(N2)
    import time
    M=(N1+N2)/2
    print("a média dos numeros somados é", M)
    from tqdm import tqdm
    for M in tqdm(range(13)):
        time.sleep(0.5)
        os.system("cls")
    if M>=5:
        print("aprovado")
        input("pressione enter para finalizar")
    elif M<= 1:
        print("reprovado")
        input("pressione enter para finalizar")
    elif M <= 4:
        print("recuperação")
        input("pressione enter para finalizar")


