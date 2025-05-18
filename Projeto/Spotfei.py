# Spotifei - Projeto do primeiro semestre de ciências da computação na FEI

import os

Usuarios = "usuarios.txt"
Musicas = "musicas.txt"
Historico = "historico.txt"

# Inicializa os arquivos caso não existam
for arquivo in [Usuarios, Musicas, Historico]:
    if not os.path.exists(arquivo):
        open(arquivo, "w").close()

# Menu principal
menu_principal = {
    1: "Registrar novo usuário",
    2: "Login",
    0: "Sair"
}

# Menu do usuário
menu_usuario = {
    1: "Buscar música",
    2: "Curtir música",
    3: "Descurtir música",
    4: "Visualizar informações da música",
    5: "Gerenciar playlists",
    6: "Visualizar histórico",
    0: "Logout"
}

# Loop principal

def main():
    usuario_logado = None
    while True:
        if not usuario_logado:
            escolha = exibir_menu(menu_principal)
            if escolha == 1:
                registrar_usuario()
            elif escolha == 2:
                usuario_logado = login()
            elif escolha == 0:
                sair()
            else:
                print("Opção inválida.")
        else:
            escolha = exibir_menu(menu_usuario)
            if escolha == 1:
                buscar_musica()
            elif escolha == 2:
                curtir_musica(usuario_logado)
            elif escolha == 3:
                descurtir_musica(usuario_logado)
            elif escolha == 4:
                visualizar_info_musica()
            elif escolha == 5:
                gerenciar_playlists(usuario_logado)
            elif escolha == 6:
                visualizar_historico(usuario_logado)
            elif escolha == 0:
                usuario_logado = None
            else:
                print("Opção inválida.")

# Exibe menu e retorna escolha

