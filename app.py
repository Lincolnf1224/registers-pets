
print('ola \n')

import pyodbc
dados_conexao = (
                 'driver={MySQL ODBC 8.0 ANSI Driver};'
                'server=localhost:3306;'
                'database=cadastro;'
                'uid=root;'
                'pwd=07112616LRAM#;'
                'charset=utf8mb4;'
 )

conexao = pyodbc.connect(dados_conexao)

print('conexao bem sucedida'
      '\n')

from time import sleep
sleep(2)

print('[h]elp para ajuda                |\n'
      '[r]egister para um novo registro |\n'
      '[v]iew para ver seus dados       |\n'
      '[a]lter para alterar seus dados  |')

pergunta = str(input('o que deseja fazer?'))

if pergunta == 'h':
    # nota : colocar tupla com mensagem de ajuda com os comandos futuramente
    print('[h]elp para ajuda                |\n'
      '[r]egister para um novo registro |\n'
      '[v]iew para ver seus dados       |\n'
      '[a]lter para alterar seus dados  |')

#elif  pergunta == 'r':
    #nome



