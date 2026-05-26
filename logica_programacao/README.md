# 🐍 Aula: Lógica de Programação com Python

## 1. Comandos Básicos de Entrada e Saída
Para interagir com o usuário e exibir dados:

*   **`print()`**: Exibe uma mensagem ou valor no console.
*   **`input()`**: Captura o que o usuário digita (sempre retorna o dado como *string*).
*   **`int()`**: Converte um valor para número inteiro (essencial para cálculos após o `input`).

### Exemplo:
```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá {nome}, você tem {idade} anos.")
```

---

## 2. Estruturas Condicionais (Tomada de Decisão)
O **`if`** (se) e o **`else`** (senão) controlam o fluxo do programa com base em condições.

```python
nota = 7
if nota >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
```

---

## 3. Estruturas de Repetição (Loops)
Usadas para executar o mesmo bloco de código várias vezes.

*   **`for`**: Usado quando sabemos o número de repetições (ex: percorrer uma lista ou intervalo).
*   **`while`**: Usado enquanto uma condição for verdadeira.

### Exemplo `for` e `while`:
```python
# Contagem de 0 a 4
for i in range(5):
    print(i)

# Loop até o usuário digitar 0
numero = -1
while numero != 0:
    numero = int(input("Digite 0 para sair: "))
```

---

## 4. Trabalhando com Tempo (`import time`)
Para pausar a execução do programa, utilizamos o módulo `time`.

```python
import time

print("Iniciando contagem regressiva...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1) # Pausa por 1 segundo
print("Decolar! 🚀")
```

---

## 5. Sugestões de Projetos Práticos

### Projeto 1: Calculadora de Média
Um programa que recebe 3 notas, calcula a média e diz se o aluno passou (Média > 7).

### Projeto 2: Simulador de Caixa Eletrônico
Usar o `while` para criar um menu de opções (1- Ver Saldo, 2- Sacar, 3- Sair).

### Projeto 3: Jogo da Adivinhação
O programa escolhe um número e o usuário tem X tentativas para acertar, usando `if/else` para dar dicas de "maior" ou "menor".

---

## 💡 Dicas de Sintaxe
1.  **Indentação:** Em Python, o espaço no início da linha é obrigatório para definir o que está dentro do `if`, `for` ou `while`.
2.  **Case Sensitive:** Python diferencia letras maiúsculas de minúsculas (`Print` é diferente de `print`).
