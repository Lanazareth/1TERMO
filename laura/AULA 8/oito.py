# Exercícios de Programação Python: "O Caça-Erros"

# 1. O Problema da Idade
#*errado 
# idade = input("digite sua idade: ")
# if idade >=18:
#     print(" você é maior de idade ")
# #*corrigido 
# idade = int(input("digite a sua idade"))
# if idade >= 18:
    # print("Você é maior de idade")
#*melhorado 
# print("✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎")
# print("bem-vindo ao monitoramento de idade")
# print("✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎")
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

# print("✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎✴︎")

# 2. A Escrita Fiel
#errado
# nome = "mariana"
# print("seja bem-vinda, nome!")

# corigido
# nome = "mariana"
# print(f"seja bem-vinda,{nome}!")

# melhorado
# print("ola, seja bem-vinda ao nosso site")
# nome = input("digite o seu nome para realizar o seu cadastro: ")
# print(f"muito obrigada pelo o seu cadastro {nome}!♥︎")

# 3. Falta de Espaço
# errado
# numero = 10
# if numero > 5:
# print("o numero é maior que cinco")
# else:
# print("o numero é menor ou igual a cinco")

# corrigido
# numero = 10
# if numero > 5:
#     print("o numero é maior que cinco")
# else:
#     print("o numero é menor ou igual a cinco")

# melhorado
# numero = int(input("digite um numero: "))
# if numero < 5:
#     print("o numero e menor que cinco.")
# else:
#     print("o numero e maior ou igual a cinco.")


# 4. Esquecimento Fatal5
#errado 
# usuario = "aluno123"
# if usuario =="aluno123"
# print("login realizado con sucesso")

# corrigido
# usuario = "aluno123"
# if usuario == "usuario":
#     print(" login realizado com sucesso")

# melhorado 
# usuario = input("digite o nome do seu usuario: ")
# print(f"seu login foi realizado com sucesso jogador {usuario}")


# 5. Atribuição vs. Comparação
# # errado
# clima = "ensolarado"
# if clima = "chuvoso":
#    print("leve um guarda-chuva ")

# # corrigido
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("leve um guarda=chuva")

# melhorado###
# print("se planejando para o clima ")
# print("clima 1: ensolarado")
# print("clima 2 : chuvoso")
# print("clima 3 :  nublado")
# clima = int(input("digite o clima do dia de hoje:"))
 
# if clima == 1:
#    print("use algo para se proteger do sol, como protetor, oculos de sol,ect")
# elif clima == 2: 
#    print("use guarda-chuva e roupas mais grosas")
# elif clima == 3:
#    print("utilize agasalhos para evitar ventos gelados")
# else:
#    print("obrigado por nos consultar")


# 6.Misturando Alhos com Bugalhos
# errado
# pontos = 50
# print("parabens! você fez" "+pontos" "+pontos")

# corrigido
# pontos = 50
# print(f"Parabens você fez +{pontos} +{pontos}")

# melhorado 
# pontos = int(input("digite os seus pontos: "))
# if pontos> 50:
#     print(f"parabens você fez {pontos} pontos")
# elif pontos != 50:
#     print(f"parabens você fez {pontos} pontos")

# 7 A Ordem dos Fatores
# errado
# nota = 9.5
# if nota >= 7:
#     print("aprovado")
# elif nota >= 9:
#     print("exelente!")

# corrigido 
# nota = float(input("digite a sua nota: "))
# if nota >= 7:
#     print("aprovado!")
# elif nota >= 9:
#     print("exelente!!")
###melhorado
# nota = float(input("digite a sua nota: "))
# if nota <=5:
#     print("reprovado!")
# elif nota >=6:
#     print("aprovado!!")
# elif nota <=9:
#     print("exelente!!!")
# else:
#     print("obrigado por consultar a sua nota !")

# 8. O Contador de 1 a 5
# ##errado
# for i in range (5)
# print(i)
### corrigido
# for i in range (5):
#     print({i})
### melhorado 
# print("contador numerico!")
# for i in range (1, 6):
#     print(f"contando numero... {i}")

# 9. O Loop Eterno
###errado
# tentativas = 1
# while tentativas <= 3:
    # print("tentando conectar...")
###corrigido
# tentativas = 1
# while tentativas <= 3:
#     print(f"tentativa {tentativas}: tentando conectar...")
#     tentativas += 1
####melhorado 
# tentativas = 1 
# while tentativas <= 3: 
#     print(f"tentaviva {tentativas}: tentando conctar...")
#     tentativas += 1
# print("conecção instavel...")
# print("não foi possivel conctar....")
# print("tente novamente mais tarde.")


# 10. A Senha Teimosa
####errado
# senha = ""
# while senha == "python123":
#     senha = input("digite a senha secreta: ")
# print("acesso concedido! ")
###corrigido 
# senha = "python123"
# senha = input("digite a sua senha: ")
# while senha == "python123":
#     print("acesso concedido")
###melhorado 
# senha = "python123"
# senha = input("digite a sua senha para a liberação do seu acesso: ")
# while senha == "python123":
#     print("verificando...")
#     print("acesso liberado!")






