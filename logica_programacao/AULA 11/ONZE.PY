# Interface grafica com TKINTER
# componentes principais (widgets)

# tk: Janela principal
# Label: Texto ou rotulo
# Button: Um botão clicável
# Entry: Um campo de entrada de texto

# import tkinter as tk
# from tkinter import messagebox

# # 1. criar a jenela principal
# janela = tk.Tk()
# janela.title("Minha Primeira Janela GUI")
# janela.geometry("400x200") #Largura x Altura

# # 2. Criar a função 
# def mostrar_mensagem():
#     messagebox. showinfo("Sucesso!", "Você clicou no botão :)")

# # 3. Criar os componentes
# lbl_titulo_pagina = tk.Label(janela, text="Bem-Vindo a aula de Interface Gráfica!", font=("Arial", 14, "bold"))
# lbl_titulo_aula = tk.Label(janela, text="aula 11!", font=("Arial", 12, "bold"))
# btn_clique_pagina = tk.Button(janela, text="Clique Aqui", font=("Arial", 14), bg="#2ecc71", fg="white", command=mostrar_mensagem)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#e74c3c", fg="white", command=janela.destroy)

# # 4. Posicionar os componentes na janela
# lbl_titulo_pagina.pack(pady=20) #pady adiciona um espaçamento vertical
# lbl_titulo_aula.pack(pady=10)
# btn_clique_pagina.pack(pady=3)
# btn_fechar_janela.pack(pady=10)

# janela.mainloop()




