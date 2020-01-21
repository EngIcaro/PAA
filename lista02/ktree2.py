def dp(peso_acumulado,peso, aresta, k, solucao_valido):
    print(peso_acumulado, peso)
    global array_peso
    if(array_peso[peso_acumulado] != 0):
        return [array_peso[peso_acumulado], solucao_valido]
    elif(peso_acumulado == peso):
        array_peso[peso_acumulado] += 1
        return [1, solucao_valido]
    elif(peso_acumulado > peso):
        return [0,solucao_valido]
    soma = 0
    for i in range(1,k+1):
        if(i >= aresta or (solucao_valido == 1)):
            aux = dp(peso_acumulado+i, peso,aresta,k,1)
            soma = soma + aux[0]
        else:
            aux = dp(peso_acumulado+i, peso,aresta,k,0)
            if(aux[1] == 1):
                soma = soma + aux[0]
    return [soma, 1]
    


array_peso = [0]*100000    
n = input("").replace(" ", ",").split(",")
n = [int(x) for x in n] 
print(n)
final = dp(0,n[0],n[2],n[1], 0)
print(final[0])