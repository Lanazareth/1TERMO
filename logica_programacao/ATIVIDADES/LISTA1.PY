# Atividade 1: Mensagem de Boas-Vindas
# # Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
# # programação em Python!".

# print("bem-vindo ao mundo da programação em Python!")

# # Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# # Exemplo de saída:
# # Fulano de Tal
# # 30
# pergunta1 = input("qual e o seu nome: ")
# pergunta2 = int(input("qual e a sua idade: "))

# print("seu nome e sua idade são: ",pergunta1, pergunta2)


# # Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# # por 128. Cada resultado deve ser exibido em uma linha separada.
# # ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# # ● Obs: Realize também a mesma situação com variáveis

# print(135 + 246)

# valor1 = float(input("Digite o primeiro valor"))
# valor2 = float(input("digite o segundo valor"))
# total = valor1 + valor2
# print("A soma é:", total)
 

# subtração1 = float(input("digite o primeiro valor"))
# subtração2 = float(input("digite o sugundo valor"))
# total = subtração1 - subtração2
# print("a subtração é:", total)


# Atividade 4: Multiplicação e Divisão

# (print(15 * 8))
# (print(78 / 3))
# valor1 = float(input("digite o primeito valor"))
# valor2 = float(input("digite o segundo valor"))
# operador = input("qual operador deseja?")

# if operador == "*":
#     multiplicação = valor1 * valor2
#     print("A multiplicação foi: ", multiplicação)
# elif operador == "/":
#      divisão = valor1 / valor2
#      print("A divisão foi: ", divisão)

# Atividade 5: Potenciação
# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# ● Dica: O operador de potenciação em Python é **.

# (print(5 ** 3))

# Atividade 6: Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.

# nome = input("seu nome?")
# sobrenome = input("seu sobrenome?")
# print(" seu nome " + nome +  " seu sobrenome " + sobrenome)

# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

# Qdeproduzidas = int(input(" digite a quantidade de peças produzidas:"))
# Qdedefeituosas = int(input("digite a quantidade de peças defeituosas:"))
# Qdepeçasboas = Qdeproduzidas - Qdedefeituosas
# TXdeaproveitamento = Qdepeçasboas / Qdeproduzidas
# print("a taxa de aproveitamento foi de: ",TXdeaproveitamento)

# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).

# idade = int(input("qual a sua idade:"))
# print("eu tenho" , idade, "e em 10 anos terei",idade + 10 ,"anos")

# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

# valorpassagem = int(input("digite o valor da passagem:"))
# custohotel = int(input("digite o custo do hotel:"))
# Qdenoites = int(input(" quantas noites ira ficar?"))
# custototal = (custohotel * Qdenoites) + valorpassagem
# print("o custo total da viajem foi de:" , custototal)

# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:

# ==========================
# Relatório de Vendas
# ==========================
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50
# ==========================


produto = input("qual o produto desejado?")
Qvendida = int(input("qual foi a quantidade vendida?"))
PRunitario = float(input("qual o valor unitario?"))
VLtotal = Qvendida * PRunitario

print("-------------------")
print("relatorio de vendas")
print("-------------------")
print("produto: " , produto )
print("quantidade vendida: " , Qvendida )
print("preço unitario: " , PRunitario )
print("valor total: " , VLtotal )
      