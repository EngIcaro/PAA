#import time
def dp(peso_acumulado,peso, aresta, k, solucao_valida):
    if((peso_acumulado == peso) and (solucao_valida)):
        return 1
    elif(peso_acumulado >= peso):
        return 0 
    soma = 0
    for i in range(1, k+1):
        if(i >= aresta):
            if(array_peso_valido[peso_acumulado+i]!= -1):
                soma = soma + array_peso_valido[peso_acumulado+i]
                #print(soma)
            else:
                soma = soma + dp(peso_acumulado+i, peso,aresta,k,1)
                #print(soma)
        else:
            if((array_peso_valido[peso_acumulado+i]!= -1) and (solucao_valida == 1)):
               soma = soma +  array_peso_valido[peso_acumulado+i]
               #print(soma)
            elif((array_peso_nao[peso_acumulado+i] != -1) and (solucao_valida == 0)):
                soma = soma +  array_peso_nao[peso_acumulado+i]
                #print(soma)
            else:
                soma = soma + dp(peso_acumulado+i, peso,aresta,k,solucao_valida)
    if(solucao_valida == 1):
        array_peso_valido[peso_acumulado] = soma
    elif(solucao_valida == 0):
        array_peso_nao[peso_acumulado] = soma
    #print(soma)
    return soma

#inicio = time.time()
array_peso_nao = [-1]*220
array_peso_valido = [-1]*220

n = input("").replace(" ", ",").split(",")
n = [int(x) for x in n] 
#print(n)

print(dp(0,n[0],n[2],n[1], 0)%1000000007)
#fim = time.time()
#print(fim - inicio)