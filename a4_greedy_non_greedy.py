# Meta caracteres: ^ $ ( )
#` * 0 ou n
#` + 1 ou n
#` ? 0 ou 1

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''

# para encontrarmos p e div devemos cololar dentro do conjunto [] independente da ordem, depois usamos um quantidicador de {1,3},
print(re.findall(r'<[vidp]{1,3}>', texto))

# aqui pegaremos o . que pode repetir 0 ou n vezes, usaremos o dotall que seria.*
# esse resultado é re meio ambigua, pois ela não sabe ao certo onde é o fechamento da tag, esse é o comportamento greedy
print(re.findall(r'<[vidp]{1,3}>.*', texto))
print(re.findall(r'<[vidp]{1,3}>.*<[\/vidp]{1,3}>', texto))

# Para que o comportamento seja non greedy ou lazy fazemos a re da seguinte forma

#` * 0 ou n
print(re.findall(r'<[vidp]{1,3}>.*?<\/[vidp]{1,3}>', texto))

#` + 1 ou n
print(re.findall(r'<[vidp]{1,3}>.+?<\/[vidp]{1,3}>', texto))