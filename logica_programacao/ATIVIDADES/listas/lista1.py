# # Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# # jogador [nick] está no nível [nível] e pronto para a partida!"
# print("*************")
# print("Perfil gamer!")
# print("*************")
# nick = input(" digite o seu nick de jogador:")
# nivel = input("digite o seu nivel atua:")
# print(" o jogador", nick,  "esta no nivel", nivel, )
# print("*******************************************")
# # # Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# # # multiplique por 4 para mostrar quanto ele terá no final do mês.

# print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
# print("caululadora de mesada")
# print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
# valorporsemana = int(input("digite o valor ganho por semana:"))
# conta = valorporsemana * 4
# print("o ganho total do mês foi de:", conta)
# print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
# # # Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# # # Megabytes (MB) (multiplique por 1024).

# print("'''''''''''''''''''''")
# print("conversão de internet")
# print("'''''''''''''''''''''")
# gigi = int(input("digite o valor de gigabytes que deseja converter em megabytes: "))
# meme = 1024 
# concon =  gigi * meme
# print(" a converção foi de:" , concon)
# print("'''''''''''''''''''''''''''''")
# # # Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# # # média final.
# print("#####################")
# print("cauculadora de medias")
# print("#####################")

# nota1 = int(input(" digite a sua nota de matematica:"))
# nota2 = int(input("digite a sua nota de português:"))
# media = nota1 + nota2 / 2
# print("sua media final foi de: ", media)
# print("###############################")
# # # Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# # # o aluno ganhou hoje. Exiba o total atualizado.

# print("_________________________")
# print("caucular novos seguidores")
# print("_________________________")

# santigos = int(input("digite a quantidade de seguidores atuais:"))
# snovos =  int(input("digite a quantidade de seguidores novos:"))
# stotal = santigos + snovos
# print("agora o total de seguidosres é:", stotal)
# print("_______________________________________")
# # # Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# # # ele já viveu (idade * 365).

# print("..............................")
# print(" cauculadora de dias de vida !")
# print("..............................")
 
# aninhos = int(input("digite a sua idade:"))
# qdias = 365
# ddvida = aninhos * qdias
# print(" você ja vivel:", ddvida)
# print(".......................")
# # # 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# # # total da conta.

# print("+++++++++++++++++")
# print("consumo do lanche")
# print("+++++++++++++++++")

# sal = float(input("qual o valor do salgado:"))
# su = float(input("qual o valor do suco:"))
# conta = sal + su
# print("o valor total da conta foi:", conta)
# print("++++++++++++++++++++++++++++++++++")
# # # Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# # # em que ele nasceu.

# print("~~~~~~~~~~~~~~~~~~")
# print(" ano de nascimento")
# print("~~~~~~~~~~~~~~~~~~")

# ida = int(input("digite a sua idade:"))
# ano = int(input("digite o ano atual:"))
# conano = ida - ano 
# print("o seu ano de nascimento é:", conano)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# # # Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# # # "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# # # mais, "Acesso liberado".

# print("^^^^^^^^^^^^^^^")
# print("filtro de idade")
# print("^^^^^^^^^^^^^^^")

# idade = int(input("digite a sua idade:"))
# if idade <= 13:
#     print("acesso restrito")
# elif idade >= 13:
#     print("ecesso moderado")
# elif idade >= 18:
#     print("acesso liberado")
# else:
#     print("acesso liberado")
# print("^^^^^^^^^^^^^^^^^^^")
# # # 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# # # repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# # # chegar em 10 e exibe: "Por favor, conecte o carregador!".

# print("°°°°°°°°°°°°")
# bateria = 100
# print("°°°°°°°°°°°°")

# while bateria > 10:
#     print(f"bateria em {bateria}%")
#     bateria -= 10

# print(f"bateria em {bateria}% ")
# print("por favor concte ao caregador")
# print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
# # # # 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# # # foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# # # esse número, printando: "Curtida no [i] recebida!".
# print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
# for curtida in range(1, 6):
#     print(f"curtida n° {curtida} recebida")
# print("essa foi sua contagem de curtidas!")
# print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
# # # 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# # # aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# # # quantas vezes ele adiciona itens ao carrinho (use um contador).;

# print("=================")
# print("compras oline")
# print("=================")
# contador = 0
# produto = ""

# print("carrinho de compras oline")
# print("digite 'sair' para finalizar a compra")


# while produto.lower() != "sair":
#     produto = input("digite o nome do produto: ")
#     contador += 1
# if produto.lower() != "sair":
#     print(f" peoduto {produto} adicionado ao carrinho")

# print(f"compra finalizada! você adicionou {contador} ao seu carrinho.")
# print("==============================================================")
