#Calculando Desconto 5%
r=float(input('Qual valor do produto? R$'))
d=r*0.05
print(f"""custava: R${r}
com 5% de desconto: R${r-d:.2f}""")
