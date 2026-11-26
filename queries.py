from banco import conexao


# 1. JOIN duplo pela associativa
def fichas_completas():
    return conexao.execute("""
        SELECT p.nome_personagem, c.nome_classe, pc.nivel_experiencia
        FROM personagens AS p
        JOIN personagens_classes AS pc ON pc.id_personagem = p.id_personagem
        JOIN classes AS c ON c.id_classe = pc.id_classe
        ORDER BY p.nome_personagem
    """).fetchall()


# 2. Agregação: COUNT + AVG com GROUP BY (o LEFT JOIN mostra classe sem ninguém)
def resumo_por_classe():
    return conexao.execute("""
        SELECT c.nome_classe,
            COUNT(pc.id_personagem) AS quantidade,
            COALESCE(ROUND(AVG(pc.nivel_experiencia), 1), 0) AS media_xp
        FROM classes AS c
        LEFT JOIN personagens_classes AS pc ON pc.id_classe = c.id_classe
        GROUP BY c.id_classe
        ORDER BY quantidade DESC
    """).fetchall()


# 3. Filtro digitado pelo usuário
def herois_por_genero(genero):
    return conexao.execute("""
        SELECT p.nome_personagem, c.nome_classe, c.estilo_de_jogo
        FROM personagens AS p
        JOIN personagens_classes AS pc ON pc.id_personagem = p.id_personagem
        JOIN classes AS c ON c.id_classe = pc.id_classe
        WHERE p.genero = ?
    """, (genero,)).fetchall()


# 4. Agregação: SUM + ORDER BY
def ranking_experiencia():
    return conexao.execute("""
        SELECT p.nome_personagem, SUM(pc.nivel_experiencia) AS xp_total
        FROM personagens AS p
        JOIN personagens_classes AS pc ON pc.id_personagem = p.id_personagem
        GROUP BY p.id_personagem
        ORDER BY xp_total DESC
    """).fetchall()


# 5. HAVING + GROUP_CONCAT
def multiclasses():
    return conexao.execute("""
        SELECT p.nome_personagem, COUNT(*) AS quantidade, GROUP_CONCAT(c.nome_classe, ', ') AS classes
        FROM personagens AS p
        JOIN personagens_classes AS pc ON pc.id_personagem = p.id_personagem
        JOIN classes AS c ON c.id_classe = pc.id_classe
        GROUP BY p.id_personagem
        HAVING COUNT(*) > 1
    """).fetchall()


# 6. LEFT JOIN + IS NULL
def classes_vazias():
    return conexao.execute("""
        SELECT c.nome_classe
        FROM classes AS c
        LEFT JOIN personagens_classes AS pc ON pc.id_classe = c.id_classe
        WHERE pc.id_personagem IS NULL
    """).fetchall()
