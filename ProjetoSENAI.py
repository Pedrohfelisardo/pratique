
time1 = {
    'Pedro': {'nome': "Pedro", 'agente': "Gekko", 'kills': 6, 'mortes': 21, 'assists': 11, 'plantes': 3, 'disarms_spike': 1, 'killed_by': "Angel - 2k", 'suffered_by': "Ricardo - 6k"},
    'Gustavo': {'nome': "Gustavo", 'agente': "Jett", 'kills': 44, 'mortes': 17, 'assists': 6, 'plantes': 0, 'disarms_spike': 0, 'killed_by': "Ricardo - 13k", 'suffered_by': "Ricardo - 6k"},
    'Bruno': {'nome': "Bruno", 'agente': "KillJoy", 'kills': 17, 'mortes': 19, 'assists': 5, 'plantes': 1, 'disarms_spike': 0, 'killed_by': "Thiago - 5k", 'suffered_by': "Thiago - 6k"},
    'Igor': {'nome': "Igor", 'agente': "Clove", 'kills': 12, 'mortes': 20, 'assists': 10, 'plantes': 0, 'disarms_spike': 1, 'killed_by': "Prikitinha - 5k", 'suffered_by': "Gebe - 8k"},
    'Higa': {'nome': "Higa", 'agente': "Sova", 'kills': 4, 'mortes': 21, 'assists': 9, 'plantes': 1, 'disarms_spike': 0, 'killed_by': "Priquitinha, Gebe, Ricardo, Angel - 1k", 'suffered_by': "Ricardo - 7k"}
}

time2 = {
    'Angel': {'nome': "Angel", 'agente': "Sage", 'kills': 11, 'mortes': 17, 'assists': 14, 'plantes': 0, 'disarms_spike': 0, 'killed_by': "Bruno - 4k", 'suffered_by': "Gustavo - 9k"},
    'Thiago': {'nome': "Thiago", 'agente': "Cypher", 'kills': 25, 'mortes': 14, 'assists': 5, 'plantes': 2, 'disarms_spike': 0, 'killed_by': "Higa - 6k", 'suffered_by': "Gustavo - 6k"},
    'Ricardo': {'nome': "Ricardo", 'agente': "Jett", 'kills': 27, 'mortes': 19, 'assists': 5, 'plantes': 1, 'disarms_spike': 0, 'killed_by': "Higa - 7k", 'suffered_by': "Gustavo - 13k"},
    'Gebe': {'nome': "Gebe", 'agente': "Reyna", 'kills': 27, 'mortes': 15, 'assists': 9, 'plantes': 1, 'disarms_spike': 0, 'killed_by': "Higa - 6k", 'suffered_by': "Gustavo - 5k"},
    'Priquitinha': {'nome': "Priquitinha", 'agente': "KillJoy", 'kills': 8, 'mortes': 18, 'assists': 9, 'plantes': 2, 'disarms_spike': 1, 'killed_by': "Pedro - 4k", 'suffered_by': "Gustavo - 8k"}
}



def exibir_placar(time, time_label):
    print('-' * 100)
    print(f'{time_label} PLACAR')
    print('-' * 100)
    print(f'Player\t\tKills\t\tMortes\t\tAssists')
    for jogador, estatisticas in time.items():
        print(f'\n{estatisticas["nome"]}\t\t{estatisticas["kills"]}\t\t{estatisticas["mortes"]}\t\t{estatisticas["assists"]}')

def calc_placar(time):
    total_kills = sum([jogador['kills'] for jogador in time.values()])
    total_mortes = sum([jogador['mortes'] for jogador in time.values()])
    assists = sum([jogador['assists'] for jogador in time.values()])
    return str(total_kills), str(total_mortes), str(assists)
def pergunta(time1, time2):
    mortes_entre = {}

    while True:
        print('\nSoma dos placares:')
        print(f'Time 1: {calc_placar(time1)} Kills/Mortes/Assistências')
        print(f'Time 2: {calc_placar(time2)} Kills/Mortes/Assistências')

        exibir_placar(time1, "Time 1")
        exibir_placar(time2, "Time 2")

        resposta = input("\nDigite o nome de um jogador para saber mais sobre ele (ou 'sair' para sair): ").strip().capitalize()
        if resposta.lower() == 'sair':
            break

        if resposta in time1 or resposta in time2:
            jogador = time1.get(resposta) or time2.get(resposta)
            if jogador:
                # Informações do jogador
                print(
                    f"Informações sobre {jogador['nome']}:\n"
                    f"Agente: {jogador['agente']}\n"
                    f"Kills: {jogador['kills']}\n"
                    f"Mortes: {jogador['mortes']}\n"
                    f"Assistências: {jogador['assists']}\n"
                    f"Desarmes da Spike: {jogador['disarms_spike']}\n"
                    f"Plantes: {jogador['plantes']}\n"
                    f"Quem mais matou: {jogador['killed_by']}\n"
                    f"Quem mais morreu: {jogador['suffered_by']}")


                continuar = input("\nDeseja saber informações de outro jogador? (sim/não): ").strip().lower()
                if continuar != 'sim':
                    print('FIM DO PROGRAMA.')
                    break
        else:
            print("Nome inválido.")



pergunta(time1, time2)
