import math

#Obtenção de Dados

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

sub1 = sub2 = sub3 = sub4 = sub5 = sub6 = sub7 = sub8 = sub9 = sub10 = sub11 = sub12 = 0
linha1 = linha2 = linha3 = linha4 = linha5 = linha6 = 0
mid1 = mid2 = mid3 = mid4 = mid5 = mid6 = 0
histerese = 0

for l in range (0, 5):
    for c in range (0, 4):
        matriz[l][c]= float(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)

for l in range(0, 5):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)

#Incerteza da Histerese

#Subtração de colunas
sub1 = matriz[0][0] - matriz[0][1]
sub2 = matriz[0][2] - matriz[0][3]
sub3 = matriz[1][0] - matriz[1][1]
sub4 = matriz[1][2] - matriz[1][3]
sub5 = matriz[2][0] - matriz[2][1]
sub6 = matriz[2][2] - matriz[2][3]
sub7 = matriz[3][0] - matriz[3][1]
sub8 = matriz[3][2] - matriz[3][3]
sub9 = matriz[4][0] - matriz[4][1]
sub10 = matriz[4][2] - matriz[4][3]

#Comparar a maior histerese

maior = sub1

if sub2>sub1 and sub2>sub3 and sub2>sub4 and sub2>sub5 and sub2>sub6 and sub2>sub7 and sub2>sub8 and sub2>sub9 and sub2>sub10:
    maior = sub2

elif sub3>sub1 and sub3>sub2 and sub3>sub4 and sub3>sub5 and sub3>sub6 and sub3>sub7 and sub3>sub8 and sub3>sub9 and sub3>sub10:
    maior = sub3

elif sub4>sub1 and sub4>sub2 and sub4>sub3 and sub4>sub5 and sub4>sub6 and sub4>sub7 and sub4>sub8 and sub4>sub9 and sub4>sub10:
    maior = sub4

elif sub5>sub1 and sub5>sub2 and sub5>sub3 and sub5>sub4 and sub5>sub6 and sub5>sub7 and sub5>sub8 and sub5>sub9 and sub5>sub10:
    maior = sub5

elif sub6>sub1 and sub6>sub2 and sub6>sub3 and sub6>sub4 and sub6>sub5 and sub6>sub7 and sub6>sub8 and sub6>sub9 and sub6>sub10:
    maior = sub6

elif sub7>sub1 and sub7>sub2 and sub7>sub3 and sub7>sub4 and sub7>sub5 and sub7>sub6 and sub7>sub8 and sub7>sub9 and sub7>sub10:
    maior = sub7

elif sub8>sub1 and sub8>sub2 and sub8>sub3 and sub8>sub4 and sub8>sub5 and sub8>sub6 and sub8>sub7 and sub8>sub9 and sub8>sub10:
    maior = sub8

elif sub9>sub1 and sub9>sub2 and sub9>sub3 and sub9>sub4 and sub9>sub5 and sub9>sub6 and sub9>sub7 and sub9>sub8 and sub9>sub10:
    maior = sub9

elif sub10>sub1 and sub10>sub2 and sub10>sub3 and sub10>sub4 and sub10>sub5 and sub10>sub6 and sub10>sub7 and sub10>sub8 and sub10>sub9:
    maior = sub10

print(f'A maior histerese é: {maior}')

if maior<0:
    maior * (-1)

uHisterese = maior/math.sqrt(12)

#Incerteza do tipo A

#Cálculo da média

for c in range (0,4):
    linha1 += matriz[0][c]

for c in range (0,4):
    linha2 += matriz[1][c]

for c in range (0,4):
    linha3 += matriz[2][c]

for c in range (0,4):
    linha4 += matriz[3][c]

for c in range (0,4):
    linha5 += matriz[4][c]

#Média

mid1 = linha1/4
mid2 = linha2/4
mid3 = linha3/4
mid4 = linha4/4
mid5 = linha5/4

#Subtração das médias

