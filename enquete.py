opcoes = []
votos = []


def cadastrar_opcao():
    opcao = input("Cadastrar opção: ")
    opcoes.append(opcao)
    votos.append(0)


cadastrar_opcao()
continuar = input("Deseja cadastrar outra opção? (s/n): ")

while continuar == "s":
    cadastrar_opcao()
    continuar = input("Deseja cadastrar outra opção? (s/n): ")


def listar_opcoes():
    for i, opcao in enumerate(opcoes, start=1):
        print(i, opcao)


listar_opcoes()


def registrar_voto():
    listar_opcoes()

    escolha = int(input("Digite o número da opção que deseja votar: "))

    if escolha >= 1 and escolha <= len(opcoes):
        votos[escolha - 1] += 1
        print("Voto registrado com sucesso!")
    else:
        print("Opção inválida!")


def consultar_votos():
    for i, opcao in enumerate(opcoes):
        print(opcao, "-", votos[i], "votos")


def mostrar_resultado():
    total_votos = sum(votos)

    if total_votos == 0:
        print("Nenhum voto registrado.")
    else:
        for i, opcao in enumerate(opcoes):
            percentual = (votos[i] / total_votos) * 100
            print(opcao, "-", votos[i], "votos -", round(percentual, 2), "%")
