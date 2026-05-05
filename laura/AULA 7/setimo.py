# projeto cancela automatica 

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código
print("***************************************")
print("✨ Seja Bem-Vindo ao estacionamento ✨")
print("***************************************")

print("Leia e Selecione uma das opções abaixo")
print("Opção 1:Emitir Tícket")
print("opção 2: verificar TAG")
print("Opção 3: interfone")
entrada = int(input("digite o numero da opção que deseja: "))

if entrada == 1:
    print("emitindo o ticket")
    hora_entrada = float(input("digite hora de entrada🕑: "))
    valor_estacio = float(input("digite a valor a cobrar💵:"))
    hora_saida = float(input("digite a hora da saida🕑:"))
    total_permanencia = hora_saida - hora_entrada
    print(f"seu tempo de permanencia {total_permanencia}⏲︎ em horas")
    total_estacio = total_permanencia * valor_estacio
    print(f"O valor a ser cobrado foi de R${total_estacio}💸")
    print("devolver ticket")
elif entrada == 2:
    print("verificando a TAG")
    print("sua estadia no shopping será cabrado na sua fatura🧾")

elif entrada == 3: 
    print(" acesso pelo interfone 📞")
    print("liberando o seu acesso pelo interfone")
    print("sua saida também deverá ser realizada pelo interfone")
else:
    print("Obrigado peela visita ")

print("********************************")

# passo 2- virificação do tempo




