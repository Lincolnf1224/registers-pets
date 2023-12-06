print('ola \n')

import pyodbc
dados_conexao = (
                 'driver={MySQL ODBC 8.0 ANSI Driver};'
                'server=localhost:3306;'
                'database=petshop;'
                'uid=root;'
                'pwd=07112616LRAM#;'
                'charset=utf8mb4;'
 )

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

print('conexao bem sucedida'
      '\n')

from time import sleep
sleep(0)

pergunta = str(input('o que deseja fazer?'))

if pergunta == 'h':
    # nota : colocar tupla com mensagem de ajuda com os comandos futuramente
    print('[h]elp para ajuda                |\n'
      '[r]egister para um novo registro |\n'
      '[v]iew para ver seus dados       |\n'
      '[a]lter para alterar seus dados  |')

elif  pergunta == 'r':
    # nota : fazer uma classe que execute r , execute v e execute a

    especie = str(input('especie:')).upper()
    nome = str(input('nome:'))
    sexo = str(input('sexo:')).upper()
    
    criar = (f'''insert into pets (id , especie , nome , sexo) values(default ,'{especie}','{nome}', '{sexo}')''')
    cursor.execute(criar)
    cursor.commit()
    print('sucesso')

#else temporario
else:
    c = 'select * from pets'
    cursor.execute(c)
    resposta = cursor.fetchall()
    print(resposta)





