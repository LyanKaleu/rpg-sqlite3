from banco import conexao


# CREATE 
def cadastrar_classe(nome, descricao, pontos_vida, pontos_resistencia, estilo_de_jogo):
    cursor = conexao.execute("""
        INSERT INTO classes (nome_classe, descricao, pontos_vida, pontos_resistencia, estilo_de_jogo)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, descricao, pontos_vida, pontos_resistencia, estilo_de_jogo)
    )

    conexao.commit()
    return cursor.lastrowid


# READ
def listar_classes():
    return conexao.execute("SELECT * FROM classes ORDER BY id_classe").fetchall()


# UPDATE
def alterar_classe(id_classe, nome, descricao, pontos_vida, pontos_resistencia, estilo_de_jogo):
    cursor = conexao.execute("""
        UPDATE classes 
        SET nome_classe = ?, descricao = ?, pontos_vida = ?, pontos_resistencia = ?, estilo_de_jogo = ?
        WHERE id_classe = ?""", 
        (nome, descricao, pontos_vida, pontos_resistencia, estilo_de_jogo, id_classe)
    )
    conexao.commit()
    return cursor.rowcount


# DELETE
def excluir_classe(id_classe):
    cursor = conexao.execute("DELETE FROM classes WHERE id_classe = ?", (id_classe,))
    conexao.commit()
    return cursor.rowcount  # 0 = id não existe


# Buscar pelo nome
def pesquisar_classes(termo):
    return conexao.execute("SELECT * FROM classes WHERE nome_classe LIKE ?", (f"%{termo}%",)).fetchall()
