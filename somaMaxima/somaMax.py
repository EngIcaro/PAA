# Soma máxima pelo método da força bruta
# run python3 terminal python3 script.py < x.in
# tamanho de um array: len(inputArray)
# lembrar que no range(i,j) só vai até j-1
def sumMax(inputArray):
    max = 0
    for i in range(len(inputArray)):
        for j in range(i,len(inputArray)):
            parcial = 0
            for pont in range(i, j+1):
                parcial = parcial + inputArray[pont]
                if (max < parcial):
                    max = parcial
    return max

array = input("").replace(" ", ",").split(",")
array = [int (x) for x in array]
print(sumMax(array))
