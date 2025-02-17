#Analisando Triângulo v1.0
cor= {'0':'\033[m',
      'vd':'\033[1;32m',
      'vm':'\033[1;31m',
      'am':'\033[1;33m',
      'az':'\033[1;36;40m'}

print(f"""{cor['az']}{'=-'*18}{cor['0']}
{cor['az']}      Analisador de Triângulo       {cor['0']}
{cor['az']}{'=-'*18}{cor['0']}""")

#ler as informações do triângulo

a=float(input(f"{cor['am']}Primeiro segmento: {cor['0']}"))
b=float(input(f"{cor['am']}Segundo segmento: {cor['0']}"))
c=float(input(f"{cor['am']}Terceiro segmento: {cor['0']}"))

print(f"{cor['az']}{'=-'*18}{cor['0']}")

#calcula se forma ou não um triângulo

if a+b>c and a+c>b and b+c>a:
    print('\033[1;32mForma um Triângulo\033[m')
else:
    print('\033[1;31mNão forma um Triângulo\033[m')
