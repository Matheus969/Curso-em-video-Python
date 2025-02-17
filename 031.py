#Custo da Viagem
Km=int(input('Quantos km tem sua viajem? '))
if Km <= 200:
    price=0.50*Km
else:
    price=0.45*Km
print(f"Sua viajem custara, R${price:.2f}")
