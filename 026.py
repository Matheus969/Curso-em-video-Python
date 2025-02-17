#Primeira e última ocorrência de uma string
a=input('Digite algo: ').strip().upper()
print(f"""Tem {a.count('A')} letras A
A primeira Letra A apareceu na posição {a.find('A')+1}
A ultima Letra A apareceu na posição {a.rfind('A')+1}""")
