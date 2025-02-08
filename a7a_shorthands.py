# os shorthand com letras minusculas são para encontrar alguma coisa, e os shorthand com letras maiusculas são a negação da coisa

# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda
# \B -> não borda

# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

"""
# pegando todas as palavras de uma string

# usamos um conjunto com um range de a-z e o quantificador + que pode repetir 1 ou n vezes, dessa forma: r'[a-z]+'
# e usamos flags=re.I para ignorar o case
# assim temos todas as palavras, sem acentos
# print(re.findall(r'[a-z]+', texto, flags=re.I))

# letras minúsculas e maiúsculas
print(re.findall(r'[a-zA-Z]+', texto))
print(10*'------')

# letras minúsculas e maiúsculas e números
print(re.findall(r'[a-zA-Z0-9]+', texto))
print(10*'------')

# letras minúsculas e maiúsculas, números e todas as letras com acentuação
print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
print(10*'------')

# usando o shorthand r'\w+' para fazer exatamente o que foi feito anteriormente
# isso inclui outros caracteres especiais
print(re.findall(r'\w+', texto))
print(10*'------')

# se usarmos flags=re.A, não estará em full unicode mas somente a tabela ASCII
# se parecerá com o conjunto letras minúsculas e maiúsculas, e números
print(re.findall(r'\w+', texto, flags=re.A))
print(10*'------')

# usando o r'\W+' teremos quebras de linha, virgulas, espaços, pontuação
print(re.findall(r'\W+', texto))
print(10*'------')

# com a flags=re.A pegamos letras acentuadas
print(re.findall(r'\W+', texto, flags=re.A))
print(10*'------')

# usando r'\d+' pegamos somente os números
print(re.findall(r'\d+', texto, flags=re.A))
print(10*'------')

# usando r'\D+' pegamos o inverso de números
print(re.findall(r'\D+', texto, flags=re.A))
print(10*'------')

# usando r'\s+' pegamos qualquer tipo de espaço
print(re.findall(r'\s+', texto, flags=re.A))
print(10*'------')

# usando r'\S+' pegamos td que não é espaço
print(re.findall(r'\S+', texto, flags=re.A))
print(10*'------')

# usando r'\b+' irá encontrar uma string vazia no começo ou no fim de cada palavra
# usamos da seguinte maneira para:

#  palavras que começam com e: r'\be\w+'
print(re.findall(r'\be\w+', texto, flags=re.A))
print(10*'------')

#  palavras que terminam com e: r'\w+e\b'
print(re.findall(r'\w+e\b', texto, flags=re.A))
print(10*'------')

#  palavras que tem exatamente um número determinado de letras: r'\b\w{4}\b'
print(re.findall(r'\b\w{4}\b', texto, flags=re.I))
print(10*'------')

#  se tirarmos as bordas, encontramemos palavras cortadas: r'\w{4}'
print(re.findall(r'\w{4}', texto, flags=re.I))
print(10*'------')

# ex: se queremos encontrar o começo de uma palavra, mas o restante dessa palavra não pode ter uma borda. ex: para encontrar o começo da palavra flores usamos r'flo\B'
print(re.findall(r'flo\B', texto, flags=re.A))
print(10*'------')
"""
