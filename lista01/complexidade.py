# -*- coding: utf-8 -*-

#%%
import math
import matplotlib.pyplot as plt
def graph():
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    f5 = []
    f6 = []
    f7 = []
    f8 = []
    f9 = []
    f10 = []
    f11 = []
    f13 = []
    f14 = []
    f15 = []
    for x in range(2,50):
        print(x)
        #f1.append((2 ** x))
        f2.append(math.log(math.log(x,2), 2))
        #f3.append(((x ** 3) + math.log(x,2)))
        f4.append(math.log((x ** 2),2))
       # f5.append((x - (x ** 2) + (5*(x**3))))
       # f6.append((x ** x))
        #f7.append((x ** 2))
     #   f8.append((x ** 3))
        f9.append((x * math.log(x,2)))
        f10.append((math.log(x,2) ** 2))
        f11.append((x ** (1/2)))
        #f13.append(math.factorial(x))
        f14.append(x)
        f15.append(((3/2) ** 2))
    #plt.subplot(1,1,1); plt.plot(f1, color= 'blue', label = '2^x')
    #plt.legend()
    plt.subplot(1,1,1); plt.plot(f2, color= 'red', label = 'lg(lg(n))')
    plt.legend()
    #plt.subplot(1,1,1); plt.plot(f3, color= 'black', label = 'n^3 + lg(n)')
    #plt.legend()
    plt.subplot(1,1,1); plt.plot(f4, color= 'pink', label = 'lg(n^2)')
    plt.legend()
    #plt.subplot(1,1,1); plt.plot(f5, color= 'yellow', label = 'n - n^2 + 5n^3')
    #plt.legend()
    #plt.subplot(1,1,1); plt.plot(f6, color= 'orange', label = 'n^n')
    #plt.legend()
    #plt.subplot(1,1,1); plt.plot(f7, color= 'steelblue', label = 'n^2')
    #plt.legend()
    #plt.subplot(1,1,1); plt.plot(f8, color= 'crimson', label = 'n^3')
    #plt.legend()
    plt.subplot(1,1,1); plt.plot(f9, color= 'purple', label = 'n*lg(n)')
    plt.legend()
    plt.subplot(1,1,1); plt.plot(f10, color= 'coral', label = '(lg(n))^2')
    plt.legend()
    plt.subplot(1,1,1); plt.plot(f11, color= 'grey', label = '(n)^1/2')
    plt.legend()
    #plt.subplot(1,1,1); plt.plot(f13, color= 'navy', label = 'n!')
    #plt.legend()
    plt.subplot(1,1,1); plt.plot(f14, color= 'olivedrab', label = 'x')
    plt.legend()
    plt.subplot(1,1,1); plt.plot(f15, color= 'goldenrod', label = '(3/2)^n')
    plt.legend()
    plt.show()
graph()