#dezena, centena, milhar
n=(input('Digite um número de 0 a 9999: ')).zfill(4)
print(f"""Unidade: {n[3]} 
Dezena: {n[2]}
Centena: {n[1]}
Milhar: {n[0]}""")