#Aumentos múltiplos
n=float(input('\033[1;33mQual salário do funcionário? R$\033[m'))
if n >= 1250.00:
    sr=n+(n * 0.10)
else:
    sr=n + (n * 0.15)
print(f'\033[1;32mQuem ganhava R${n:.2f} ganhara R${sr:.2f}\033[m]')
