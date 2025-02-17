#Calcular Aluguel de carro
d=(int(input('Quantos Dias o carro foi alugado? ')))
k=(int(input('Rodou quantos Km? ')))
r=(60*d)+(0.15*k)
print(f'O total a pagar é R${r:.2f}')
