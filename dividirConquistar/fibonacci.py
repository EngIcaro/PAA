#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:45:23 2019
@author: Icaro Gabriel Paiva Bastos
"""
#%% Fibonacci Top-Down
def fibonacci(n):
    if(n <= 1):
        return n
    resultado = fibonacci(n-1) + fibonacci(n-2)
    print(resultado)
    return resultado
fibonacci(11)
#%% Fibonacci bottom-up

def fibonnaci(n):
    fib2 = 1
    fib1 = 0
    resultado = 0
    for i in range(n):
        resultado = fib2 + fib1
        fib1 = fib2
        fib2 = resultado
    return resultado
print(fibonnaci(11))
