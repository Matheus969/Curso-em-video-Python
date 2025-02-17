#Maior e menor valores
n1=float(input('\033[4;33mDigite o primeiro número: \033[m'))
n2=float(input('\033[4;33mDigite o segundo número: \033[m'))
n3=float(input('\033[4;33mDigite o terceiro número: \033[m'))

maior = n1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
if n2 > n1 and n3:
    maior = n2
if n3 > n1 and n2:
    maior = n3

menor = n1
if n2 < n1:
    menor = n2
if n3 < n1:
    menor = n3
print(f'\033[1;32m{maior} È o maior número\033[m')
print(f'\033[1;31m{menor} È o menor número\033[m')
