create table dados(
codigo int not null auto_increment ,
datadenascimento varchar(13)  default 'Desconhecido' ,
pais varchar(30),
estado varchar(40),
dono varchar(30),
vacinado enum ('S' , 'N'),
primary key(codigo)
)




