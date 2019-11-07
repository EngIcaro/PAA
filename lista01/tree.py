#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:33:02 2019

@author: icaro
"""
#%%
# Nó da árvore
class Node:
    def __init__(self,key, h): 
        self.left = None
        self.right = None
        self.val = key 
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



r = Node(50, 2) 
insert(r,Node(30, 2)) 
insert(r,Node(20, 2)) 
insert(r,Node(40, 2)) 
insert(r,Node(70, 2)) 
insert(r,Node(60, 2)) 
insert(r,Node(80, 2)) 

inorder(r) 