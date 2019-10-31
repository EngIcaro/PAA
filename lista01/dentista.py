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
    melhor = -1
    index = 0
    for i in range(n):
         aux = ((consultas[i][1] - consultas[i][0])/consultas[i][0]) 
         if(aux > melhor):
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