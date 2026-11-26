from banco import conexao


# CREATE 
def cadastrar_personagem(nome, genero, raca, atributos, habilidades):
    cursor = conexao.execute("""
        INSERT INTO personagens (nome_personagem, genero, raca, atributos, habilidades)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, genero, raca, atributos, habilidades),
    )

    conexao.commit()
    return cursor.lastrowid


# READ
def listar_personagens():
    return conexao.execute("SELECT * FROM personagens ORDER BY id_personagem").fetchall()


# UPDATE
def alterar_personagem(id_personagem, nome, genero, raca, atributos, habilidades):
    cursor = conexao.execute("""
        UPDATE personagens 
        SET nome_personagem = ?, genero = ?, raca = ?, atributos = ?, habilidades = ?
        WHERE id_personagem = ?""", 
        (nome, genero, raca, atributos, habilidades, id_personagem,)
    )
    conexao.commit()
    return cursor.rowcount


# DELETE
def excluir_personagem(id_personagem):
    cursor = conexao.execute("DELETE FROM personagens WHERE id_personagem = ?", (id_personagem,))
    conexao.commit()
    return cursor.rowcount  # 0 = id não existe


# Buscar pelo nome
def pesquisar_personagens(termo):
    return conexao.execute("SELECT * FROM personagens WHERE nome_personagem LIKE ?", (f"%{termo}%",)).fetchall()
