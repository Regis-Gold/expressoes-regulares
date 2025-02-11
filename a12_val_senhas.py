# https://en.wikipedia.org/wiki/List_of_Unicode_characters
import re
from pprint import pprint

senha_forte_regexp = re.compile(
    r'^(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$', flags=re.M)

string = """
VÁLIDAS
dv}2NZ7B~3a.  
U4Cz[c9n9C?=  
s5y2]HY<8kZ`  
m}3Hf4~Bc^1B  
6}xgOyW^~X68  

SEM MINÚSCULAS
2[9UJ*3[JZ8:  
R6^4{Z96"CD<  
8N}7"^C`0KX7  
:4[A3B<UW5<0  
ZE~U4+3.F8_5

SEM MINÚSCULAS E NÚMEROS
{W{X=D?NP\|U
KS~>PJ?A#X,'
_){MBRG,;?SY
}XN(LP}~/Q>N
*?S_\"[XXOJY

SEM NÚMEROS CARACTERES E MINÚSCULAS
XTFHMVCYPMCI
NIGKVJXQYMON
OJQXUMHWEFJC
STYUVOVOJPUF
CJJDQJFVEXUU

QUANTIDADE INVÁLIDA (6)
4Yfa|8
3zY4|z
K4kh8`
bW77j*
V{3i9v
"""

pprint(senha_forte_regexp.findall(string))