
relatorio = []

while True:
    print("\n***************************************")
    print("✨ Seja Bem-Vindo ao estacionamento ✨")
    print("***************************************")

    print("Menu")
    print("Leia e Selecione uma das opções abaixo")
    print("Opção 1: Emitir Tícket")
    print("Opção 2: Verificar TAG")
    print("Opção 3: Interfone")
    print("Opção 4: Gerar Relatório de Entradas e Saídas")
    

    try:
        entrada = int(input("\nDigite o numero da opção que deseja: "))

        if entrada == 1:
            print("\n--- Emitindo o ticket ---")
            placa = input("Digite a sua placa: ")
            modelo = input("Digite o modelo do seu veiculo 🚗: ")
            
            hora_entrada = float(input("Digite a hora de entrada 🕑 (ex: 14.5 para 14:30): "))
            valor_estacio = float(input("Digite o valor a cobrar por hora 💵: "))
            hora_saida = float(input("Digite a hora da saida 🕑: "))
                
            total_permanencia = hora_saida - hora_entrada
            total_estacio = total_permanencia * valor_estacio
                
            print(f"\nSeu tempo de permanencia foi de {total_permanencia:.2f} ⏲︎ horas")
            print(f"O valor a ser cobrado foi de R${total_estacio:.2f} 💸")
            print("Devolver ticket")
                
                
            relatorio.append({
                    "Acesso": "Ticket",
                    "Placa": placa,
                    "Modelo": modelo,
                    "Cobranca": f"R$ {total_estacio:.2f}"
                })

        elif entrada == 2:
            print("\n--- Verificando a TAG ---")
            placa = input("Digite a sua placa: ")
            modelo = input("Digite o modelo do seu veiculo 🚗: ")
            print("Sua estadia no shopping será cobrada na sua fatura🧾")
            print("Tenha uma boa estadia!⭐")
            
            
            relatorio.append({
                "Acesso": "TAG",
                "Placa": placa,
                "Modelo": modelo,
                "Cobranca": "Fatura"
            })

        elif entrada == 3: 
            print("\n--- Acesso pelo interfone 📞 ---")
            placa = input("Digite a sua placa: ")
            modelo = input("Digite o modelo do seu veiculo 🚗: ")
            print("Liberando o seu acesso pelo interfone...")
            print("Lembrando que sua saida também deverá ser realizada pelo interfone.")
            print("Tenha uma boa estadia!⭐")
            
            
            relatorio.append({
                "Acesso": "Interfone",
                "Placa": placa,
                "Modelo": modelo,
                "Cobranca": "A definir"
            })
            
        elif entrada == 4:
            print("\n📊 --- RELATÓRIO DE ENTRADAS E SAÍDAS ---")
            if not relatorio:
                print("Nenhum veículo foi registrado até o momento.")
            else:
                for i, registro in enumerate(relatorio, 1):
                    print(f"{i}. [{registro['Acesso']}] Placa: {registro['Placa']} | Modelo: {registro['Modelo']} | Cobrança: {registro['Cobranca']}")
            print("------------------------------------------")

        elif entrada == 0:
            print("\nEncerrando o sistema. Obrigado pela visita, volte sempre! 👋")
            print("***************************************************************")
            break 
        else:
            print("\n❌ Opção inválida. Escolha um número de 0 a 4.")

    except ValueError:
        print("\n❌ ERRO: Opção inválida. Por favor, digite um número inteiro para o menu.")