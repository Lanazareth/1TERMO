while True:
    print("\n=======================================")
    print("\n          BIBLIOTECA DIGITAL           ")
    print("\n=======================================")
    nome = input("Digite seu nome: ")
    print(f"Olá {nome}, seja bem-vindo à Biblioteca Digital")
    print("Escolha uma opção: ")
    print("            Opção 1: ALunos")
    print("       Opção 2: Comunidade Geral")
    print("\n=======================================")

    opção = int(input("Qual opção você deseja? "))

    if opção == 1:
        print(f"Olá {nome}, que tipo de livro deseja conhecer? ")
        print("Livros Comuns = 1")
        print("Livros Raros = 2")
        livros = int(input("Livros Raros ou Comuns? "))
        if livros == 1:
            livro = input("Qual livro comum você deseja? ")
            print("Alunos podem ficar com o livro por até 14 dias de graça.")
            dias = int(input(f"Quantos dias você deseja ficar com o livro {livro}? "))
            if dias <= 14:
                print(f"Parabéns! Você terá {dias} dias para terminar de ler {livro}, boa leitura!")
            elif dias > 14:
                print("Será cobrada uma taxa fixa de R$ 5,00 por dia")
                valor_final = (dias-14)*5
                print(f"O valor final será de: {valor_final} reais")
                print(f"Parabéns! Você terá {dias} dias para terminar de ler {livro}, Boa leitura!")
            else:
                print("Erro: encerrando sistema!")
        elif livros == 2:
            livro_raro = input("Qual livro raro você deseja explorar? ")
            dias1 = int(input(f"Quantos dias você deseja ficar com o livro {livro_raro}? "))
            if dias1 <= 14:
                print(f"Parabéns! Você terá {dias1} dias para terminar de ler {livro_raro}, boa leitura!")
            elif dias1 > 14:
                print("Será cobrada uma taxa fixa de R$ 5,00 por dia")
                valor_final1 = (dias1- 14)*5
                print(f"O valor final será de: {valor_final1}")
            else:
                print("Erro: encerrando sistema!")
    elif opção == 2:
        livro2 = input(f"Olá {nome}, que livro deseja conhecer? ")
        print("A Comunidade Geral pode ficar por até 7 dias de graça.")
        dias2 = int(input(f"Quanto dias você deseja ficar o {livro2}? "))
        if dias2 <= 7:
                print(f"Parabéns! Você terá {dias2} dias para terminar de ler {livro2}, boa leitura!")
        elif dias2 > 7:
            print("Será cobrada uma taxa fixa de R$ 5,00 por dia")
            valor_final2 = (dias2-7)*5
            print(f"O valor final será de: {valor_final2} reais.")
            print(f"Parabéns! Você terá {dias2} dias para terminar de ler {livro2}, Boa leitura!")
        else:
            print("Erro: encerrando sistema!")
    else:
        print("Erro: encerrando sistema!")