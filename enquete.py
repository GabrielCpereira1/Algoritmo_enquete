opcoes = []

def cadastrar_opcao():
    opcao = input("Cadastrar opcão: ")
    opcoes.append(opcao)

cadastrar_opcao()
continuar = input("Deseja cadastrar outra opção? (s/n): ")
while continuar == "s":
    cadastrar_opcao()
    continuar = input("Deseja cadastrar outra opção? (s/n): ")

def listar_opcoes():
    for i, opcao in enumerate(opcoes, start=1):
        print(i,opcao)

listar_opcoes()


