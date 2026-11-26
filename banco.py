import sqlite3

# Setup do banco
conexao = sqlite3.connect("rpg.db")
conexao.execute("PRAGMA foreign_keys=ON")
cursor = conexao.cursor()


# Criação das 3 tabelas principais
cursor.executescript("""
    CREATE TABLE IF NOT EXISTS personagens(
        id_personagem INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_personagem TEXT NOT NULL UNIQUE,
        genero TEXT NOT NULL CHECK (genero IN('M', 'F')),
        raca TEXT NOT NULL,
        atributos TEXT,
        habilidades TEXT
    );                
""")


cursor.executescript("""
    CREATE TABLE IF NOT EXISTS classes(
        id_classe INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_classe TEXT NOT NULL UNIQUE,
        descricao TEXT,
        pontos_vida INTEGER NOT NULL,
        pontos_resistencia INTEGER NOT NULL,
        estilo_de_jogo TEXT
    );               
""")


cursor.executescript("""
    CREATE TABLE IF NOT EXISTS personagens_classes(
        id_personagem INTEGER NOT NULL,
        id_classe INTEGER NOT NULL,
        nivel_experiencia INTEGER NOT NULL DEFAULT 1,
        PRIMARY KEY(id_personagem, id_classe),
        FOREIGN KEY(id_personagem) REFERENCES personagens(id_personagem) ON DELETE CASCADE,
        FOREIGN KEY(id_classe) REFERENCES classes(id_classe) ON DELETE CASCADE
    );             
""")


ja_populado = cursor.execute("SELECT COUNT(*) FROM personagens").fetchone()[0] > 0

if not ja_populado:
    # Inserindo os dados na tabela
    cursor.executemany("INSERT INTO personagens (nome_personagem, genero, raca, atributos, habilidades) VALUES(?,?,?,?,?)", [
        ("Lyra Vento-Lâmina", "F", "Elfo", "Agilidade e sabedoria", "Tiro Certeiro"),
        ("Thorgar Martelo-de-Pedra", "M", "Anão", "Constituição e Força", "Muralha de ferro"),
        ("Kaelen do Véu Rubro", "F", "Tiefling", "Inteligência e Feitiçaria", "Chamas Infernais"),
        ("Astarion Presa-Pálida", "M", "Elfo", "Destreza e Carisma", "Ataque Furtivo"),
        ("Shadowheart da Noite Velada", "F", "Meio-Elfo", "Sabedoria e Constituição",  "Palavra Curativa"), 
        ("Thrall Martelo-da-Perdição", "M", "Orc", "Força e Sabedoria", "Fúria da Tempestade"),
        ("Lydia Escudo-Juramentado", "F", "Nórdico", "Força e Constituição", "Golpe de Escudo"),
    ])


    cursor.executemany("INSERT INTO classes (nome_classe, descricao, pontos_vida, pontos_resistencia, estilo_de_jogo) VALUES(?,?,?,?,?)", [
        ("Ladino", "Especialista em furtividade, agilidade, armadilhas e ataques precisos.", 9, 15, "Bater e correr"),
        ("Guerreiro", "Mestre no combate armado, uso de escudos e armaduras pesadas.", 14, 18, "Tanque"),
        ("Mago", "Artes arcanas, manipulação de energia elemental e sombria.", 7, 12, "Artilharia mágica"),
        ("Clérigo", "Servo de uma divindade, cura aliados e protege o grupo com fé.", 10, 14, "Suporte e cura"),
        ("Patrulheiro", "Caçador das terras selvagens, mestre do arco e do rastreio.", 11, 16, "Ataque à distância"),
        ("Xamã", "Canaliza os espíritos e os elementos da natureza.", 10, 13, "Controle elemental"),
        ("Bardo", "Usa música e palavras para encantar inimigos e inspirar aliados.", 8, 12, "Suporte e encantamento"),
    ])


    cursor.executemany("INSERT INTO personagens_classes (id_personagem, id_classe, nivel_experiencia) VALUES(?,?,?)", [
        (1, 1, 12),  # Lyra: Ladino
        (2, 2, 23),  # Thorgar: Guerreiro
        (3, 3, 14),  # Kaelen: Mago
        (1, 5, 8),   # Lyra: Patrulheiro (multiclasse)
        (2, 4, 6),   # Thorgar: Clérigo (multiclasse)
        (3, 1, 5),   # Kaelen: Ladino (multiclasse)
        (4, 1, 18),  # Astarion: Ladino
        (5, 4, 16),  # Shadowheart: Clérigo
        (6, 6, 25),  # Thrall: Xamã
        (6, 2, 20),  # Thrall: Guerreiro (multiclasse)
        (7, 2, 11),  # Lydia: Guerreiro
    ])


# Confirmar as alterações no banco
conexao.commit()
