#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:02:07 2019

@author: icaro
"""
#%%
from decimal import *

getcontext().prec = 2

n = int(input(""))
#print(n)
peso = int(input(""))
#print(peso)
decolar = input("").replace(" ", ",").split(",")
decolar = [int (x) for x in decolar]
#print(decolar)
pousar = input("").replace(" ", ",").split(",")
pousar = [int (x) for x in pousar]
#print(pousar)
begin = 0
end = 10000000000
gasolina = 0
while(abs(end-begin) > 1e-6):
#    print("begin: ", begin, "end: ", end)
    atual = (begin+end)/2
    sobrou = atual
#    print("atual: ", sobrou)
    for i in range(len(decolar)):
        gasolinaDecolar = ((peso+sobrou)/decolar[i])
        sobrou = (sobrou - gasolinaDecolar)
        gasolinaPousar = ((peso+sobrou)/pousar[i])
        sobrou = (sobrou - gasolinaPousar)
    if(sobrou>=0):
        gasolina = atual
#        print("sobrou: ", sobrou, "gasolina: ", gasolina)
        end = atual
    else:
        begin = atual
if(gasolina < 1e-7):
    print("-1")
else: 
    print("%.2f" % gasolina)