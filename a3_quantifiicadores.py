# Meta caracteres: ^ $ ( )
#` * 0 ou n (ilimitado)
#`  + 1 ou n {1,}
#` ? 0 ou 1
# {n} alguma coisa especifica
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''

# Os quantificadores são aplicados as coisas que estão a esquerda dele, não é só um caracter
# Podemos aplicados em grupos()+, range de conjuntos [a-zA-z0-9]+ ou no caracter literal r'jo+ão+'

# + 1 ou n {1,}, pode repetir 1 ou n vezes
print(re.findall(r'jo+ão+', texto, flags=re.I))

# Range entre [a-zA-z]+
print(re.findall(r'j[a-zA-z]+ão+', texto, flags=re.I))

# Especifico
print(re.findall(r'j[o]+ão+', texto, flags=re.I))

#´ * 0 ou n, pode existir 0 ou n vezes
print(re.findall(r'jo*ão*', texto, flags=re.I))

#´ ? 0 ou 1, pode existir 1 vez ou não existir
print(re.findall(r'jo?ão?', texto, flags=re.I))

# {min, max}, posso repetir 1 ou n vezes
# {10,} 10 ou mais
# {,10} De zero a 10
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))

# {10} Especificamente 10
# {5,10} Range de 5 a 10
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

# print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I)) # subistituindo todos os joão por Felipe

# {n}
print(10*'*    ')
texto2 = 'João ama ser amado'
print(re.findall(r'ama', texto2, flags=re.I))

# a palavra ama mais uma letra desse range [do]
print(re.findall(r'ama[do]', texto2, flags=re.I))

# irá checar o range [do] duas vezes para
print(re.findall(r'ama[do]{2}', texto2, flags=re.I))

# irá checar o range [do] de 0 ou n vezes
print(re.findall(r'ama[od]*', texto2, flags=re.I))

# irá checar o range [do] de 0 a duas vezes
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))