#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:33:02 2019

@author: icaro
"""
#%%
'''
# Nó da árvore
class Node:
    def __init__(self,begin,end,h): 
        self.left = None
        self.right = None
        self.begin = begin
        self.end = end
        self.height = h
# Função para adicionar um nó na árvore
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
# Função para printar o nó
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 

'''
#%%

# Nó da árvore
class Node:
    def __init__(self,begin,end,h): 
        self.left = None
        self.right = None
        self.begin = begin
        self.end = end
        self.height = h
        
        
def creatree(begin, end):
    if(begin == end):
        return Node(begin, end, profundidade[begin])
    else:
        r = Node(begin, end, -1)
        r.left = creatree(begin, int(((begin+end)/2)))
        r.right = creatree(int((((begin+end)/2)+1)),end)
        return r
    
def SearchTree(r, search):    
    
    
n = int(input(""))
profundidade = [0]*(n+1)
for i in range(1,n+1):
    profundidade[i] = int(input(""))
r = creatree(1,n)
total = 0
for i in range(2, n):
    altura = profundidade[i]
    esquerda = 0
    direita = 0
    for minn in range(1,i):
        value = SearchTree(r,minn)
        if(value > altura):
            esquerda = 1
    for maxx in range(i,18):
        value = SearchTree(r,maxx)
        if(value > altura):
            direita = 1