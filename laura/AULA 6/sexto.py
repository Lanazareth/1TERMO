# Clean Code - aula 6
# para quer ?
# print("c usar?
# como usalean code - aula 6")
# aula = 6
# print(f"estamos na aula {aula} de clean code")
 

##manipulação de arquivo e texto
# texto = "   Python é Muito Legal!  "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower()) # "python"
# print(texto.strip().capitalize()) # "Python"
# print(texto.strip().title()) # "Python"
# print(texto.strip().replace(" ", "_")) # "Python"
# print(texto.strip().split()) # ["Python"]

# escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("estudar Python hoje!")
#     arquivo.write("\nLer sobre clean code.")

# # ler
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)


#exercicio 1
# crie um programa que peca ao usuaria pata inserir uma frase e, em seguida, exida com as seguintes tranformações 
# - remova os espaços estras no inicio e no final 

# texto = input("por favor digite uma frase:")
# print(texto.strip().split())

# exercicio 2 
# crie um programa que leia o conteudo de um arquivo de texto e conte quantas vezes
# a palavra python apareceno arquivo. exida o resultado para o usuario 

# print("contagem de palavras em arquivo")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"a contagem de palavras {contagem}e de...")

#execução de comando de sistemas
# import os #importa o modulo os interagir com o sistemas operacional
#onde estou
# print(os.getcwd())
#listar arquivo na pasta
# print(os.listdir())
# print(os.listdir(".."))  # lista arquivo da pasta pai
# print(os.listdir("..\\..")) #lista arquivos da pasta avó
# print(os.listdir("C:\\")) # lista arquivos da raiz do C
# print(os.listdir("C:\\Users")) #lista arquivos da pasta users
# print(os.listdir("C:\\users\\Public")) # lista de arquivo da pasta public

# outros  comandos uteis
# criar pasta 
# os.mkdir("nova_pasta")
#renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
#excluir pasta
# os.rmdir("pasta_renomeada")


# exercici 1
# crie um script que mostre o caminho da pasta atual
# print(os.getcwdb())

# exercicio 2
# liste os arquivos da pasta atual
# print(os.listdir()) 
# exercicio 3
# # crie uma pasta chamada "projetos" e depois renomei para "meus_projetos". por fim, exclua a  pasta.
# os.mkdir("projetos")

# os.rename("projetos", "meus_projetos")

# os.rmdir("meus_projetos")

# exercicio 4
# crei um arquivo chamado "log.txt" be escreva a mensagem " log de atividades".
# depois leia o conteudo do arquivo e exida na tela
# with open("Log.txt", "w") as arquivo:
#     arquivo.write("log de atividade")

# with open("Log.txt", "r") as arquivo:
#     conteudo =arquivo.read()
#     print(conteudo)

# dicionario de informações
# pessoa = {
#     "nome": "alice",
#     "idade": 30,
#     "cidade": "são paulo",
#     "profissão": "engenharia"
# }
# pessoa2 = {
#     "nome": "bruno",
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "designer"
# }
# print(pessoa["nome"])
# print(pessoa2["nome"], pessoa2["idade"])

# cardapio = {
#     "segunda": "macarronada",
#     "terça": "bacalhada",
#     "quarta": "feijoada",
#     "quinta": "arroz careteiro"
#     "sexta": "bolo de carne"
# }
# cardapio = {
#     "segunda": "lasanha",
#     "terça": "macarrão ao molho branco",
#     "quarta": "parmegiana",
#     "quinta": "arroz com fraudinha"
#     "sexta": "rondele"
# }
# print(cardapio["segunda"])
# print(cardapio2["quinta"], cardapio2["sexta"])

# exemplo 2: desligar o pc (comando para windows)
# with open("deligar.bat", "w") as desligar:
#     desligar.white("shutdown -s -t 60 -c \"desligamento programado para daqui a 1 hora. salve o seu trabalho!\")
#-s comando para desligar
# -t tempo definir
# -a cancelar desligamento
