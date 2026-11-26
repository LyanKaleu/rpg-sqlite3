TITULO = r"""
____  ____   ____
|  _ \|  _ \ / ___|
| |_) | |_) | |  _
|  _ <|  __/| |_| |
|_| \_\_|    \____|
"""


def abertura():
    print(TITULO)


def despedida():
    print("\nAté a próxima aventura!")


def menu(titulo, opcoes, zero="Voltar"):
    print(f"\n========== {titulo} ==========")

    for numero, opcao in enumerate(opcoes, start=1):
        print(f"  {numero} - {opcao}")
    print(f"  0 - {zero}")

    return input("Escolha: ").strip()


def mostrar(titulo, linhas):
    print(f"\n--- {titulo} ---")

    if not linhas:
        print("Nada encontrado!")

    for linha in linhas:
        print(" | ".join(str(campo) for campo in linha))
    pausar()


def sucesso(mensagem):
    print(f"\n[+] {mensagem}")


def erro(mensagem):
    print(f"\n[!] {mensagem}")


def pausar():
    input("\nPressione Enter para continuar...")
