import re
### VALIDANDO CPF E IP ###

"""
Válidando CPF:
- são números que podem ou não começar com 0
- precisamos saber se tem 3 números na 1º, 2º e 3º casa, e na última se tem 2 números
- 025.258.963-10 

1 - re.compile compilar a re
2 - os sinais de ^ e $ para válidar um campo
3 - usamos o \d para pegar os números
4 - {3} ou {2} para sequência de 3 ou 2 num
5 - \. para fazermos o escape do .
"""

cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
print(cpf_reg_exp.search(cpf))
print(10* '-----')

"""
Validando IP:
- precisamos criar um range de 0 a 255
- 0.0.0.0 
- 255.255.255.255

1 - o range é 0.0.0.0 até 255.255.255.255
2 - faremos um for in com 300 IPs
3 - i é o index
4 - 301 é o range para pegarmos 300 IPs
5 - ip é uma varialvel
6 - print (ip) mostrará o range completo

- os sinais de ^ e $ para válidar um campo
- criamos um grupo dentro da re ()
- esse grupo não precisa ser salvo (?:)
- flags=re.X para comentar dentro da re
- dividimos o range com |
- 250-255 | 200-249 | 100-199 | 10-99 | 0-9
- fora do grupo colocamos \. para IP valid
- repetimos 4 vezes para validar o IP inteiro
- chamamos re ip_reg_exp.findall(ip) no for
- assim encontramos o range validado
"""

ip_reg_exp = re.compile(r'''
    ^
    (?:
    25[0-5]| # 250-255
    2[0-4][0-9]| # 200-249
    1[0-9]{2}| # 100-199
    [1-9][0-9]| # 10-99
    [0-9] # 0-9
    )
    \.
    (?:
    25[0-5]| # 250-255
    2[0-4][0-9]| # 200-249
    1[0-9]{2}| # 100-199
    [1-9][0-9]| # 10-99
    [0-9] # 0-9
    )
    \.
    (?:
    25[0-5]| # 250-255
    2[0-4][0-9]| # 200-249
    1[0-9]{2}| # 100-199
    [1-9][0-9]| # 10-99
    [0-9] # 0-9
    )
    \.
    (?:
    25[0-5]| # 250-255
    2[0-4][0-9]| # 200-249
    1[0-9]{2}| # 100-199
    [1-9][0-9]| # 10-99
    [0-9] # 0-9
    )
    $
''', flags=re.X)

# Exemplo 2
# colocamos toda e re dentro de um grupo maior, que também não precisamos salvar (?:
# depois de fechar o grupo 2 usamos \.? para tornar o . opcional
# usamos {4} para repetir o grupo 4 vezes
# depois usamos \b e fechamos com $

ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5]| # 250-255
            2[0-4][0-9]| # 200-249
            1[0-9]{2}| # 100-199
            [1-9][0-9]| # 10-99
            [0-9] # 0-9
        )
        \.?
    ){4}
    \b
    $
''', flags=re.X)

# versão compacta
ip_reg_exp = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))