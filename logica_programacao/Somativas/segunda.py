# Foco: print, input, operações matemáticas e f-strings
# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
# import tkinter as tk
# from tkinter import messagebox

# def saudar_usuario():
#     nome = campo_nome.get()
#     turno = campo_turno.get()

#     if nome == "" and turno == "": 
#         messagebox.showwarning(" Aviso, por favor digite seu nome e seu turno!")
#     else: 
#         messagebox.showinfo("Saudação", f"operador {nome} registrado no turno {turno}")
                            
# app = tk.Tk()
# app.title("Exercicio 1")
# app.geometry("350x200")
# # Componentes
# lbl_nome = tk.Label(app, text="Digite seu nome abaixo:")
# lbl_nome.pack(pady=10)
# campo_nome = tk.Entry(app, font=("Arial", 12))
# campo_nome.pack(pady=5)
# lbl_turno = tk.Label(app, text="digite seu turno: ")
# lbl_turno.pack(pady=10)
# campo_turno = tk.Entry(app, font=("arial", 12))
# campo_turno.pack(pady=5)
# btn_enviar = tk.Button(app, text="Enviar", command=saudar_usuario)
# btn_enviar.pack(pady=15)
# app.mainloop()

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("700x200")
# janela.configure(bg="#B9B136")

# def calcular_producao():
#     pecas = int(pecas_quantidade.get())
#     if pecas == "":
#         messagebox.showwarning("Aviso", "Por favor, digite a quantidade de peças para o cálculo!")
#     else:
#         pecas = pecas * 8
#         messagebox.showinfo("Cálculo de Produção", f"Foram produzidas {pecas} peças em um turno de 8 horas!")

# lbl_quantidade = tk.Label(janela, text="Digite a quantidade de peças produzidas em 1 hora: ")
# lbl_quantidade.grid(row=0, column=0, pady=10, padx=10)
# btn_clique = tk.Button(janela, text="Cálculo Total da Produção", font=("Arial, 11"), bg="#EFF0F0", fg="black", command=calcular_producao)
# btn_clique.grid(row=1, column=0, pady=10, padx=10)

# pecas_quantidade = tk.Entry(janela, font=("Arial, 14"))
# pecas_quantidade.grid(row=0, column=1, pady=10, padx=10)

# janela.mainloop()
    


# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Conversor de Umidade")
# janela.geometry("600x200")
# janela.configure(bg="#6E031E")

# def conversor_umidade():
#     conversor = float(conversor_numero.get())
#     if conversor == "":
#         messagebox.showwarning("Aviso!", "É necessário digitar a pressão em Bar para a conversão!")
#     else:
#         conversor = conversor * 14.5
#         messagebox.showinfo("Conversão de Umidade", f"A conversão da pressão Bar par PSI foi {conversor}")

# lbl_numero = tk.Label(janela, text="Digite em Bar para fazer a conversão para PSI")
# lbl_numero.grid(row=0, column=0, pady=10, padx=10)
# btn_clique = tk.Button(janela, text="Conversor de Umidade", font=("Arial, 11"), bg="#EFF0F0", fg="black", command=conversor_umidade)
# btn_clique.grid(row=1, column=0, pady=10, padx=10)

# conversor_numero = tk.Entry(janela, font=("Arial, 14"))
# conversor_numero.grid(row=0, column=1, pady=10, padx=10)

# janela.mainloop()

# 4.Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     # 1. Pega os valores como texto primeiro
#     texto_nota1 = um_usuario.get()
#     texto_nota2 = dois_usuario.get()
#     texto_nota3 = tres_usuario.get()
    
#     # 2. Verifica se ALGUMA das caixas está vazia (usa 'or' em vez de 'and')
#     if texto_nota1 == "" or texto_nota2 == "" or texto_nota3 == "":
#         messagebox.showwarning("Aviso", "Por favor, preencha todas as três notas.")
#         return # Para a função aqui
        
#     # 3. Tenta converter os textos para números e calcular
#     try:
#         nota1 = float(texto_nota1)
#         nota2 = float(texto_nota2)
#         nota3 = float(texto_nota3)
        
#         valor_notas = nota1 + nota2 + nota3
#         resultado_final = valor_notas / 3 
        
        
#         messagebox.showinfo("Resultado", f"A média das notas é: {resultado_final:.2f}")
        
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite apenas números válidos (use ponto para decimais).")    


