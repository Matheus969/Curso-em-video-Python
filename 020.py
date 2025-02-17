#Sorteio de Ordem 
from random import shuffle
a=input('Primeiro Aluno: ')
b=input('segundo Aluno: ')
c=input('Terceiro Aluno: ')
d=input('Quarto Aluno: ')
#sorteia lista
l=[a, b, c, d]
shuffle(l)
#exibe o resultado da lista
print(f"""A ordem da apresentação é
{(l)}""")