def exibir_menu(menu):
    print("\nMenu:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = input("Escolha uma opção: ")
    if escolha.isdigit():
        return int(escolha)
    return -1

# Registro de novos usuários

def registrar_usuario():
    print("Registrar novo usuário:")
    nome_usuario = input("Digite o nome de usuário: ").strip()
    senha_usuario = input("Digite a senha: ").strip()
    with open(Usuarios, "r") as arquivo:
        for linha in arquivo:
            nome_salvo, _ = linha.strip().split(",")
            if nome_usuario == nome_salvo:
                print("Usuário já existe.")
                return
    with open(Usuarios, "a") as arquivo:
        arquivo.write(f"{nome_usuario},{senha_usuario}\n")
    print("Usuário registrado com sucesso!")

# Login de usuários existentes

def login():
    print("Login:")
    nome_usuario = input("Digite o nome de usuário: ").strip()
    senha_usuario = input("Digite a senha: ").strip()
    with open(Usuarios, "r") as arquivo:
        for linha in arquivo:
            nome_salvo, senha_salva = linha.strip().split(",")
            if nome_usuario == nome_salvo and senha_usuario == senha_salva:
                print("Login bem-sucedido!")
                return {"nome": nome_usuario}
    print("Usuário ou senha incorretos.")
    return None

# Verifica se música existe

def verificar_musica_existente(titulo_musica):
    with open(Musicas, "r") as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(",")
            titulo, artista, curtidas, descurtidas = campos
            if titulo.lower() == titulo_musica.lower():
                return titulo, artista, curtidas, descurtidas
    return None

# Busca de músicas por título

def buscar_musica():
    print("Buscar música:")
    termo_busca = input("Digite o nome da música: ").lower()
    encontrado = False
    with open(Musicas, "r") as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(",")
            titulo, artista, curtidas, descurtidas = campos
            if termo_busca in titulo.lower():
                print(f"Título: {titulo}, Artista: {artista}")
                encontrado = True
    if not encontrado:
        print("Nenhuma música encontrada.")

# Curtir música e salvar no histórico

def curtir_musica(usuario):
    print("Curtir música:")
    titulo_musica = input("Digite o título da música: ").strip()
    if not verificar_musica_existente(titulo_musica):
        print("Música não encontrada.")
        return
    musicas = []
    with open(Musicas, "r") as arquivo:
        musicas = arquivo.readlines()
    with open(Musicas, "w") as arquivo:
        for linha in musicas:
            campos = linha.strip().split(",")
            titulo, artista, curtidas, descurtidas = campos
            if titulo.lower() == titulo_musica.lower():
                curtidas = str(int(curtidas) + 1)
                print(f"Você curtiu: {titulo} - {artista}")
                salvar_historico(usuario["nome"], f"Curtiu: {titulo} - {artista}")
            arquivo.write(f"{titulo},{artista},{curtidas},{descurtidas}\n")

# Descurtir música e salvar no histórico

def descurtir_musica(usuario):
    print("Descurtir música:")
    titulo_musica = input("Digite o título da música: ").strip()
    if not verificar_musica_existente(titulo_musica):
        print("Música não encontrada.")
        return
    musicas = []
    with open(Musicas, "r") as arquivo:
        musicas = arquivo.readlines()
    with open(Musicas, "w") as arquivo:
        for linha in musicas:
            campos = linha.strip().split(",")
            titulo, artista, curtidas, descurtidas = campos
            if titulo.lower() == titulo_musica.lower():
                descurtidas = str(int(descurtidas) + 1)
                print(f"Você descurtiu: {titulo} - {artista}")
                salvar_historico(usuario["nome"], f"Descurtiu: {titulo} - {artista}")
            arquivo.write(f"{titulo},{artista},{curtidas},{descurtidas}\n")

# Exibe detalhes da música

def visualizar_info_musica():
    print("Informações da música:")
    titulo_musica = input("Digite o título da música: ").strip()
    dados = verificar_musica_existente(titulo_musica)
    if dados:
        titulo, artista, curtidas, descurtidas = dados
        print(f"\nTítulo: {titulo}\nArtista: {artista}\nCurtidas: {curtidas}\nDescurtidas: {descurtidas}")
    else:
        print("Música não encontrada.")

# Gerenciamento de playlists

def gerenciar_playlists(usuario):
    nome_playlist = input("Nome da playlist: ").strip()
    nome_arquivo_playlist = f"playlist_{usuario['nome']}_{nome_playlist}.txt"
    print("\n1 - Criar/Resetar playlist")
    print("2 - Adicionar música à playlist")
    print("3 - Remover música da playlist")
    print("4 - Exibir playlist")
    print("5 - Excluir playlist")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        open(nome_arquivo_playlist, "w").close()
        print("Playlist criada/reinicializada.")
    elif opcao == "2":
        musica_para_adicionar = input("Digite o nome da música para adicionar: ").strip()
        if verificar_musica_existente(musica_para_adicionar):
            with open(nome_arquivo_playlist, "a") as arquivo:
                arquivo.write(musica_para_adicionar + "\n")
            print("Música adicionada à playlist.")
        else:
            print("Música não encontrada. Só é possível adicionar músicas existentes.")
    elif opcao == "3":
        musica_para_remover = input("Digite o nome da música para remover: ").strip()
        if os.path.exists(nome_arquivo_playlist):
            with open(nome_arquivo_playlist, "r") as arquivo:
                linhas_playlist = arquivo.readlines()
            with open(nome_arquivo_playlist, "w") as arquivo:
                for linha in linhas_playlist:
                    if linha.strip().lower() != musica_para_remover.lower():
                        arquivo.write(linha)
            print("Música removida da playlist.")
        else:
            print("Playlist não encontrada.")
    elif opcao == "4":
        if os.path.exists(nome_arquivo_playlist):
            print(f"\nConteúdo da playlist '{nome_playlist}':")
            with open(nome_arquivo_playlist, "r") as arquivo:
                for linha in arquivo:
                    print("-", linha.strip())
        else:
            print("Playlist vazia ou não encontrada.")
    elif opcao == "5":
        if os.path.exists(nome_arquivo_playlist):
            os.remove(nome_arquivo_playlist)
            print("Playlist excluída com sucesso.")
        else:
            print("Playlist não encontrada.")
    else:
        print("Opção inválida.")

# Salva curtidas/descurtidas no histórico do usuário

def salvar_historico(nome_usuario, acao):
    with open(Historico, "a") as arquivo:
        arquivo.write(f"{nome_usuario}:{acao}\n")

# Exibe as ações de curtida/descurtida do usuário

def visualizar_historico(usuario):
    if not os.path.exists(Historico):
        print("Nenhum histórico disponível.")
        return
    print(f"\nHistórico de {usuario['nome']}:")
    with open(Historico, "r") as arquivo:
        for linha in arquivo:
            if linha.startswith(usuario['nome'] + ":"):
                print("-", linha.strip().split(":", 1)[1])

# Encerra o programa

def sair():
    print("Saindo...")
    exit()

if __name__ == "__main__":
    main()