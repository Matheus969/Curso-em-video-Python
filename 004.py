#Dissecando uma variável
p=input('Digite algo: ')
print(f"""O tipo primitivo e {type(p)}
È letra?: {p.isalpha()}
È alphanúmeric?: {p.isalnum()}
È número?: {p.isnumeric()}
È minúsculo?: {p.islower()}
È maiúsculo?: {p.isupper()}
È titulo?: {p.istitle()}
È digito?: {p.isdigit()}
È númerico?: {p.isdecimal()}
È feito de espaço?: {p.isspace()}""")
