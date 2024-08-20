# funcoes.py

def adicionar_jogador(jogadores): #Adcionar Jogador#

    nome = input("Digite o nome do jogador: ")
    if nome in jogadores:
        print("Jogador já está cadastrado.")
    else:
        jogadores[nome] = {
            'total_partidas': 0,
            'total_gols': 0,
            'total_assistencias': 0
        }
        print(f"Jogador {nome} adicionado com sucesso.")
    return jogadores

def registrar_estatisticas(jogador, gols, assistencias): #Atualizar as Estatisticas#

    jogador['total_partidas'] += 1
    jogador['total_gols'] += gols
    jogador['total_assistencias'] += assistencias
    return jogador

def exibir_relatorio(jogador): #Gera relatório#

    if jogador['total_partidas'] == 0:
        media_gols = 0
        media_assistencias = 0
    else:
        media_gols = jogador['total_gols'] / jogador['total_partidas']
        media_assistencias = jogador['total_assistencias'] / jogador['total_partidas']
    
    relatorio = (
        f"Total de partidas: {jogador['total_partidas']}\n"
        f"Total de gols: {jogador['total_gols']}\n"
        f"Total de assistências: {jogador['total_assistencias']}\n"
        f"Média de gols por partida: {media_gols:.2f}\n"
        f"Média de assistências por partida: {media_assistencias:.2f}\n"
    )
    return relatorio

def coletar_gols_assistencias(): #Coletar os dados da partida

    try:
        gols = int(input("Número de gols na partida: "))
    except ValueError:
        print("Entrada inválida. Usando 0 gols por padrão.")
        gols = 0
    
    try:
        assistencias = int(input("Número de assistências na partida: "))
    except ValueError:
        print("Entrada inválida. Usando 0 assistências por padrão.")
        assistencias = 0

    return gols, assistencias

def mostrar_menu(): #Menu#

    print("\n........MENU........")
    print()
    print("1. Adicionar jogador")
    print("2. Registrar estatísticas")
    print("3. Ver estatísticas de jogador")
    print("4. Sair")
    print()
    escolha = int(input("Escolha uma opção: "))
    return escolha

