import os

def torreDeHanoi():
    print('''====================================================
                    TORRE DE HANOI                   
====================================================''')

    n = int(input("Com quantos discos você gostaria de ser desafiado? "))

    if n <= 0:
        print("O número de discos deve ser maior que zero.")
        return
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Boa sorte!\n")

    torres = [[i for i in range(n, 0, -1)], [], []]

    while True:
        mostrarTorres(torres)
        origem = int(input("\nDigite a torre de origem (1, 2, 3): ")) - 1
        destino = int(input("Digite a torre de destino (1, 2, 3): ")) - 1
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if origem not in (0, 1, 2) or destino not in (0, 1, 2):
            print("Torre inválida. Use 1, 2 ou 3.")
            continue

        moverDisco(torres, origem, destino)

        if torres[2] == list(range(n, 0, -1)):
            mostrarTorres(torres)
            print("\nParabéns! Você venceu a Torre de Hanoi!")
            break

def mostrarTorres(torres):
    for i in range(len(torres)):
        torre = torres[i]
        print(f"Torre {i + 1}: {torre}")

def moverDisco(torres, origem, destino):
    if torres[origem] == []:
       print("A torre de origem está vazia.\n")
    elif (torres[destino] == []) or (torres[origem][-1] < torres[destino][-1]):
        disco = torres[origem].pop()
        torres[destino].append(disco)
    else:
        print("Movimento inválido. Não é possível colocar um disco maior em cima de um menor.")

torreDeHanoi()
