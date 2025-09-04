#1.Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão. 
n1, n2 = int(input()), int(input())
if (n1 + n2) % 2 == 0 : print("Par")
else: print("Ímpar")

#2.Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:
#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."
a, b, c, d, e = "Excelente!", "Muito Bom!", "Bom!", "Regular.", "Ruim."
nota= int(input("Digite a avaliação do filme (1 a 5): "))
if nota == 5: print (a)
elif nota == 4: print (b)
elif nota == 3: print (c)
elif nota == 2: print (d)
elif nota == 1: print (e)

#3.Você está desenvolvendo um programa para verificar se um ano é bissexto. Escreva um código em Python que solicita ao usuário para inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto". 
#Teste seu código com os valores: 1900 (não bissexto), 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto). 
ano= int(input("Digite um ano:"))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) : print("Bissexto")
else: print("Não Bissexto")

#4.Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
distancia = float(input("Digite a distância da entrega em km: "))
peso = float(input("Digite o peso do pacote em kg:"))
if distancia <= 100: frete = 1 * peso
elif distancia <= 300: frete = 1.5 * peso
else: frete = 2 * peso
if peso > 10: frete += 10
print(f"Valor do frete: R${frete:.2f}")

