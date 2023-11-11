#classe para coneçao 

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

#funçao para criar dados
  #cursor.commit() edita o banco de dados


#funçao para ler um dado
  #id = int(input('coloque um id'))

  #comando = f'select nome from gafanhotos where id = {id}'
  #cursor.execute(comando)
  #resposta = cursor.fetchall()
  #print(resposta)



#funçao para inserir dados


#funçao para ler dados


#funçao para deletar dados


#funçao para desligar o servidor
  #cursor.close()
  #conexao.close()