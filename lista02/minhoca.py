#%%
class Node:
    def __init__(self,filhos,pesoFilhos,peso): 
        self.filhos = filhos
        self.pesoFilhos = pesoFilhos
        self.peso = peso



c = input("")
c = int(c)
while(c):
    dados = input("").replace(" ", ",").split(",")
    dados = [int(x) for x in dados] 
    n = dados[0]
    m = dados[1]
    #print('n', n, 'm', m)
    # Preciso inicializar o grafo de Vértices = n
    grafo=[]
    for i in range(0,n):
        grafo.append(Node([],[],2020))
    grafo[0].peso = 0
    # Preciso preencher o grafo
    while(m):
        dados = input("").replace(" ", ",").split(",")
        dados = [int(x) for x in dados]
        grafo[dados[0]].filhos.append(dados[1])
        grafo[dados[0]].pesoFilhos.append(dados[2])
        m -= 1
   # for j in(grafo):
   #     print(j.peso, j.filhos, j.pesoFilhos)    
    # Preciso executar o Bellman Ford
    for i in range(0,(len(grafo)-1)):
        for j in(grafo):
            for qtd in range(0, len(j.filhos)):
                if((j.peso!= 2020) and grafo[j.filhos[qtd]].peso > (j.peso + j.pesoFilhos[qtd])):
                    grafo[j.filhos[qtd]].peso = (j.peso + j.pesoFilhos[qtd])
    verdade = 0
    for j in(grafo):
        for qtd in range(0, len(j.filhos)):
            if((j.peso!= 2020) and grafo[j.filhos[qtd]].peso > (j.peso + j.pesoFilhos[qtd])):
                verdade = 1
                grafo[j.filhos[qtd]].peso = (j.peso + j.pesoFilhos[qtd])
    if(verdade):
        print("possible")
    else:
        print("not possible")
    #for j in(grafo):
    #    print(j.peso, j.filhos)
    #grafo.clear()
    c -= 1
