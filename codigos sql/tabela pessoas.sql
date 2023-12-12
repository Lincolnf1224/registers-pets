create table pessoas(
id int auto_increment not null,
nome varchar(30) not null,
email varchar(40),
senha int ,
data_de_nascimento date,
sexo enum ('F' , 'M'),
primary key(id)
)


