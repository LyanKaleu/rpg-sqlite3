import tela


# Funções de validação de entrada
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            tela.erro("Isso não é um número, aventureiro!")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto:
            return texto
        tela.erro("Este campo não pode ficar vazio!")


def ler_genero():
    while True:
        genero = input("Gênero (M/F): ").strip().upper()

        if genero in ("M", "F"):
            return genero
        tela.erro("Digite apenas M ou F!")


def ler_personagem():
    nome = ler_texto("Nome do herói: ")
    genero = ler_genero()
    raca = ler_texto("Raça: ")
    atributos = input("Atributos (opcional): ").strip()
    habilidades = input("Habilidades (opcional): ").strip()

    return nome, genero, raca, atributos, habilidades


def ler_classe():
    nome = ler_texto("Nome da classe: ")
    descricao = input("Descrição (opcional): ").strip()
    pontos_vida = ler_inteiro("Pontos de vida: ")
    pontos_resistencia = ler_inteiro("Pontos de resistência: ")
    estilo_de_jogo = input("Estilo de jogo (opcional): ").strip()

    return nome, descricao, pontos_vida, pontos_resistencia, estilo_de_jogo
