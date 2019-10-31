#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:56:19 2019

@author: icaro
"""
from operator import itemgetter
config = input("").replace(" ", ",").split(",")
config = [int (x) for x in config]
#print(config)
# Lendo os vertices
vertices = input("").replace(" ", ",").split(",")
vertices = [int (x) for x in vertices]
# Criando o grafo
grafo = {}
# Criando o grafo. atribuindo o tempo daquelo vértice e               uma lista vazia de ligações
for i in range(len(vertices)):
    grafo[i+1] = [vertices[i], []]
# Lendo as ligações e atribuindo a lista do vértice corrento
for i in range(config[1]):
    aresta = input("").replace(" ", ",").split(",")
    aresta = [int(x) for x in aresta]
    grafo[aresta[0]][1].append(aresta[1])
    grafo[aresta[1]][1].append(aresta[0])
visitados = [0]*1000000
tempo = 0
for j in grafo.keys():
    maior = -1
    index = 0
    for i in grafo.keys():
        if(maior < grafo[i][0] and (visitados[i]==0)):
            maior = grafo[i][0]
            index = i
    adjacentes = grafo[index][1]
    for i in range(len(adjacentes)):
        if(visitados[adjacentes[i]] == 0):    
            tempo += grafo[adjacentes[i]][0]
    visitados[index] = 1
print(tempo)
