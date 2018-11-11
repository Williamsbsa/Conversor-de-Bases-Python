#binario ->decimal = Bin(1 1 0) = Dec(1*2^2 + 1*2^1 + 0*2^0)
base = int((input("Digite a base de origem do número que deseja passar para base decimal :")))
casas = int(input("Digite a quantidade de casas que haverá em seu número :"))
numero = [0] * casas
soma = 0
potencia = casas - 1

#inserindo os numeros das outras bases
for cont in range (casas):
        novoCont = cont + 1
        print ("Digite qual número deseja colocar na",novoCont, "casa :") #consegui fazer o print entrar no preencherNum.
        preencheNum = int(input())
        while (preencheNum < 0 or preencheNum >= base):
            novoCont = cont + 1
            print("Digite CORRETAMENTE qual número deseja colocar na", novoCont, "casa :")  # consegui fazer o print entrar no preencherNum.
            preencheNum = int(input())
        numero[cont] = preencheNum
print ("Número na base", base, "digitado :", numero)

#convertendo pra decimal
for cont in range (casas):
    soma = soma + (numero[cont]*base**potencia)
    potencia -= 1
print ("Valor correspondente na base Decimal = ",soma)