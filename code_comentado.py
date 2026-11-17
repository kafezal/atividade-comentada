# de; samuel augusto da silva
# importar o módulo do sqlite
import sqlite3

# literalmente 'tente', sendo considerado pra realizar primeira este
try:
    # cria uma conexão
    banco = sqlite3.connect('banco.db')

    # cria um curso: o bagulho q segue as instruções dadas para o banco de dados
    cursor = banco.cursor()

    # bota o cursor pra criar um banco aluno onde tem: id_aluno comko inteiro; Nome como texto; idade como inteiro
    # email como texto
    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)")

    # vai botar o cursor pra inserir os dado(valores) na tabela alunos
    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (2, 'jheimes',25,'rick@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ")

    # vai confirmar a inserção para determinado banco(nesse caso o banco.db)
    banco.commit()

    # vai printar um texto dizendo q os dados foram adicionados
    print("Os dados foram adicionados com sucesso!!")

    # bota o cursor pra selecionar tudo na tabela aluno
    cursor.execute("Select *FROM aluno")

    # vai printar tudo o q o cursor esta com ele, nesse caso tudo da tabela aluno
    print(cursor.fetchall())

    # bota o cursor pra deletar os dados da fileira quando tiver na tabela aluno a idade = 20 
    cursor.execute("DELETE from aluno WHERE idade = 20")

    # bota pra confirmar a inserção das ações dadas no curso pra o banco de dados(banco.db)
    banco.commit()

    # vai fechar as ações que serão inseridas no banco de dados
    banco.close()

    # vai printar dizendo que os dados foram removidos com sucesso
    print("Os dados foram removidos com sucesso!!")

# sabe o Try, bom, se isso der errado vai basicamente vai ir pra cá, semelhante a um if e else
except sqlite3.Error as erro:

    # vai printar dizendo q houve erro
    print("Erro ao excluir: ", erro)
