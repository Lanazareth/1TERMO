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
#         messagebox.showinfo("Saudação", f"operador {nome} registrado no {turno}")
                            
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

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("média de qualidade")
janela.geometry("600x200")
janela.configure(bg="#6E031E")

def media_de_qualidade():
    media = float(media.get())
    nota1 = float(campo_nota1.get())
    nota2 = float(campo_nota2.grt())
    nota3 = float(campo_nota3.get()) 

    if media == "":
        messagebox.showwarning("aviso!, e nessesario digitar as notas para caucular as medias.")
    else:
        media = (nota1 + nota2 + nota3) / 3
        messagebox.showinfo("media de qualidade", f" a media das suas notas foi de {media} ")

lbl_nota1 = tk.Label(janela, text= "Digite a nota 1 : ")
lbl_nota1.grid(row=0, column=0, pady=5, padx=10)
campo_nota1 =tk.Entry(janela, font=("Arial", 12))
campo_nota1.grid(row=0, column=1, pady=10, padx=10)
lbl_nota2 = tk.Label(janela, text="digita a nota  2 : ")
lbl_nota2.grid(row=1, column=0, pady=5, padx=10)
campo_nota2 =tk.Entry(janela,  font=("Arial", 12))
campo_nota2.grid(row=1, column=1, pady=10, padx=10)
lbl_nota3 = tk.Label(janela, text= "Digite a nota 3 : ")
lbl_nota3.grid(row=2, column=0, pady=5, padx=10)
campo_nota3 =tk.Entry(janela, font=("Arial", 12))
campo_nota3.grid(row=2, column=1, pady=10, padx=10)
btn_clique = tk.Button(janela, text="caucular media", font=("Arial, 11"), bg="#EFF0F0", fg="black", command=media_de_qualidade)
btn_clique.grid(row=4,column=1, pady=5, padx=10)

media_de_qualidade = tk.Entry(janela, font=("Arial, 14")) 
media_de_qualidade.grid(row=0, column=1, pady=10, padx=10)

janela.mainloop()