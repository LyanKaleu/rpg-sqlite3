import sqlite3


# Setup do banco
conexao = sqlite3.connect("rpg.db")
conexao.execute("PRAGMA foreign_keys=ON")
cursor = conexao.cursor()


# Criação das 3 tabelas principais
cursor.executescript("""
      CREATE TABLE IF NOT EXISTS personagens(
          id_personagem INTEGER PRIMARY KEY AUTOINCREMENT,
          nome_personagem VARCHAR(30),
          genero CHAR(1) NOT NULL CHECK (genero IN('M', 'F')),
          raca VARCHAR(30),
          atributos VARCHAR(80),
          habilidades VARCHAR(50)
      );                
""")

cursor.executescript("""
      CREATE TABLE IF NOT EXISTS classes(
          id_classe INTEGER PRIMARY KEY AUTOINCREMENT,
          nome_classe VARCHAR(30),
          descricao VARCHAR(100),
          pontos_vida INTEGER,
          pontos_resistencia INTEGER,
          estilo_de_jogo VARCHAR(30)
      );               
""")

cursor.executescript("""
      CREATE TABLE IF NOT EXISTS personagens_classes(
          id_personagem INTEGER NOT NULL,
          id_classe INTERGER NOT NULL,
          nivel_experiencia INTEGER,
          PRIMARY KEY(id_personagem, id_classe),
          FOREIGN KEY(id_personagem) REFERENCES personagens(id_personagem) ON DELETE CASCADE,
          FOREIGN KEY(id_classe) REFERENCES classes(id_classe) ON DELETE CASCADE
      );             
""")


# Inserindo os dados na tabela
cursor.executemany("INSERT INTO personagens VALUES(?,?,?,?,?)", [
    ("Lyra Vento-Lâmina","F","Elfo","Agilidade e sabedoria", "Tiro Certeiro"),
    ("Thorgar Martelo-de-Pedra","M","Anão","Constituição e Força", "Muralha de ferro"),
    ("Kaelen do Véu Rubro", "F", "Tiefling", "Inteligência e Feitiçaria", "Chamas Infernais")
])

cursor.executemany("INSERT INTO classes VALUES(?,?,?,?,?)", [
    ("Ladino", "Especialista em furtividade, agilidade, armadilhas e ataques precisos.", 9, 15, "Bater e correr"),
    ("Guerreiro", "Mestre no combate armado, uso de escudos e armaduras pesadas.", 14, 18, "Tanque"),
    ("Mago", "Artes arcanas, manipulação de energia elemental e sombria.", 7, 12, "Artilharia mágica")
])

cursor.executemany("INSERT INTO personagens_classes  VALUES(?,?,?)", [
    (1, 1, 12),
    (2, 2, 23),
    (3, 3, 14)
])


# Confirmar as alterações no banco
conexao.commit()


# Consultas no banco
cursor.execute("""
""")


cursor.execute("""
""")


cursor.execute("""
""")