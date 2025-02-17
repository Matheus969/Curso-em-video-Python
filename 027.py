#primeiro e ultimo nome
n=input('Digite seu nome completo: ').strip()
print(f'Olá, {n.split()[0]}')
print(f'Seu primeiro nome é {n.split()[0]}')
print(f'Seu último nome é {n.split()[-1]}')
