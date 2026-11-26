from banco import conexao


# CREATE
def associar(id_personagem, id_classe, nivel_experiencia):
    conexao.execute("""
        INSERT INTO personagens_classes (id_personagem, id_classe, nivel_experiencia)
        VALUES (?, ?, ?)
        """, (id_personagem, id_classe, nivel_experiencia)
    )
    conexao.commit()


# DELETE
def desassociar(id_personagem, id_classe):
    cursor = conexao.execute(
        "DELETE FROM personagens_classes WHERE id_personagem = ? AND id_classe = ?",
        (id_personagem, id_classe),
    )
    conexao.commit()

    return cursor.rowcount


def classes_do_personagem(id_personagem):
    return conexao.execute("""
        SELECT c.id_classe, c.nome_classe, pc.nivel_experiencia
        FROM personagens_classes AS pc
        JOIN classes AS c ON c.id_classe = pc.id_classe
        WHERE pc.id_personagem = ?
    """, (id_personagem,)
    ).fetchall()


def personagens_da_classe(id_classe):
    return conexao.execute("""
            SELECT p.id_personagem, p.nome_personagem, pc.nivel_experiencia
            FROM personagens_classes AS pc
            JOIN personagens AS p ON p.id_personagem = pc.id_personagem
            WHERE pc.id_classe = ?
        """, (id_classe,)
        ).fetchall()
