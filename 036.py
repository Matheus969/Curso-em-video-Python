#Aprovando Empréstimo

cs=float(input('\033[1;36mQual valor da casa? R$: \033[m'))
sl=float(input('\033[1;36mQual seu salário? R$: \033[m'))
an=float(input('\033[1;36mQuantos anos você vai pagar? \033[m'))
pr=cs/(an*12)
mn=sl * 30/100
#exibe as informaçoes

print(f"""\033[1;33m{'=-'*18}
Casa: R${cs:.2f} 
Anos: {an:.0f} 
Prestação: R${pr:.2f} 
{'=-'*18}\033[m""")

#aprovado ou negado

if pr <= mn:
    print('\033[1;32mEmpréstimo aprovado\033[m') 
else:
    print('\033[1;31mEmpréstimo negado\033[m')
