# Meta caracteres: ^ $ ( )
# [@#a-zA-Z0-9] nos conjuntos encontraremos coisas dentro de um range
# (ABC|DEF) nos grupos teremos de encontrar especificamento o que pedimos
# nos dois casos podemos usar um quantificador de após o sinal a dir ex: 
# conjunto [a-zA-Z0-9]+
# grupos(abc|def)+

# Os grupos são salvos na memória
# (tx) podemos acessar o retrovisor assim \1

import re
# para que possamos ver o print de uma forma mais bonita importamos o pprint
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Frase qualquer</p> <div></div>
'''

"""
# ()    \1
# () () \1  \2
# (()) () \1  \2  \3
# para saber o número do retrovisor, devemos contar quantas aberturas de parentedes tem no grupo

# criamos o grupo ([vidp]{1,3}) que pode ser acessado com \1 para não termos que repetição

# dessa forma irá retornar apenas as tags
print(re.findall(r'<([vidp]{1,3})>.*?<\/\1>', texto))
print(10*'-----')

# pra resolvermos isso teremos de por tudo dentro de um grupo maior, envolvendo toda a re e chamando o retrovisor \2
tags = (re.findall(r'(<([vidp]{1,3})>.*?<\/\2>)', texto))
pprint(tags)
print(10*'-----')
# assim teremos uma tupla com todos os resultados

# podemos separar coisas em grupos, para depois termos acesso a essa coisa
# no findall podemos acessar somente o texto dentro das tags, adicionando mas um grupo no dotall dessa forma (.*?) para quantificar coisas
tags2 = (re.findall(r'(<([vidp]{1,3})>(.*?)<\/\2>)', texto))
pprint(tags2)
print(10*'-----')
# e podemos pegar esse

for tag in tags2:
    um, dois, tres = tag
    pprint(tres)

# Um exemplo interessante de se usar é ?: na abertura do grupo (?: para sinalizar que quero criar o grupo mas não quero salvar ele
print(10*'-----')
print(re.findall(r'<([vidp]{1,3})>(?:.*?)<\/\1>', texto))
# encontra as palavras mas não as retorna

print(10*'-----')
"""

cpf = '147.852.963-12'
# validação do formato do CPF
# dentro da re usamos três vezes [0-9]{3}
# separamos as três com \.
# e no ultimo usamos [0-9]{2} separado por -
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))

# como podemos observar o primeiro e segundo treixo são iguais, então podemos por dentro de um conjunto e multiplicar por 2 com um quantificador, ex: ([0-9]{3}\.){2}
print(re.findall(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}', cpf))
# mais isso não gera o ['147.852.'] como esperamos, pois ela checa o primeiro e salva, depois checa o segundo e salva, ficando somente o segundo salvo na memoria

# pra resolver isso colocamos a re inteira dentro de um grupo maior
# usamos ?: no inicio do retovisor \2  para sinalizar que o grupo foi criado mas não não estará salvo na memoria
# assim teremos o CPF completo
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# em Python podemos criar um grupo nomeado
# usamos ?P<> e colocamos o nome entre os sinais de maior e menor
# podemos acessar pelo número do grupo ou pelo nome que criamos
print(re.findall(r'<(?P<tag>[vidp]{1,3})>.*?<\/\1>', texto))
print(re.findall(r'<(?P<tag>[vidp]{1,3})>.*?<\/(?P=tag)>', texto))

# substituindo tudo que está dentro da tag e colocando entre aspas
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"um(a) \3"\4', texto))
