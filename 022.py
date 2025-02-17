#Leitor de nome
n=input('Qual seu nome completo?  ')
print(f"""Maiúscula: {n.upper()}
Minúscula: {n.lower()}
Quantas letras: {len(n.replace(' ',''))}
Quantas letras primeiro nome: {len(n.split()[0])}""")
