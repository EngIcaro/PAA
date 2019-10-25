# Aluno: Ícaro Gabriel Paiva Bastos
# Data: 16/10/2019

# += 1 funciona
#%%

def merge(esquerda, direita):
    tamanho = len(esquerda) + len(direita)
    array = [0]*tamanho
    auxEsquerda = auxDireita = 0
    print('tamnho:' + str(tamanho) + 'esq: ' + str(auxEsquerda) + 'dir: ' + str(auxDireita))
    for i in range(0, tamanho):
        if(esquerda[auxEsquerda] < direita[auxDireita]):
            array[i] = esquerda[auxEsquerda]
            auxEsquerda+= 1
            if(auxEsquerda >= len(esquerda)):
                array[i+1:] = direita[auxDireita:]
                break
        else:
            array[i] = direita[auxDireita]
            auxDireita+=1
            if(auxDireita >= len(direita)):
                array[i+1:] = esquerda[auxEsquerda:]
                break
    print('array final: ' + str(array))
    return array


def mergesort(array):
    esquerda = []
    direita = []
    tamanho = len(array)
    if(tamanho == 1):
        return array
    else:
        mid = int(tamanho/2)
        esquerda =  mergesort(array[0:mid])
        direita  =  mergesort(array[mid:tamanho])
        
        return(merge(esquerda, direita))
        
array = input("").replace(" ", ",").split(",")
array = [int (x) for x in array]
mergesort(array)
        
    

