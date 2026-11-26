import sqlite3

import banco
import queries
import tela
import utils
from crud import associacoes_crud, classes_crud, personagens_crud


def menu_personagens():
    while True:
        opcao = tela.menu("PERSONAGENS", ["Cadastrar", "Listar", "Pesquisar", "Alterar", "Excluir"])

        try:
            match opcao:
                case "1":
                    personagens_crud.cadastrar_personagem(*utils.ler_personagem())  # * entrega cada um ao parâmetro correspondente
                    tela.sucesso("Um novo herói surge no reino!")
                case "2":
                    tela.mostrar("Heróis do reino", personagens_crud.listar_personagens())
                case "3":
                    termo = utils.ler_texto("Buscar pelo nome: ")
                    tela.mostrar("Resultado da busca", personagens_crud.pesquisar_personagens(termo))
                case "4":
                    id_personagem = utils.ler_inteiro("Id do herói: ")
                    if personagens_crud.alterar_personagem(id_personagem, *utils.ler_personagem()):
                        tela.sucesso("Herói atualizado!")
                    else:
                        tela.erro("Herói não encontrado.")
                case "5":
                    if personagens_crud.excluir_personagem(utils.ler_inteiro("Id do herói: ")):
                        tela.sucesso("O herói partiu para sempre...")
                    else:
                        tela.erro("Herói não encontrado.")
                case "0":
                    break
                case _:
                    tela.erro("Opção inválida.")
        except sqlite3.IntegrityError as erro:
            tela.erro(f"O banco recusou: {erro}")


def menu_classes():
    while True:
        opcao = tela.menu("CLASSES", ["Cadastrar", "Listar", "Pesquisar", "Alterar", "Excluir"])

        try:
            match opcao:
                case "1":
                    classes_crud.cadastrar_classe(*utils.ler_classe())  # * entrega cada um ao parâmetro correspondente
                    tela.sucesso("Uma nova classe foi fundada!")
                case "2":
                    tela.mostrar("Classes do reino", classes_crud.listar_classes())
                case "3":
                    termo = utils.ler_texto("Buscar pelo nome: ")
                    tela.mostrar("Resultado da busca", classes_crud.pesquisar_classes(termo))
                case "4":
                    id_classe = utils.ler_inteiro("Id da classe: ")
                    if classes_crud.alterar_classe(id_classe, *utils.ler_classe()):
                        tela.sucesso("Classe atualizada!")
                    else:
                        tela.erro("Classe não encontrada.")
                case "5":
                    if classes_crud.excluir_classe(utils.ler_inteiro("Id da classe: ")):
                        tela.sucesso("A classe foi esquecida pelo tempo...")
                    else:
                        tela.erro("Classe não encontrada.")
                case "0":
                    break
                case _:
                    tela.erro("Opção inválida.")
        except sqlite3.IntegrityError as erro:
            tela.erro(f"O banco recusou: {erro}")


def menu_associacoes():
    while True:
        opcao = tela.menu("ASSOCIAÇÕES", ["Associar", "Desassociar", "Classes de um herói", "Heróis de uma classe"])

        try:
            match opcao:
                case "1":
                    associacoes_crud.associar(
                        utils.ler_inteiro("Id do herói: "),
                        utils.ler_inteiro("Id da classe: "),
                        utils.ler_inteiro("Nível de experiência: "),
                    )
                    tela.sucesso("O herói aprendeu uma nova classe!")
                case "2":
                    id_personagem = utils.ler_inteiro("Id do herói: ")
                    id_classe = utils.ler_inteiro("Id da classe: ")
                    if associacoes_crud.desassociar(id_personagem, id_classe):
                        tela.sucesso("O herói abandonou essa classe.")
                    else:
                        tela.erro("Esse herói não tem essa classe.")
                case "3":
                    id_personagem = utils.ler_inteiro("Id do herói: ")
                    tela.mostrar("Classes do herói", associacoes_crud.classes_do_personagem(id_personagem))
                case "4":
                    id_classe = utils.ler_inteiro("Id da classe: ")
                    tela.mostrar("Heróis da classe", associacoes_crud.personagens_da_classe(id_classe))
                case "0":
                    break
                case _:
                    tela.erro("Opção inválida.")
        except sqlite3.IntegrityError as erro:
            if "UNIQUE" in str(erro):
                tela.erro("Este herói já domina essa classe!")
            else:
                tela.erro("Herói ou classe não existe!")


def menu_consultas():
    while True:
        opcao = tela.menu("CONSULTAS", [
            "Fichas completas",
            "Resumo por classe",
            "Heróis por gênero",
            "Ranking de experiência",
            "Multiclasses",
            "Classes sem heróis",
        ])

        match opcao:
            case "1":
                tela.mostrar("Herói | Classe | XP", queries.fichas_completas())
            case "2":
                tela.mostrar("Classe | Heróis | Média de XP", queries.resumo_por_classe())
            case "3":
                tela.mostrar("Herói | Classe | Estilo", queries.herois_por_genero(utils.ler_genero()))
            case "4":
                tela.mostrar("Herói | XP total", queries.ranking_experiencia())
            case "5":
                tela.mostrar("Herói | Qtd | Classes", queries.multiclasses())
            case "6":
                tela.mostrar("Classes sem heróis", queries.classes_vazias())
            case "0":
                break
            case _:
                tela.erro("Opção inválida.")


def main():
    tela.abertura()

    while True:
        opcao = tela.menu("MENU PRINCIPAL", ["Personagens", "Classes", "Associações", "Consultas"], zero="Sair")

        match opcao:
            case "1":
                menu_personagens()
            case "2":
                menu_classes()
            case "3":
                menu_associacoes()
            case "4":
                menu_consultas()
            case "0":
                tela.despedida()
                banco.conexao.close()
                break
            case _:
                tela.erro("Opção inválida.")


if __name__ == "__main__":
    main()
