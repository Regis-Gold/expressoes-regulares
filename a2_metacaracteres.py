# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# | OU
# . Qualquer caractere (com exceção da quebra de linha)
print(re.findall(r'João|Maria|p..a', texto))
print(re.findall(r'João|joão|Maria', texto))

# [] conjunto de caracteres
# neste ex: [Jj] encontrará João e joão
# neste ex: [Mm] encontrará Maria e maria
print(re.findall(r'[Jj]oão|[Mm]aria', texto))

# pode mandar um range entre [a-z] minúsculas
print(re.findall(r'[a-z]aria', texto))

# pode mandar um range entre [A-Z] maiúsculas
print(re.findall(r'[A-Z]aria', texto))

# pode mandar um range entre [a-zA-Z] minúsculas e maiúsculas
# podemos usar [0-9] para ranges numéricos
print(re.findall(r'[a-zA-Z0-9]aria', texto))
print(re.findall(r'[a-zA-Z0-9]oão', texto))

# a flags=I ignora o caseSens da string, não diferenciando letras maiúscilas e minúsculas
print(re.findall(r'jOãO|mAriA', texto, flags=re.I))

