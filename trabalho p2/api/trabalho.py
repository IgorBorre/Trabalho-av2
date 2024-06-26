import mysql.connector
from flask import Flask, jsonify


conexao = mysql.connector.connect(
    host='172.19.0.2',
    port='3306',
    user='root',
    password='masterkey',
    database='escola',
)

cursor = conexao.cursor()

app = Flask(__name__)


@app.route('/escola/curso', methods=['GET'])

def obterCurso():
    cursor.execute('SELECT * FROM Curso')
    return cursor.fetchall()


@app.route('/escola/curso/<int:id>', methods=['GET'])
def obterCursobyid(id):
    cursor.execute('SELECT * from Curso where idCurso = %s', [id])
    return cursor.fetchall()


@app.route('/escola/curso/add/<string:nome>/<int:horas>/<string:local>/<int:idProfessor>', methods=['POST'])
def addCurso(nome, horas, local, idProfessor):
    cursor.execute('INSERT INTO Curso (nomeCurso, horas, localizacao, idProfessor) values (%s, %s, %s, %s)', [nome, horas, local, idProfessor])
    conexao.commit()
    cursor.execute('SELECT * FROM Curso')
    return cursor.fetchall()


@app.route('/escola/curso/update/<int:id>/<string:nome>/<int:horas>/<string:local>/<int:idProfessor>', methods=['PUT'])
def attCurso(id, nome, horas, local, idProfessor):
    cursor.execute('UPDATE Curso set nomeCurso = %s, horas = %s, localizacao = %s, idProfessor = %s WHERE idCurso = %s', [nome, horas, local, idProfessor, id])
    conexao.commit()
    cursor.execute('SELECT * FROM Curso')
    return cursor.fetchall()


@app.route('/escola/curso/delete/<int:id>', methods=['DELETE'])
def excluiCurso(id):
    cursor.execute('DELETE FROM Curso where idCurso = %s', [id])
    conexao.commit()
    cursor.execute('SELECT * FROM Curso')
    return cursor.fetchall()


@app.route('/escola/aluno')
def obterAluno():
    cursor.execute('SELECT * FROM Aluno')
    return cursor.fetchall()


@app.route('/escola/aluno/add/<string:nome>/<int:matricula>/<int:idcurso>', methods=['POST'])
def addAluno(nome, matricula, idcurso):
    cursor.execute('INSERT INTO Aluno (nomeAluno, matricula, idCurso) VALUES (%s, %s, %s)', [nome, matricula, idcurso])
    conexao.commit()
    cursor.execute('SELECT * FROM Aluno')
    return cursor.fetchall()


@app.route('/escola/aluno/delete/<int:id>', methods=['DELETE'])
def excluiAluno(id):
    cursor.execute('DELETE FROM Aluno Where idAluno = %s', [id])
    conexao.commit()
    cursor.execute('SELECT * FROM Aluno')
    return cursor.fetchall()


@app.route('/escola/aluno/<int:id>')
def obterAlunobyid(id):
    cursor.execute('SELECT * FROM Aluno WHERE idAluno = %s', [id])
    return cursor.fetchall()


@app.route('/escola/aluno/update/<int:id>/<string:nome>/<int:matricula>/<int:idcurso>', methods=['PUT'])
def updateAluno(id, nome, matricula, idcurso):
    cursor.execute('UPDATE Aluno SET nomeAluno = %s, matricula = %s, idCurso = %s WHERE idAluno = %s', [nome, matricula, idcurso, id])
    conexao.commit()
    cursor.execute('SELECT * FROM Aluno')
    return cursor.fetchall()

@app.route('/escola/professor')
def obterProfessor():
    cursor.execute('SELECT * FROM Professor')
    return cursor.fetchall()


@app.route('/escola/professor/add/<string:nome>/<int:salario>', methods=['POST'])
def addProfessor(nome, salario):
    cursor.execute('INSERT INTO Professor (nomeProfessor, salario) VALUES (%s, %s)', [nome, salario])
    conexao.commit()
    cursor.execute('SELECT * FROM Professor')
    return cursor.fetchall()


@app.route('/escola/professor/delete/<int:id>', methods=['DELETE'])
def excluiProfessor(id):
    cursor.execute('DELETE FROM Professor Where idProfessor = %s', [id])
    conexao.commit()
    cursor.execute('SELECT * FROM Professor')
    return cursor.fetchall()


@app.route('/escola/professor/<int:id>')
def obterProfessorbyid(id):
    cursor.execute('SELECT * FROM Professor WHERE idProfessor = %s', [id])
    return cursor.fetchall()


@app.route('/escola/professor/update/<int:id>/<string:nome>/<int:salario>', methods=['PUT'])
def updateProfessor(id, nome, salario):
    cursor.execute('UPDATE Professor SET nomeProfessor = %s, salario = %s WHERE idProfessor = %s', [nome, salario, id])
    conexao.commit()
    cursor.execute('SELECT * FROM Professor')
    return cursor.fetchall()


app.run(port = 5000, host = '0.0.0.0', debug = True)


cursor.close()
conexao.close()