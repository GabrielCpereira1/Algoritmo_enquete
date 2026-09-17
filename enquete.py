opcoes = []
votos = []


def cadastrar_opcao():
    opcao = input("Digite a opção que deseja cadastrar: ")
    opcoes.append(opcao)
    votos.append(0)
    print("Opção cadastrada com sucesso!")


def listar_opcoes():
    if len(opcoes) == 0:
        print("Nenhuma opção cadastrada.")
    else:
        print("\n--- OPÇÕES CADASTRADAS ---")
        for i, opcao in enumerate(opcoes, start=1):
            print(i, "-", opcao)


def registrar_voto():
    if len(opcoes) == 0:
        print("Nenhuma opção cadastrada.")
        return

    listar_opcoes()

    escolha = int(input("Digite o número da opção que deseja votar: "))

    if escolha >= 1 and escolha <= len(opcoes):
        votos[escolha - 1] += 1
        print("Voto registrado com sucesso!")
    else:
        print("Opção inválida!")


def consultar_votos():
    if len(opcoes) == 0:
        print("Nenhuma opção cadastrada.")
    else:
        print("\n--- QUANTIDADE DE VOTOS ---")
        for i, opcao in enumerate(opcoes):
            print(opcao, "-", votos[i], "votos")


def mostrar_resultado():
    if len(opcoes) == 0:
        print("Nenhuma opção cadastrada.")
        return

    total_votos = sum(votos)

    if total_votos == 0:
        print("Nenhum voto registrado.")
    else:
        print("\n--- RESULTADO DA ENQUETE ---")

        for i, opcao in enumerate(opcoes):
            percentual = (votos[i] / total_votos) * 100

            print(
                opcao,
                "-",
                votos[i],
                "votos -",
                round(percentual, 2),
                "%"
            )

        print("Total de votos:", total_votos)


def mostrar_vencedora():
    if len(opcoes) == 0:
        print("Nenhuma opção cadastrada.")
        return

    total_votos = sum(votos)

    if total_votos == 0:
        print("Nenhum voto registrado.")
        return

    maior_voto = max(votos)
    vencedoras = []

    for i in range(len(opcoes)):
        if votos[i] == maior_voto:
            vencedoras.append(opcoes[i])

    if len(vencedoras) == 1:
        print(
            "Opção vencedora:",
            vencedoras[0],
            "com",
            maior_voto,
            "votos."
        )
    else:
        print("Houve empate entre:")

        for opcao in vencedoras:
            print("-", opcao)

        print("Cada opção recebeu", maior_voto, "votos.")


def menu():
    while True:
        print("\n===== ENQUETE =====")
        print("1 - Cadastrar opção")
        print("2 - Listar opções")
        print("3 - Registrar voto")
        print("4 - Consultar quantidade de votos")
        print("5 - Mostrar resultado")
        print("6 - Mostrar opção vencedora")
        print("7 - Encerrar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_opcao()

        elif escolha == "2":
            listar_opcoes()

        elif escolha == "3":
            registrar_voto()

        elif escolha == "4":
            consultar_votos()

        elif escolha == "5":
            mostrar_resultado()

        elif escolha == "6":
            mostrar_vencedora()

        elif escolha == "7":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


menu()
