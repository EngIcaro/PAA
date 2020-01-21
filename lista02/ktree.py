def dp(i,j,k,peso,d,valido):
    global qtd
    if(qtd[i+j] != 0 and (valido)):
        return qtd[i+j]
    elif((i+j == peso) and (valido)):
        qtd[i+j] = qtd[i+j] + 1
        return 1
    elif((i + j>= peso)):
        return 0
    soma = 0
    for x in range(1,k+1):
        if(x >= d):
            soma = soma + dp(i+j,x,k,peso,d,1)
            #print(soma)
        else:
            if(valido):
                soma = soma + dp(i+j,x,k,peso,d,1)
             #   print(soma)
            else:
                soma = soma + dp(i+j,x,k,peso,d,0)
    return soma

qtd = [0]*100000
n = input("").replace(" ", ",").split(",")
n = [int(x) for x in n]
#print(n)
i = int(0); j = int(0)
#print(n[0])
print(dp(i, j,n[1],n[0],n[2],0))