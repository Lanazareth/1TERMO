## 🎓 Aula: Arquitetura IoT - Prática com Arduino e Programação

## 1. O Ecossistema Arduino na IoT
O Arduino atua principalmente na **Camada de Percepção**. Ele é a interface entre o mundo físico e o digital.

*   **Microcontrolador:** Geralmente baseado em chips AVR (como o ATmega328P) ou arquiteturas mais modernas com Wi-Fi nativo (como o **ESP32**, compatível com a IDE Arduino).
*   **Ciclo de Execução:** Diferente de um PC, o Arduino roda um "loop" infinito, lendo sensores e reagindo a eles em tempo real.

---

## 2. Linguagem C++ (Firmware / Dispositivo)
O C++ é a linguagem padrão para programar microcontroladores via IDE Arduino. É uma linguagem de "baixo nível" comparada ao Python, o que garante maior velocidade e menor uso de memória.

### Estrutura Básica (Sketch):
```cpp
// Definições de hardware
const int LED_PIN = 13; 

void setup() {
  // Roda uma vez quando o Arduino liga
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Roda repetidamente para sempre
  digitalWrite(LED_PIN, HIGH);
  Serial.println("LED Aceso");
  delay(1000); 
  digitalWrite(LED_PIN, LOW);
  delay(1000);
}
```

---

## 3. Linguagem Python (Gateway / Backend / IA)
Na arquitetura IoT, o Python raramente roda no Arduino básico. Ele costuma rodar em **Gateways** (como Raspberry Pi) ou em **Servidores de Nuvem**.

*   **Processamento de Dados:** Ideal para bibliotecas de Ciência de Dados (Pandas, NumPy).
*   **Comunicação Serial:** Python é usado para "conversar" com o Arduino via USB.
*   **MicroPython:** Uma versão simplificada que roda em placas potentes como ESP32 ou Raspberry Pi Pico.

### Exemplo: Python lendo dados do Arduino (via Serial):
```python
import serial # Biblioteca PySerial

# Configura a porta serial (Ex: COM3 no Windows ou /dev/ttyUSB0 no Linux)
arduino = serial.Serial('COM3', 9600)

while True:
    data = arduino.readline().decode('ascii')
    print(f"Dados recebidos do Arduino: {data}")
```

---

## 4. Comparativo: C++ vs. Python em IoT


| Característica | C++ (Arduino) | Python (Gateway/Cloud) |
| :--- | :--- | :--- |
| **Performance** | Altíssima (compilado) | Média (interpretado) |
| **Uso de Memória** | Muito eficiente (Kbytes) | Exigente (Mbytes) |
| **Facilidade** | Curva de aprendizado maior | Muito fácil e legível |
| **Aplicação** | Controle direto de hardware | Análise de dados e APIs |

---

## 5. Exercício Prático Sugerido
1.  **Hardware:** Conectar um sensor de umidade ao Arduino.
2.  **C++:** Programar o Arduino para enviar o valor da umidade via Serial a cada 5 segundos.
3.  **Python:** Criar um script para receber esse valor, salvar em um arquivo `.txt` ou enviar para um dashboard na web.
