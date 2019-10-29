#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 07:38:55 2019

@author: icaro
"""

#%%

config = input("").replace(" ", ",").split(",")
config = [int (x) for x in config]
print(config)
vertices = input("").replace(" ", ",").split(",")
vertices = [int (x) for x in vertices]
grafo = {}
visitados = [0]*1000000
for i in range(len(vertices)):
    grafo[i+1] = [vertices[i], []]

for i in range(config[1]):
    aresta = input("").replace(" ", ",").split(",")
    aresta = [int(x) for x in aresta]
    grafo[aresta[0]][1].append(aresta[1])