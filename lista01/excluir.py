#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:04:13 2019

@author: icaro
"""

#%%

class Node:
    def __init__(self,begin,end,val, par, impar): 
        self.left = None
        self.right = None
        self.begin = begin
        self.end = end
        self.value = val
        self.par = par
        self.impar = impar
        
def creatree(begin, end):
    if(begin == end):
        if(numeros[begin]%2 == 0):
#            print("par:", numeros[begin])
            return Node(begin, end, numeros[begin], 1, 0)
        else:
#            print("impar:", numeros[begin])
            return Node(begin, end, numeros[begin], 0, 1)
    else:
        r = Node(begin, end, -1, 0, 0)
        r.left = creatree(begin, int(((begin+end)/2)))
        r.right = creatree(int((((begin+end)/2)+1)),end)
        r.par = (r.left.par + r.right.par)
        r.impar = (r.left.impar + r.right.impar)
        return r


def SearchSegment(r, begin, end):
    if((r.begin >= begin) and (r.end <= end)):
#        print("01: ", r.value, "par: ", r.par, "impar:", r.impar)
        return [r.par, r.impar]
    elif((r.end < begin) or (r.begin > end)):
        return [-1, -1]
    else:
        esq = SearchSegment(r.left, begin, end)
        dire = SearchSegment(r.right, begin, end)
        if(esq[0]!=-1):
            if(dire[0]!=-1):
                return[esq[0]+dire[0],esq[1]+dire[1]]
            else:
                return[esq[0],esq[1]]
        if(dire[0]!=-1):
            return[dire[0],dire[1]]
            
            
def upadte(r, begin, end, new):
    if(r.begin == begin and r.end == end):
#        print("entreiiiiii")
        if(r.par == 1):
            if(new%2 == 0):
#                print("era impar e substitu� po rum par1")
                r.value = new
                return[1, 1]
            else:
#                print("era impar e substitu� po rum par3")
                r.par = 0
                r.impar = 1
                r.value = new
                return[1, 2]
        else:
            if(new%2==0):
#                print("era impar e substitu� po rum par")
                r.impar = 0
                r.par = 1
                r.value = new
                return[2, 1]
            else:
#                print("era impar e substitu� po rum par2")
                r.value = new
                return[2, 2]
    elif((r.end < begin) or (r.begin > end)):
#         print("entreiiiiiiAAAA")
         return [0,0]
    else:
#        print("entreiiiiiiBBBBBB")
        esq = upadte(r.left, begin, end, new)
        dire = upadte(r.right, begin, end, new)
        if(esq[0]!= 0):
            if(esq[0] == esq[1]):
                return [esq[0], esq[1]]
            else:
                if(esq[0] == 1):
                    r.par -= 1
                    r.impar += 1
                    return [esq[0], esq[1]]
                else:
                    r.par += 1
                    r.impar -= 1
                    return [esq[0], esq[1]]
        elif(dire[0]!=0):
            if(dire[0] == dire[1]):
                return[dire[0], dire[1]]
            else:
                if(dire[0] == 1):
                    r.par -= 1
                    r.impar += 1
                    return[dire[0], dire[1]]
                else:
                    r.par += 1
                    r.impar -= 1
                    return[dire[0], dire[1]]
        
        



#import time
#inicio = time.time()
n = int(input(""))
#print(n)
numeros = input("").replace(" ", ",").split(",")
#print(numeros[len(numeros)-1])
if(numeros[len(numeros)-1] == ''):
    del(numeros[len(numeros)-1])
#print(numeros[len(numeros)-1])
numeros = [int (x) for x in numeros]

#print(numeros)
root = creatree(0, n-1)
#print(root.impar)
q = int(input(""))
while(q != 0):
    requisicao = input("").replace(" ", ",").split(",")
#    print("requiscao",requisicao)
    begin = int(requisicao[1]) - 1
    end = int(requisicao[2]) - 1
    if(requisicao[0] == '1'):
        resultado = SearchSegment(root,begin, end)
        print(resultado[0])
    elif(requisicao[0] == '2'):
        resultado = SearchSegment(root,begin, end)
        print(resultado[1])
    else:
        upadte(root, begin, begin, end+1)
    q -=1
#fim = time.time()
#print(fim - inicio)