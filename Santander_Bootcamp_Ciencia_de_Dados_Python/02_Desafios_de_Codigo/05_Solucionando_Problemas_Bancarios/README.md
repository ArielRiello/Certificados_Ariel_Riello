## Desafios O Grande Depósito
### 1 / 1 - Solucionando Problemas Bancários

Nivel : Básico / Matemática

### Descrição

Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro e solicitar um novo valor. O programa deve continuar solicitando valores de depósito até que seja digitado um valor válido.
 
---

### Entrada

O programa deve utilizar o Scanner para receber os valores de depósito digitados pelo cliente. Os valores podem ser decimais, representando valores em reais.

---

### Saída

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

---

### Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

|Entrada|Saída|
|-|-|
|500.50|Deposito realizado com sucesso! Saldo atual: R$ 500.50|
|-100|Valor invalido! Digite um valor maior que zero.|
|0|Encerrando o programa...|

---

### Código Inicial:

~~~python
valor = float(input())

if valor > 0:
    //TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
elif valor == 0:
   //TODO: Imprimir a mensagem de valor inválido.
else:
  //TODO: Imprimir a mensagem de encerrar o programa.
~~~

---

### Código Resposta:

*Código resposta para passar no teste*

~~~python
valor = float(input())

if valor > 0:
    print(f"Deposito realizado com sucesso!\nSaldo atual: R$ {valor:.2f}")
elif valor == 0:
    print("Encerrando o programa...")
else:
    print("Valor invalido! Digite um valor maior que zero.")
~~~

---

### Código Resposta Melhorado:

*Código sugestão de resolução*

*OBS: Não passa no software do desafio*

~~~python
def deposito(valor):
    while True:
        if valor > 0:
            print('Deposito realizado com sucesso!\nSaldo atual: R$ {:.2f}'.format(valor))
            break
        elif valor == 0:
            print('Encerrando o programa...')
            break
        else:
            print('Valor invalido! Digite um valor maior que zero.')
            valor = float(input())

valor = float(input())
deposito(valor)
~~~

---