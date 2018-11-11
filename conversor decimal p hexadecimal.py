# decimal = [0,1,2,3,4,5,6,7,8,9] ... hexa=[0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]
decimal = int(input("Digite um número na base Decimal, que deseja passar para Hexadecimal :"))
hexadecimal = []

while (decimal < 0):
    decimal = int(input("Digite CORRETAMENTE um número na base Decimal, que deseja passar para Hexadecimal :"))

if decimal >= 0 and decimal < 10:
    print("Valor digitado na base Decimal é (", decimal, "), convertido para base Hexadecimal fica :", decimal)

elif decimal > 9 and decimal < 16:
    for cont in range(decimal, 16, 1):
        cont = decimal
        cont = chr(55 + cont )
    print("Valor digitado na base Decimal é (", decimal, "), convertido para base Hexadecimal fica :", cont)

elif decimal >= 16:
    divisao = int(decimal/16)
    diviResto = (decimal%16)
    if diviResto <= 9:
        hexadecimal.append(diviResto)
    elif diviResto > 9 and diviResto < 16:
        for cont in range(diviResto, 16, 1):
            cont = diviResto
            cont = chr(55 + cont)
            hexadecimal.append(cont)
            break
    while divisao != 0:
        diviResto = (divisao % 16)
        divisao = int(divisao / 16)
        if diviResto <= 9:
            hexadecimal.insert(0, diviResto)
        elif diviResto > 9 and diviResto < 16:
            for cont in range(diviResto, 16, 1):
                cont = diviResto
                cont = chr(55 + cont)
                hexadecimal.insert(0, cont)
                break
    print("Valor digitado na base Decimal é (", decimal, "), convertido para base Hexadecimal fica :", hexadecimal)

else:
    print ("Número digitado está incorreto.")