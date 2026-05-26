# 1. O Laço 'for' (Repeticões Determinadas)
# use 'for' quando você sabeexatamente quantas vezes algo deve acontecer ( como ler 10 sensores ou procesar uma lista de peças)
# Exemplo; Relatorio de produção diaria 
# imagine que você tem uma mete de produzir 5 lotes e quer numerar cada um: 

#Exemplo 1:
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [ok]")
#     print("produção do dia finalizada!")

# #Exemplo 2 
# for b in range(10):
#     print(f"Quantidade total {b} foi...")

#exemplo 3
#imagine o seguinte cenairio, iremos produzir 20 disco de vinil.

# for disco in range(21):
#     print(f"Processando disco número {disco}...")
#     print("qualidade verificada. [OK]")
# print("Produção do dia finalizada!")

#Exemplo 4

# peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "prego", "chave de fenda"]
# itempeças = ["cilindrias", "Eixo conico", "radiais", "chave metalica"]

# for item in peças:
#     print(f"Item em estoque: {item} e {itempeças}")
#     for item2 in itempeças:
#         print(f"item de peças em estoque: {itempeças}")


#exemplo 5
#imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a  partir da seleção ele lista os produtos

# print("loja da nazareth")
# print("opçao 1- peças")
# print("opçao 2- itempeças")
# menu = int(input("escolha uma opçao"))

# peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "prego", "chave de fenda"]
# itempeças = ["cilindrias", "Eixo conico", "radiais", "chave metalica"]

# if menu == 1:
#     for item1 in peças:
#         print(f"sua lista de peças {peças} são...")
# elif menu == 2:
#     print(f"sua lista de item peças {itempeças} são...")
# else:
#     print("opçao invalida: encerrando o sistema")


##Exercicio 1
## 1. contador de produção (for)
##uma esteira prcessa 10 peças por ciclo. crie um progrma que use um for para controlar de 1 a 10 e, para cada numero, imprima:" peça X processada com susseso". no final exiba"ciclo comcluido

# print("contator de produção")

# for peças in range(1, 11):
#     print(f"processando peça numero{peças}...")
#     print("peça verificada com sucesso")
# print("ciclo de produção comcluido")

## Exercicio 2
#imagine a produção de frutas em uma feira. desejo apresentar as frutas banana, manga, melancia. uma quantidada de 10 bananas , 5 mangas , 10 melancias e 13 abacaxi
#no fim da produção gostaria de ter um total das produções

# frutas = ["banana", "manga", "melancia", "abacaxi"]

# for banana in range(1, 11):
#     print(f"banana n° {banana}")
#     print("qualidade [boa]")
# for manga in range(1, 6):
#     print(f"manga n° {manga}")     
#     print("qualidade [boa]")
# for melancia in range(1, 11):
#     print(f"melancia n° {melancia}")     
#     print("qualidade [boa]")
# for abacaxi in range(1, 14):
#     print(f"abacaxi n° {abacaxi}")     
#     print("qualidade [boa]")
# print("A produção foi de frutas foi de:", 10 + 5 + 10 + 13)
    

## exercicio 3 
## montar uma tabuada iniciante pode ser usada por uma valor fixo e depois usar a pergunta

