# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n

import re
texto2 = '''
131.768.460-53 ABC
055.123.060-50 DEF
955.123.060-90
'''

# o multiline faz com que esses dois caracteres sejam aplicados no começo ^ e fim $ de linha
# encontramos os CPF pois não usamos começa com^ e termina com$
print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', texto2, flags=re.M))

# encontramos somente o último CPF pois usamos começa com^ e termina com$
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto2, flags=re.M))

texto3 = 'O João gosta de folia \n E adora ser amado'

# para encotrar as frases que começam e terminam com a mesma letra usamos esta re, mas se tivermos quebra de linha no meio do texto teremos um resultado vazio
print(re.findall(r'^o.*o$', texto3, flags=re.I))

# para resolver esse problema usamos flags=re.S para reconhecer as quebras de linha
print(re.findall(r'^o.*o$', texto3, flags=re.I | re.S))
