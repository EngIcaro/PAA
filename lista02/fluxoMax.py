def largura(matriz,father,inicio,fim,n):
    visited = [0]*n
    #for i in range(n):
    lista = []
    lista.append(0)
    while(len(lista)):
        vertice = lista.pop(0)
        for i in range(n):
            if((matriz[vertice][i] > 0) and (visited[i] == 0)):
                visited[i] = 1
                father[i] = vertice
                lista.append(i)
    return visited[fim]

def ford_fulkerson(matriz, inicio, fim, n):
    max_flow = 0
    father  = [-1]*n
    while(largura(matriz,father,inicio,fim, n)):
        print("passei")
        path_flow = 1000
        novofim = fim
       # Agora, de trás pra frente, verificamos qual é a aresta
       # com menor capacidade residual. Ou seja, qual é o
       # "gargalo" daquele caminho.

        while(novofim != inicio):
            vertice = father[novofim]
            if(matriz[vertice][novofim] < path_flow):
                path_flow = matriz[vertice][novofim]
            novofim = vertice
        print('path', path_flow)     
       # Uma vez descoberta o "gargalo", é preciso subtrair
       # das capacidades de cada aresta do caminho, esse valor.
       # O caminho é sempre: u->v
       # Logo, temos que diminuir da aresta [u][v] e aumentar a aresta [v][u]     
        novofim = fim 
        while(novofim != inicio):
            vertice = father[novofim]
            matriz[vertice][novofim] -= path_flow
            matriz[novofim][vertice] += path_flow
            novofim = vertice
        max_flow += path_flow
        print(max_flow)
dados = list(map(int, input().split()))
#print(dados[0], dados[1])
n = dados[0]
m = dados[1]

# Criando a matriz
matriz = [[0]*n for i in range(n)]
print(matriz)

while(m):
    dados = list(map(int, input().split()))
    matriz[dados[0]][dados[1]] = dados[2]
    
    m -= 1
ford_fulkerson(matriz, 0, 1, n)
#print(matriz)
#largura(matriz, n)