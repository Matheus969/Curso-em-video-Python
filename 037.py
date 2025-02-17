from time import sleep  #Importa sleep, para pausar a execução

#Cabeçalho do conversor de base numérica 
print(f"""\033[1;33m{'=-'*18}
         CONVERSOR DE BASE NUM
{'=-'*18}\033[m""")

#Solicita ao usuário que digite um número 
n = int(input('\033[1;36mDigite um numero: \033[m'))

#Opções de conversão de base numérica
print(f"""\033[1;33m{'=-'*18}
[ 1 ] Bínario
[ 2 ] Octal
[ 3 ] Hexadecimal
[ 4 ] Decimal
{'=-'*18}\033[m""")

#Escolha uma das opções
r = int(input(''))

#Calcula por 3 segundos
print(f"""\033[1;33mCalculando...
{'=-'*18}\033[m""")
sleep(3)

#Verifica a opção escolhida  e realiza a conversão 
if r == 1:
    print(f"{n} em BIN é \033[1;32m{bin(n)[2:]}\033[m")
elif r == 2:
    print(f"{n} em OCT é \033[1;32m{oct(n)[2:]}\033[m")
elif r == 3:
    print(f"{n} em HEX é \033[1;32m{hex(n)[2:]}\033[m")
elif r == 4:
    print(f"{n} em DEC é \033[1;32m{n}\033[m")
else:
    print(f"\033[1;31mErro(opção {r} não existe)\033[m")
