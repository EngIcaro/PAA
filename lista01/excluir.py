#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:56:43 2019

@author: icaro
"""
#%%
grafo = {}
grafo[1] = ["agua", "vinho"]
grafo[2] = "vinho"
grafo[1].append("jjj")

# Percorrer vértices do grafo
for e in grafo:
    print(e)

aux = []
# Percorrer as arestas
for e in grafo.values():
    aux.append(e)

# Deletar valor de um grafo