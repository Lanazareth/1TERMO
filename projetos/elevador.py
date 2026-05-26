#  Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

# Sistema de Elevador de Prédio

andar_atual = 0
capacidade_maxima = 5
pessoas_no_elevador = 0


print("Bem-vindo ao elevador inteligente 🤖 !")

while True:
    print(f"\n[Status] Andar atual: {andar_atual} | Pessoas no elevador: {pessoas_no_elevador}")

    try:
        
        andar_chamada = int(input("De qual andar você está chamando? (0 a 10): "))
        if andar_chamada < 0 or andar_chamada > 10:
            print("Andar inválido! O prédio possui apenas os andares de 0 a 10.")
            continue

        pessoas = int(input("Quantas pessoas vão entrar? (Máximo de 5): "))
        if pessoas < 1 or pessoas > capacidade_maxima:
            print(f"Quantidade inválida! O elevador tem capacidade para até {capacidade_maxima} pessoas.")
            continue

        andar_destino = int(input("Para qual andar desejam ir? (0 a 10): "))
        if andar_destino < 0 or andar_destino > 10:
            print("Destino inválido! O prédio possui apenas os andares de 0 a 10.")
            continue

        if andar_atual != andar_chamada:
            print(f"\nO elevador foi chamado no andar {andar_chamada}.")
            if andar_atual < andar_chamada:
                print(">>> Subindo...")
                for andar in range(andar_atual + 1, andar_chamada + 1):
                    print(f"Passando pelo andar {andar}...")
            else:
                print(">>> Descendo...")
                for andar in range(andar_atual - 1, andar_chamada - 1, -1):
                    print(f"Passando pelo andar {andar}...")
            
            andar_atual = andar_chamada
            print("Elevador parando...")
        pessoas_no_elevador = pessoas
        print(f"Portas abertas no andar {andar_atual}. {pessoas_no_elevador} pessoa(s) entrou(aram).")

        if andar_atual != andar_destino:
            print(f"\nFechando portas. Indo para o andar {andar_destino}.")
            if andar_atual < andar_destino:
                print(">>> Subindo...")
                for andar in range(andar_atual + 1, andar_destino + 1):
                    print(f"Passando pelo andar {andar}...")
            else:
                print(">>> Descendo...")
                for andar in range(andar_atual - 1, andar_destino - 1, -1):
                    print(f"Passando pelo andar {andar}...")
            
            andar_atual = andar_destino
            print("Elevador parando...")
        else:
            print("\nVocê já está no andar de destino!")

       
        print(f"Portas abertas no andar {andar_atual}. {pessoas_no_elevador} pessoa(s) saiu(íram).")
        pessoas_no_elevador = 0 
    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros!")



        