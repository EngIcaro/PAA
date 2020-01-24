dados = list(map(int, input().split()))
#print(dados[0], dados[1])
n = dados[0]
m = dados[1]
# Criando a matriz
matriz = [[10010]*n for i in range(n)]
# Inicializando a diagonal toda com 0
for i in range(n):
    matriz[i][i] = 0  
# Preenchendo a matriz
while(m):
    dados = list(map(int, input().split()))
    if(matriz[dados[0]][dados[1]] > dados[2]):
        matriz[dados[0]][dados[1]] = dados[2]
        matriz[dados[1]][dados[0]] = dados[2]
    m -= 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if(matriz[i][j] > matriz[i][k] + matriz[k][j]):
                matriz[i][j] = matriz[i][k] + matriz[k][j]
# Achando a máxima mínima distância percorrida
maior = 10010
for coluna in range(n):
    aux = 0
    for linha in range(n):
        if(aux < matriz[linha][coluna]):
            aux = matriz[linha][coluna]
    if(maior > aux):
        maior = aux
#print(matriz)
print(maior)