#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 07:38:55 2019

@author: icaro
"""

#%%
# Busca em largura
def largura(grafo, vertInicial):
    # Criando o array de visitados
    visitados = [0]*1000000
    # Marco o primero  vertice como visitado
    visitados[vertInicial] = 1
    # Crio a fila
    fila = []
    # enfilero o vertice inicial
    fila.append(vertInicial)
    while(len(fila)):
        # Retiro o vértice FIFO
        vertAtual = fila.pop(0)
        # Processso
        print(vertAtual)
        # Pegando a lista dos vértices adjacentes a ele
        lista = grafo[vertAtual][1]
        # percorrendo todos os vértices
        for i in range(len(lista)):
            # Verificando se esse vértce já foi visitado. Caso não tenha sido
            # Enfileire o vértice e marque com ovisitado
            adjacente = lista[i]
            if(visitados[adjacente] == 0):
                    visitados[adjacente] = 1
                    fila.append(adjacente)


def profundidade():
    cor = [0]*1000000
    distância = [0]*100000
#%%
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
#%%
grafo = sorted(grafo.values(), key=itemgetter(0), reverse= True)
#%%
values = []
for i in grafo.values():
    values.append(i)
values = sorted(values,key=itemgetter(0), reverse = True)
#%%
#Ordenando o dicionário
valores = grafo.values()
print(valores)
#valores = valores[]
#print(valores)
#valores = sorted(valores)
#print(valores)




