#1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:

#O terreno possui 250m2 e custa R$512,490.50 - Comente na linha acima de cada instrução uma breve descrição da instrução.

#Fórmulas: area_m2 = comprimento * largura / preco_total = preco_m2 * area_m2
comprimento = int(input("Digite o comprimento do terreno em metros: "))
largura = int(input("Digite o largura do terreno em metros: "))
preco_m2 = float(input("Digite o preço do metro quadrado do terreno: "))
area = comprimento * largura
preco_total = preco_m2 * area
print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")

#2 - Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 

#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

#86 graus Fahrenheit são 30 graus Celsius.
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))
celsius = int((fahrenheit-32) * (5/9))
print(f"{fahrenheit} graus Fahrenheit são {int(celsius)} graus Celsius.")

#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:

#Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)

#A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
nome1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o preço unitário do produto 1:"))
quantidade1 = int(input("Digite a quantidade do produto 1:"))

nome2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o preço unitário do produto 2:"))
quantidade2 = int(input("Digite a quantidade do produto 2:"))

nome3 = input("Digite o nome do produto 3:")
preco3 = float(input("Digite o preço unitário do produto 3:"))
quantidade3 = int(input("Digite a quantidade do produto 3:"))

total = (preco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3)
print(f"Total: R${total:,.2f}")
#Entrada
#Digite o nome do produto 1:calça
#Digite o preço unitário do produto 1:199.90
#Digite a quantidade do produto 1: 3
#Digite o nome do produto 2:camisa
#Digite o preço unitário do produto 2:49.95
#Digite a quantidade do produto 2:10
#Digite o nome do produto 3:cinto
#Digite o preço unitário do produto 3:25
#Digite a quantidade do produto 3:3

#Saída Total: R$1,174.20

 