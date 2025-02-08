# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação

import re

cpf = 'a 147.852.963-12 a '

# Como muitos dados chegam na forma de strings, que sem sempre estão de forma certa para ser validada.
# Precisamos validar o CPF para que não haja erro de dados
# Dessa forma parece estar válidado, mas tem alguns meta caracteres que podemos usar
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# adicionamos o começa com, logo após a abertura da re, ex: r'^((?:[0-9]{3}...'
# adicionamos o termina com, antes de fechar a re, ex: r'...[0-9]{2})$'
# assim teremos certeza que os campos foram digitados corretamente
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))

# podemos usar começa com ^ dentro de conjuntos, se torna a negação do conjunto
print(re.findall(r'[^0-9]+', cpf))
# mostrará tudo que não está entre [^0-9]
# ['a ', '.', '.', '-', ' a ']