# janela = tk.Tk()
# janela.title("Calculadora de Média")
# janela.geometry("450x250") 
# janela.configure(bg="pink")


# lbl_nota1 = tk.Label(janela, text="Digite a primeira nota de 0 a 10:")
# lbl_nota1.grid(row=0, column=0, pady=10, padx=10, sticky="e")
# lbl_nota2 = tk.Label(janela, text="Digite a segunda nota de 0 a 10:")
# lbl_nota2.grid(row=1, column=0, pady=10, padx=10, sticky="e")
# lbl_nota3 = tk.Label(janela, text="Digite a terceira nota de 0 a 10:")
# lbl_nota3.grid(row=2, column=0, pady=10, padx=10, sticky="e")
# um_usuario = tk.Entry(janela, font=("Arial", 12), width=10)
# um_usuario.grid(row=0, column=1, pady=10, padx=10)
# dois_usuario = tk.Entry(janela, font=("Arial", 12), width=10)
# dois_usuario.grid(row=1, column=1, pady=10, padx=10)
# tres_usuario = tk.Entry(janela, font=("Arial", 12), width=10)
# tres_usuario.grid(row=2, column=1, pady=10, padx=10)
# btn_mensagem = tk.Button(janela, text="Calcular Média", command=janela_bemvindo)
# btn_mensagem.grid(row=3, column=0, columnspan=2, pady=15)

# janela.mainloop()

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     entrada = calor_usuario.get()
    
    
#     if entrada == "": 
#         messagebox.showwarning("Aviso", "Por favor, informe a temperatura do motor")
#         return 
#     try:
#         temperatura = float(entrada)
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite um número válido.")
#         return

    
#     if temperatura < 40:
#         messagebox.showinfo("Temperatura", "Baixa carga")
#     elif temperatura <= 70:
#         messagebox.showinfo("Temperatura", "Normal")
#     else:
#         messagebox.showinfo("Temperatura", "ALERTA! Resfriamento ativado.")    


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="pink") 

# lbl_mensagem = tk.Label(janela, text="Por favor, informe a temperatura do motor")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# calor_usuario = tk.Entry(janela, font=("Arial", 12))
# calor_usuario.grid(row=1, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Calcular", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()



# 6. Classificador de Lotes

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     codigo = codigo_usuario.get().upper()

#     if codigo == "":
#         messagebox.showwarning("Aviso", "Por favor, insira o código do produto")
#     elif codigo.startswith("A"):
#         messagebox.showinfo("Categoria", "Alimentos")
#     elif codigo.startswith("E"):
#         messagebox.showinfo("Categoria", "Eletrônicos")
#     else:
#         messagebox.showinfo("Categoria", "Desconhecido")

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("300x300")
# janela.configure(bg="pink")

# lbl_mensagem = tk.Label(janela, text="Por favor, insira o código do produto")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# codigo_usuario = tk.Entry(janela, font=("Arial", 12))
# codigo_usuario.grid(row=1, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Verificar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()


# Questao 7 -

# import tkinter as tk
# from tkinter import messagebox

# def verificar_maquina():
#     sensor = sensor_porta.get().lower()
#     emergencia = botao_emergencia.get().lower()

#     if sensor == "fechada" and emergencia == "desligado":
#         messagebox.showinfo("Resultado", "Máquina pode iniciar")
#     else:
#         messagebox.showwarning("Resultado", "Máquina NÃO pode iniciar")

# janela = tk.Tk()
# janela.title("Segurança de Operação")
# janela.geometry("350x200")

# tk.Label(janela, text="Sensor da porta (fechada/aberta)").grid(row=0, column=0, padx=10, pady=10)
# sensor_porta = tk.Entry(janela)
# sensor_porta.grid(row=0, column=1)

# tk.Label(janela, text="Botão de emergência (desligado/ligado)").grid(row=1, column=0, padx=10, pady=10)
# botao_emergencia = tk.Entry(janela)
# botao_emergencia.grid(row=1, column=1)

# tk.Button(janela, text="Verificar", command=verificar_maquina).grid(row=2, column=0, columnspan=2, pady=10)

# janela.mainloop()


# Questão 8 -
# import tkinter as tk
# from tkinter import messagebox

# def calcular_descarte():
#     try:
#         total = int(total_pecas.get())
#         defeituosas = int(pecas_defeituosas.get())

