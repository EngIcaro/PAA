# -*- coding: utf-8 -*-
# Aluno: Ícaro Gabriel Paiva Bastos
# Data 16/10/2019
#%%
def potencia(number, power):
    if(power == 1):
        return number
    if(power%2 == 0):
        power = power/2
        resultado = potencia(number,power)
        return resultado * resultado
    else:
        power = (power-1)/2
        resultado = potencia(number,power)
        return resultado * resultado * number

print(potencia(5,2))