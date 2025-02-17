#Ano Bissexto
from datetime import date
ano=int(input('\033[1;4;33mDigite um ano,(Digite 0 para o ano atual):\033[m '))
if ano == 0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;7;32m{ano} é um ano bissexto\033[m')
else:
    print(f'\033[1;7;31m{ano} não é um ano bissexto\033[m')