#         if total <= 0:
#             messagebox.showerror("Erro", "O total de peças produzidas deve ser maior que zero.")
#             return 
            
#         if defeituosas < 0:
#             messagebox.showerror("Erro", "O número de peças defeituosas não pode ser negativo.")
#             return
            
#         if defeituosas > total:
#             messagebox.showerror("Erro", "O número de defeituosas não pode ser maior que o total produzido.")
#             return
#         percentual = (defeituosas / total) * 100

#         if percentual > 5:
#             messagebox.showwarning("Resultado", f"Revisar Processo!\nPercentual de descarte: {percentual:.2f}%")
#         else:
#             messagebox.showinfo("Resultado", f"Processo Otimizado!\nPercentual de descarte: {percentual:.2f}%")

#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite apenas números inteiros válidos.")


# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("380x180") 
# janela.configure(bg="#b8c25e") 
# tk.Label(janela, text="Total de peças produzidas:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
# total_pecas = tk.Entry(janela, font=("Arial", 10), width=15)
# total_pecas.grid(row=0, column=1, padx=10, pady=10)
# tk.Label(janela, text="Peças defeituosas:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
# pecas_defeituosas = tk.Entry(janela, font=("Arial", 10), width=15)
# pecas_defeituosas.grid(row=1, column=1, padx=10, pady=10)

# btn_calcular = tk.Button(janela, text="Calcular", command=calcular_descarte, font=("Arial", 10, "bold"), bg="#d1d1d1")
# btn_calcular.grid(row=2, column=0, columnspan=2, pady=15)

# janela.mainloop()

# Questão 9 - 

# import tkinter as tk
# from tkinter import messagebox

# def validar_medida(event=None): # 'event=None' permite que a função funcione com o botão ou com a tecla Enter
#     try:
        
#         texto_entrada = medida_usuario.get().replace(",", ".")

#         if not texto_entrada.strip():
#             messagebox.showwarning("Aviso", "Por favor, insira uma medida antes de validar.")
#             return
#         medida = float(texto_entrada)
#         if medida <= 0:
#             messagebox.showerror("Erro", "A medida da peça deve ser maior que zero.")
#             return
#         if medida < 9.8:
#             messagebox.showwarning("Resultado", f"REPROVADO!\nA medida ({medida:.2f} mm) está ABAIXO da tolerância mínima (9.80 mm).")
#         elif medida > 10.2:
#             messagebox.showwarning("Resultado", f"REPROVADO!\nA medida ({medida:.2f} mm) está ACIMA da tolerância máxima (10.20 mm).")
#         else:
#             messagebox.showinfo("Resultado", f"APROVADO!\nA medida ({medida:.2f} mm) está dentro dos padrões.")

#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite um número válido.")

# janela = tk.Tk()
# janela.title("Controle de Qualidade")
# janela.geometry("380x160")
# janela.configure(bg="#c67cd4")
# lbl_info = tk.Label(janela, text="Especificação Alvo: 10,00 mm ± 0,20 mm", font=("Arial", 9, "italic"), bg="#f7f7f7", fg="#666")
# lbl_info.grid(row=0, column=0, columnspan=2, pady=(10, 5))
# tk.Label(janela, text="Medida da peça (mm):", font=("Arial", 10), bg="#f7f7f7").grid(row=1, column=0, padx=10, pady=10, sticky="e")
# medida_usuario = tk.Entry(janela, font=("Arial", 11), width=12)
# medida_usuario.grid(row=1, column=1, padx=10, pady=10, sticky="w")
# medida_usuario.focus() 
# medida_usuario.bind("<Return>", validar_medida) 
# btn_validar = tk.Button(janela, text="Validar Medida", command=validar_medida, font=("Arial", 10, "bold"), bg="#e0e0e0")
# btn_validar.grid(row=2, column=0, columnspan=2, pady=15)

# janela.mainloop()


# Questão 10 -

# import tkinter as tk
# from tkinter import messagebox

# def iniciar_prensa():
#     contagem = ""

#     for i in range(10, 0, -1):
#         contagem += str(i) + "\n"

#     contagem += "\nPrensa Ativada!"

#     messagebox.showinfo("Contagem Regressiva", contagem)

# janela = tk.Tk()
# janela.title("Setup da Prensa")
# janela.geometry("300x150")

# tk.Button(janela, text="Iniciar Contagem", command=iniciar_prensa).pack(pady=40)

# janela.mainloop()
