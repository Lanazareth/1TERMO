#Registro de Veículo: Peça o modelo do veículo e a placa. ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa viagem!" 
print("Registo de veículo!")
modelo_veiculo = input("Digite qual o medelo do seu veículo?...")
placa_do_carro = input(" por favor digite a placa dp seu veículo:...")
print(f"Veículo {modelo_veiculo} de placa {placa_do_carro} registrado no sistema. Boa viajem!")


# Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e o consumo médio do caminhão (km/l). ○ Calcule e exiba a distância total que o veículo pode pe]orrrc er com o tanque cheio.
print("cálculo de autonomia do veículo")

capacidade_do_tanque = float(input("por favor digite a capacidae do seu tanque em litros:..."))
comsumo_medio_do_caminhao = float(input("por favor digite o consumo medio do caminhão por km/L"))
distancia_percorida = capacidade_do_tanque /comsumo_medio_do_caminhao
print("A distancia total que o veiculo pode percorer e de:", {distancia_percorida},"km/L")
