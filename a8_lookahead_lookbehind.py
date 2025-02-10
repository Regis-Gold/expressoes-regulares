Uso de lookahead e lookbehind

import re
from pprint import pprint

texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

"""
Lookahead e lookbehind são recursos onde você pode condicionar sua expressão com o que vem à frente ou antes da busca desejada, porém ele em si não será incluído no resultado da expressão.
"""

"""
# aqui usamos: 
\w para pegar 1º um texto,
\s para pegar o 1º espaço,
usamos o grupo (\d+\.\d+\.\d+\.\d+) para encontrar a sequência de números dos IPs
\s para pegar o 2º espaço,
\w para pegar 2º um texto,
\s para pegar o 3º espaço,
(?=active) | (?!active) |
no final a variável texto que é a nossa base 
"""

# Positive lookahead
# usamos o grupo (?=active) para verificar se está active
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
print(10*'------')

# ou podemos usar essa re r'(?=.*[^in]active).+' que teremos um resultado semelhante
pprint(re.findall(r'(?=.*[^in]active).+', texto))
print(10*'------')

"""-------------------------------------"""
# Negative lookahead
# usamos o grupo (?!active) para verificar se está inactive
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))
print(10*'------')

# ou podemos usar essa re r'(?=.*inactive).+' que teremos um resultado semelhante
pprint(re.findall(r'(?=.*inactive).+', texto))
print(10*'------')

"""-------------------------------------"""
# Positive lookbehind
# usamos o grupo (?<=ONLINE) para verificar se está online
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
print(10*'------')

# ou usamos
pprint(re.findall(r'\w+(?<!OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
print(10*'------')

"""-------------------------------------"""
# Negative lookbehind
# usamos o grupo (?<!ONLINE) para verificar se está online
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
print(10*'------')

# ou usamos
pprint(re.findall(r'\w+(?<=OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
print(10*'-----")