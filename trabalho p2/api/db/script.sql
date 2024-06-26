create database escola;

use escola;

create table Professor(
idProfessor int primary key AUTO_INCREMENT,
nomeProfessor varchar(50),
salario int
);

create table Curso(
idCurso int primary key AUTO_INCREMENT,
nomeCurso varchar(50) unique,
horas int,
localizacao varchar(50),
idProfessor int,
foreign key (idProfessor) references Professor(idProfessor)
);

create table Aluno(
idAluno int primary key AUTO_INCREMENT,
nomeAluno varchar(50),
matricula int unique,
idCurso int,
foreign key (idCurso) references Curso(idCurso)
);

INSERT INTO Professor (idProfessor, nomeProfessor, salario) VALUES (1, 'teste', 1000);

