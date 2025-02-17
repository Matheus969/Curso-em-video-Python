#calculador de tinta (1l por 2m²)
l=float(input('Largura da parede: '))
a=float(input('Altura da parede: '))
área=l*a
tinta=área/2
print(f"""Dimensão{l}x{a}
Àrea: {área}m²
Tinta: {tinta}l""")
