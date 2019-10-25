# -*- coding: utf-8 -*-
"""
Aluno: Ícaro Gabriel Paiva
Questão: Sr. Indeciso
"""

#%%
def binary(lista, dinheiro, begin, end,busca):
    # 
    if(busca == "hi"):
        # Verificando o caso base
        if(begin == end):
            if(lista[begin] >= dinheiro):
                return begin
            return 0
        mid = int((begin + end)/2)
        print(mid)
        if(lista[mid] >= dinheiro):
            end = mid
            return min(binary(lista, dinheiro, begin, end,"hi"), end)
        else:
            begin = mid - 1
            return min(binary(lista, dinheiro, begin, end,"hi"), begin)

    return 0



n = int(input("entre com o valor de n:"))
lista = input().replace(" ", ",").split(",")
lista = [int(x) for x in lista]
print(lista)
q = int(input(""))
print("valor de q = {}".format(q))
for i in range(q):
    dinheiro = int(input(""))
    print(binary(lista, dinheiro,0, len(lista),"hi"))