# principal.py

from funcoes import adicionar_jogador, registrar_estatisticas, exibir_relatorio, coletar_gols_assistencias, mostrar_menu

def executar_programa():

    jogadores = {}
    
    while True:
        escolha = mostrar_menu()
        print()  

        if escolha == 1: # Adicionar jogador

            jogadores = adicionar_jogador(jogadores)
            print()  
        
        elif escolha == 2: # Registrar estatísticas

            nome = input("Digite o nome do jogador para registrar estatísticas: ")
            print()  
            
            if nome in jogadores:
                gols, assistencias = coletar_gols_assistencias()
                jogadores[nome] = registrar_estatisticas(jogadores[nome], gols, assistencias)
                print(f"Estatísticas do jogador {nome} atualizadas com sucesso.")
                print()  
            else:
                print("Jogador não encontrado.")
                print()  
        
        elif escolha == 3: # Ver estatísticas de jogador

            nome = input("Digite o nome do jogador para ver as estatísticas: ")
            print()  
            
            if nome in jogadores:
                print(exibir_relatorio(jogadores[nome]))
                print()  
            else:
                print("Jogador não encontrado.")
                print()  
        
        elif escolha == 4: # Sair

            print("Saindo do programa.")
            print()  
            break
        
        else:
            print("Opção inválida, por favor escolha novamente.")
            print()  

if __name__ == "__main__":
    executar_programa()
