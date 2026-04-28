# 1. O loço While (repetições indederminadas)
# use o While quando vai parar. ele depende de condição (como um sensor de segurança ou um botão de emergencia).
# exemplo monitor de temperatura (loop infinito controlado)
# inicio
# import time
# temperatura = 30
# while temperatura < 80:
#     print(f"Tenperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3  # Simulando o aquecimento da maquina
# print("ALERTA! temperatura atingiu o limite. Desligando motor...")

# exemplo 2.
# lista de temperaturas lisdas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # O loop para aqui NÃO lê os proximos valores (85 e 80)
#     print(f"Temperatura está em {temp}°C. Operção normal")

# print("Sistema desligado. Aguardando manutenção")

# exemplo 3.

# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peça in materiais:
#     if peça != "metal":
#         print(f"Aviso: Peça de {peça} detectada. desviando para descarte...")
#         continue # Pula o restante do codigo abaixo e vai para a proxima peça
#     #Este codigo só roda se a peça for metal
#     print(f"Processando peça de {peça}. furando e polindo...")

# print("Fim do lote de produção")


# ATIVIDADE 1
# TENTE CRIAR UM CODIGO QUE CONTE DE 1 A 10, MAS USE O CONTINUE PARA NÃO IMPRIMIR O NUMERO 5(SIMULADO UMA FALHA ESPECÍFICA NO ITEM

# for sensor in range(1, 11):
#     if sensor == 5:
#     print(f"sensor n° {sensor} com falha")
#     print(f"sensor {sensor} sem falha")
#     continue
# print("Fim! :)")
   

# ATIVIDADE 2
# SIMULE UM SEMAFORO COM PARADA PARA CADA COR. DETERMINE UM TEMPO QUE DESEJA PARA QUE QUANDO 
# MUDAR TAL CAOR ELE REPRESENTE UMA PAUSA PARA CADA COR. USE O CONTINUE PARA PULAR A COR AMARELA (SIMULANDO UM SEMAFORO COM DEFEITO QUE NÃO ACENDE A LUZ AMARELA)
# inicio
# import time

# lista = ["verde", "amarelo", "vermelho"]
# for cor in lista:
#     if cor != "amarelo":
#         print(f"Semáforo na cor {cor} ")
#         time.sleep(3)
#         continue
# print("Semáforo com defeito...")
# print("aguardando manutenção...")

# ATIVIDADE 3 
# SOMA DE CARGAS DE ENERGIA
# UMA FABRICA TEM 5 MAQUINAS. PEÇA AO USUARIO ( VIA INPUT DENTRO DO LOOP) O CONSUMO DA MAQUINA EM KWH DE CADA UMA DAS 5 MAQUINAS
# AO FINAL DO LOOP, O PROGRAMA DEVE EXIBIR O CONSUMO TOTAL DA FABRICA.
total_consumo = 0
for mqnn in range(1, 6):
    consumo = float(input(f"quanto a maquina n° {mqnn} consumiu em khw?"))
    total_consumo += consumo  # acumula o consumo total
print(f"o consumo total da fabrica é de {total_consumo} khw")
    



