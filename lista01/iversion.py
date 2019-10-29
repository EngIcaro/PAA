#%%
def merge(esquerda, direita):
    tamanho = len(esquerda) + len(direita)
    array = [0]*tamanho
    global inversoes
    auxEsquerda = auxDireita = 0
#    print('tamnho:' + str(tamanho) + 'esq: ' + str(auxEsquerda) + 'dir: ' + str(auxDireita))
    for i in range(0, tamanho):
        if(esquerda[auxEsquerda] <= direita[auxDireita]):
            array[i] = esquerda[auxEsquerda]
            auxEsquerda+= 1
            if(auxEsquerda >= len(esquerda)):
                array[i+1:] = direita[auxDireita:]
                break
        else:
            array[i] = direita[auxDireita]
            auxDireita+=1
            inversoes += (len(esquerda)-auxEsquerda)
            if(auxDireita >= len(direita)):
                array[i+1:] = esquerda[auxEsquerda:]
                break
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
        #print("esquerda: ", esquerda, "direita: ", direita)
        return(merge(esquerda, direita))

t = int(input(""))
numeros =[]
inversoes = 0
while(t):
    linha = input("")  
    n = int(input(""))
    for i in range(n):
        numeros.append(int(input("")))
    mergesort(numeros)
    numeros.clear()
    print(inversoes)
    inversoes = 0
    t-=1        
    

