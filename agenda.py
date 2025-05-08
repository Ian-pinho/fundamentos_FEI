MENU = {
    1: "Novo contato",
        2: "Procurar contato",
        3: "Atualizar contato",
        4: "Apagar contato",
        0: "Sair"
}
def main():
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            novo_contato()
        elif opcao == 2:
            procurar_contato()
        elif opcao == 3:
            atualizar_contato()
        elif opcao == 4:
            apagar_contato()
        elif opcao == 0:
            sair()
            break
        else:
            print("Opção inválida. Tente novamente.")
def exibir_menu():
        for opcao, descricao in MENU.items():
            print(f"{opcao} - {descricao}")

def novo_contato():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    with open("contatos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{sobrenome},{telefone},{email}\n")
    
    print("Contato adicionado com sucesso!")

def procurar_contato():
    nome_procurado = input("Digite o nome a ser pesquisado: ")
    with open("contatos.txt", "r") as arquivo:
        contatos = arquivo.readlines()
    for contato in contatos:
        nome, sobrenome, telefone, email = contato.strip().split(",")
        if nome.lower() == nome_procurado.lower():
            print(f"Nome: {nome}, Sobrenome: {sobrenome}, Telefone: {telefone}, email: {email}")
            break
        else:
            print("Contato não encontrado.")

def atualizar_contato():
    nome_procurado = input("Digite o nome a ser pesquisado: ")
    with open("contatos.txt", "r") as arquivo:
        contatos = arquivo.readlines()
    for i, contato in enumerate(contato):
        nome, sobrenome, telefone, email = contato.strip().split(",")
        if nome.lower() == nome_procurado.lower():
            print(f"Contato encontrado: {contato.strip()}")
            novo_nome = input("Digite o novo nome: ")
            novo_sobrenome = input("Digite o novo sobrenome: ")
            novo_telefone = input("Digite o novo telefone: ")
            novo_email = input("Digite o novo email: ")

            contatos[i] = f"{novo_nome},{novo_sobrenome},{novo_telefone},{novo_email}\n"
            break
    else:
        print("Contato não encontrado.")

def apagar_contato():
    nome_procurado = input("Digite o nome a ser pesquisado: ")
    with open("contatos.txt", "r") as arquivo:
        contatos = arquivo.readlines()
    for i, contato in enumerate(contato):
        nome, sobrenome, telefone, email = contato.strip().split(",")
        if nome.lower() == nome_procurado.lower():
            print(f"Contato encontrado: {contato.strip()}")
            contatos.pop(i)
            break
        else:
            print("Contato não encontrado.")
    with open("contatos.txt", "w") as arquivo:
        arquivo.writelines(contatos)

def sair():
    pass

if __name__ == "__main__":
    main()
