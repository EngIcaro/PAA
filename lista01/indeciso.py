import time

inicio = time.time()    
n = int(input(""))
lista = input().replace(" ", ",").split(",")
lista = [int(x) for x in lista]
q = int(input(""))
for i in range(q):
    dinheiro = int(input(""))
    begin = 0
    end = len(lista)-1
    hi = 0
    lo = 0
    beginlo = 0
    endlo = len(lista)-1
    while(begin <= end or beginlo <= endlo):
        if(begin<= end):
            mid = int((begin+end)/2)
            if(lista[mid] >= dinheiro):
                hi = mid
                end = mid-1
            else:
                begin = mid + 1
        if(beginlo <= endlo):
            midlo = int((beginlo+endlo)/2)
            if(lista[midlo] <= dinheiro):
                lo = midlo
                beginlo = midlo+1
            else:
                endlo = midlo - 1      
    print(hi, lo)
    fim = time.time()
    print(fim - inicio)