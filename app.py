import pyodbc
from time import sleep

print('\033[32m...conectando...\033[97m')

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
sleep(2)
print('conexao bem sucedida'
        '\n')

sleep(1)

print(15 * '-=')
print(f'register Dogs')
print(15 * '-=')

print('\n[h]elp para ajuda                |\n'
        '[r]egister para um novo registro |\n'
        '[v]iew para ver seus dados       |\n'
        '[S]air para fechar o programa    |\n')

while True:
    pergunta = str(input('o que deseja fazer?\n:')).upper()
    # nota : fazer uma classe que execute r , execute v e execute a
    if pergunta == 'H':
        # nota : colocar tupla com mensagem de ajuda com os comandos futuramente
        print('[h]elp para ajuda                |\n'
        '[r]egister para um novo registro |\n'
        '[v]iew para ver seus dados       |\n'
        '[S]air para fechar o programa    |\n')
        input('-')

    elif  pergunta == 'R':
        especie = str(input('especie:')).upper()
        nome = str(input('nome:'))
        sexo = str(input('sexo:')).upper()
        
        criar = (f'''insert into pets (id , especie , nome , sexo) values(default ,'{especie}','{nome}', '{sexo}')''')
        cursor.execute(criar)
        cursor.commit()
        sleep(1)
        print('sucesso')
        input('-')

    elif pergunta == 'V':
        nome = str(input('nome do pet:'))
        ver = (f'''select * from pets
            where nome = '{nome}'
            order by nome''')
        cursor.execute(ver)
        sleep(1)
        resposta=  cursor.fetchall()
        list(resposta)
        dados = [resposta[0][0], resposta[0][2], resposta[0][1], resposta[0][3]]
        print(20 * '-=')   
        print(f'''id:{dados[0]}\n'''
            f'nome:{dados[1]}\n'
            f'especie:{dados[2]}\n'
            f'sexo:{dados[3]}')
        print(20 * '-=')

        while True:
            print('[1]atualizar/[2]apagar registro/[3]sair')
            direcionamento = int(input(':'))
            if direcionamento == 1:
                print('[1]nome')
                mudança = int(input(':'))
                if mudança == 1:
                    novo_nome = str(input('novo nome:'))
                    atualizar = (f'''update pets set nome = '{novo_nome}' where id = {dados[0]} ''')
                    cursor.execute(atualizar)
                    cursor.commit()
                    sleep(1)
                    print('-atualizado-\n')
            elif direcionamento == 2:
                escolha = str(input('TEM CERTEZA?(S/N)')).upper()
                if escolha == 'S':
                    deletar = (f'''delete from pets where id = {dados[0]} ''')
                    cursor.execute(deletar)
                    cursor.commit()
                    print('...apagando seu registro...')
                    sleep(2)
                    print('Registro apagado')
                    break
                else:
                    print('\n')
            elif direcionamento == 3:
                break

        #if direcionamento == 3 or direcionamento == 2:
            #break

        else:
           print('\n') 


    elif pergunta == 'S':
        print('Ate logo(^^)\n'
              '\033[31m...fechando...\033[97m')
        sleep(2)
        break
    
    #else temporario
    else:
        c = 'select * from pets'
        cursor.execute(c)
        resposta = cursor.fetchall()
        list(resposta)
        for pos , r in enumerate(resposta):
            print(resposta[pos])
        input()