#Média Linha 1
a1 = (mid1-matriz[0][0])
b1 = (mid1-matriz[0][1])
c1 = (mid1-matriz[0][2])
d1 = (mid1-matriz[0][3])

#Média Linha 2
a2 = (mid2-matriz[1][0])
b2 = (mid2-matriz[1][1])
c2 = (mid2-matriz[1][2])
d2 = (mid2-matriz[1][3])

#Média Linha 3
a3 = (mid3-matriz[2][0])
b3 = (mid3-matriz[2][1])
c3 = (mid3-matriz[2][2])
d3 = (mid3-matriz[2][3])

#Média Linha 4
a4 = (mid4-matriz[3][0])
b4 = (mid4-matriz[3][1])
c4 = (mid4-matriz[3][2])
d4 = (mid4-matriz[3][3])

#Média Linah 5
a5 = (mid5-matriz[4][0])
b5 = (mid5-matriz[4][1])
c5 = (mid5-matriz[4][2])
d5 = (mid5-matriz[4][3])

#Elevação ao quadrado dos valores

#Elevação Linha 1
ElevA1 = a1 ** 2
ElevB1 = b1 ** 2
ElevC1 = c1 ** 2
ElevD1 = d1 ** 2

#Elevação Linha 2
ElevA2 = a2 ** 2
ElevB2 = b2 ** 2
ElevC2 = c2 ** 2
ElevD2 = d2 ** 2

#Elevação Linha 3
ElevA3 = a3 ** 2
ElevB3 = b3 ** 2
ElevC3 = c3 ** 2
ElevD3 = d3 ** 2

#Elevação Linha 4
ElevA4 = a4 ** 2
ElevB4 = b4 ** 2
ElevC4 = c4 ** 2
ElevD4 = d4 ** 2

#Elevação Linha 5
ElevA5 = a5 ** 2
ElevB5 = b5 ** 2
ElevC5 = c5 ** 2
ElevD5 = d5 ** 2

#Soma dos valores de incerteza tipo A

Soma1 = ElevA1+ElevB1+ElevC1+ElevD1
Soma2 = ElevA2+ElevB2+ElevC2+ElevD2
Soma3 = ElevA3+ElevB3+ElevC3+ElevD3
Soma4 = ElevA4+ElevB4+ElevC4+ElevD4
Soma5 = ElevA5+ElevB5+ElevC5+ElevD5

#Divisão por raíz de 12

raiz1 = Soma1/math.sqrt(12)
raiz2 = Soma2/math.sqrt(12)
raiz3 = Soma3/math.sqrt(12)
raiz4 = Soma4/math.sqrt(12)
raiz5 = Soma5/math.sqrt(12)

#Maior incerteza do tipo A entre as linhas

uA = raiz1

if raiz2>raiz1 and raiz2>raiz3 and raiz2>raiz4 and raiz2>raiz5:
    uA = raiz2

elif raiz3>raiz1 and raiz3>raiz2 and raiz3>raiz4 and raiz3>raiz5:
    uA = raiz3

elif raiz4>raiz1 and raiz4>raiz2 and raiz4>raiz3 and raiz4 > raiz5:
    uA = raiz4

elif raiz5>raiz1 and raiz5>raiz2 and raiz5>raiz3 and raiz5>raiz4:
    uA = raiz5

#Incerteza do Padrão

ucP = 0.03/2

#Incerteza da resolução

uRes = 0.01/math.sqrt(12)

#Incerteza do forno

uForno = 0.08/math.sqrt(12)

#Incerteza final

uSoma = ucP**2 + uRes**2 + uForno**2 + uHisterese**2 + uA**2
uComb = math.sqrt(uSoma)
uFinal = uComb*2

#Impressão de incertezas
print(f'Incerteza do Padrão: {ucP}')
print(f'Incerteza da Resolução: {uRes}')
print(f'Incerteza do Forno: {uForno}')
print(f'Incerteza do tipo A: {uA}')
print(f'Incerteza da Histerese: {uHisterese}')

print(f'Incerteza Expandida Final: {uFinal}')