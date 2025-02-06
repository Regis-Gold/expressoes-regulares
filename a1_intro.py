# https://github.com/luizomf/regexp-python
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex.html#regex-howto

# findall: Encontrará todas as ocorrências do padrão que quero encontrar no meu texto

# serch: Encontra a primeira ocorrência e mostrar em qual indice ele encontrou, retornando um obj math

# sub: Seria para substituir algo dentro do meu texto

# compile: compilar expressões regulares

# o r'' permite que usemos barra invertida ou para escapar algum metacaracter

# Se o que você procura não existir o retorno será >>None<<

# Lembrando que Python é uma linguagem caseSensitive

import re # import lib regular expression
string = 'Este é um teste de expressões teste regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', '1234', string, count=1))

# compilar a expressão regular e usar essas funções dentro de um obj ex: regexp
print(10 *'*   ')
regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABCD', string))