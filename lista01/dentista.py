#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:53:14 2019

@author: icaro
"""

#%%

n = int(input(""))
consultas = []
visitados = [0]*1000000
for i in range(n):
    aux = input("").replace(" ", ",").split(",")
    aux = [int(x) for x in aux]
    consultas.append(aux)
    max = 0
for j in range(n):
    melhor = 10000000
    index = 0
    for i in range(n):
         aux = abs((consultas[i][1]*(consultas[i][0]-consultas[i][1]))) 
         if(aux < melhor):
             livre = 1
             for k in visitados[consultas[i][0]:consultas[i][1]]:
                 if(k == 1):
                     livre = 0
             if(livre == 1):
                 melhor = aux
                 index = i
                 max += 1
    inicio = consultas[index][0]
    fim = consultas[index][1]
    for i in range(fim-inicio):
        visitados[inicio+i] = 1
    #print(visitados[0:20])
print(max)
#%%
n = int(input(""))
consultas = []
visitados = [0]*1000000
for i in range(n):
    aux = input("").replace(" ", ",").split(",")
    aux = [int(x) for x in aux]
    consultas.append(aux)
#print(consultas)
consultas.sort(key=lambda consultas: consultas[1])
#print(consultas)
max = 1
j = 0
for i in range(n-1):
    print(consultas[i+1][0], consultas[j][1])
    if(consultas[i+1][0] >= consultas[j][1]):
        j = i
        max +=1
print(max)

