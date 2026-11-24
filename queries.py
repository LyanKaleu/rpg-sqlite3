import sqlite3

conexao = sqlite3.connect("rpg.db")
conexao.execute("PRAGMA foreign_keys=ON")
cursor = conexao.cursor()

# Consultas no banco
'''
# Pelo menos 3 consultas com JOIN. 
# Uma delas deve passar pela tabela associativa com dois JOINs, 
# e pelo menos uma deve usar agregação (COUNT, SUM, AVG com GROUP BY).
'''

cursor.execute("""
               SELECT p.nome_personagem,  c.nome_classe, pc.nivel_experiencia
               FROM personagens AS p
               JOIN personagens_classes AS pc ON pc.id_personagem = p.id_personagem
               JOIN classes AS c ON pc.id_classe = c.id_classe;
""")

print("CONSULTA 1: Personagens, classes e nível de experiência ")
for linha in cursor.fetchall():
    print(linha)

print("\n\n")


cursor.execute("""
               SELECT c.nome_classe, COUNT(pc.id_personagem) AS quantidade_personagens
               FROM classes AS c
               LEFT JOIN personagens_classes AS pc ON pc.id_classe = c.id_classe
               GROUP BY c.id_classe, c.nome_classe;
""")

print("CONSULTA 2: Quantidade de personagens por classe")
for linha in cursor.fetchall():
    print(linha)

print("\n\n")

cursor.execute("""
               SELECT p.nome_personagem, c.nome_classe, c.estilo_de_jogo
               FROM personagens AS p
               JOIN personagens_classes AS pc ON pc.id_personagem = p.id_personagem
               JOIN classes AS c ON c.id_classe = pc.id_classe
               WHERE p.genero = 'F';
""")


print("CONSULTA 3: Personagens do gênero feminino e o estilo de jogo de sua classe")
for linha in cursor.fetchall():
    print(linha)

print("\n\n")