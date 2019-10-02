# Acrescentar sys.setrecursionlimit(10000) para recursão
# Para fazer um for decrescente for i in range(meio-1,-1,-1) vai até 0 com passos de -1
# A medida que for resolvendo coloque prints para facilitar

import sys
sys.setrecursionlimit(10000)

def dividirConquistar(array):
    #Condição de parada
    tamanho = len(array)
    if(tamanho == 1):
        # retornar o valor do meio
        print(array[0])
        return array[0]

    meio = int(tamanho/2)
    esquerda = 0
    ponteiro = 0
    direita  = 0
    # Vou olhar o melhor sufixo da parte esquerda
    for i in range(meio-1,-1,-1):
        ponteiro = ponteiro + array[i]
        if(esquerda < ponteiro):
            esquerda = ponteiro
    ponteiro = 0
    # Vou olhar o melhor prefixo da parte direita
    for i in range(meio, tamanho):
        ponteiro = ponteiro + array[i]
        if(direita < ponteiro):
            direita = ponteiro

    # Vou somar. Tendo assim a solução do meio
    soma = esquerda + direita
    # Vou olar o melhor da direita e esquerda para isso chamar a função recursiva dividindo os arrays
    a =  dividirConquistar(array[0:meio])
    b =  dividirConquistar(array[meio:tamanho])
    # Vou olhar quem foi o maior max(meio, esquerdo ou direito)
    return max(soma, a, b)
array = input("").replace(" ", ",").split(",")
array = [int (x) for x in array]
print(dividirConquistar(array))
