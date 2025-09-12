#1.Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
diferenca = abs(num1 - num2)
diferenca = round(diferenca, 2)
print(f"A diferença absoluta entre {num1} e {num2} é: {diferenca}")

#2.Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n
#Biblioteca random: Função randint()
#Biblioteca math:  Função sqrt()
import random, math 
n = int(input("Digite a quantidade de valores que deseja gerar: "))
soma = 0
for i in range(n):
    numero = random.randint(0, 100)
    soma += numero
print(soma)
print(f"A raiz quadrada é: {math.sqrt(soma):.2f}")

#3.Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.
import random
numero_aleatorio = random.randint(1, 10)
print("Advinhe o número entre 1 e 10")
while True:
    palpite = int(input("Digite seu palpite:"))
    if palpite < numero_aleatorio:
        print("Muito baixo! Tente novamente:")
    elif palpite > numero_aleatorio:
        print("Muito alto! Tente novamente:")
    else:
        print("Correto! O número é:", numero_aleatorio)

#4.Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:
#Você pode consultar esse  tutorial da Alura sobre a biblioteca datetime. Existem várias maneiras de resolver essa questão. Uma sugestão é:
#Função datetime.datetime.now() cujo retorno possui os atributos: day, month, year, hour, minute
#Usar a formatação com f-strings no momento de imprimir. Atenção para os atributos que devem sempre ter 2 dígitos precedidos por zero se necessário.
from detetime import datetime
agora= datetime.now()
data = agora.strftime("%d/%m/%Y")
hora = agora.strftime("%H:%M")
print("Data:", data)
print("Hora:", hora)

#5.Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas. Faça:
#No terminal, instale a biblioteca emoji usando o gerenciador de pacotes pip
#Conheça a função emoji.emojize()
#Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji. Em seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).
#A seguir um exemplo de interação, com uma lista de emojis sugeridos. Você pode consultar o texto que codifica outros emojis indo nessa página e passando o mouse por cima do emoji desejado
from emoji import emojize
print("Lista de emojis disponíveis:")
print(":red_heart:", emojize(":red_heart:"))
print(":thumbs_up:", emojize(":thumbs_up:"))
print(":thinking_face:", emojize(":thinking_face:"))
print(":partying_face:", emojize(":partying_face:"))
frase = input("Digite uma frase e ela será emojizada:")
frase_emojizada = emojize (frase, language= "alias")
print("n/Frase emojizada:", frase_emojizada)