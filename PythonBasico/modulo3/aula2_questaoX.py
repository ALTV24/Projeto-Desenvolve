#1 - Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário.
idade_juliana = int(input())
idade_cris = int(input())

entrada_autorizada = idade_juliana > 17 and idade_cris

print(entrada_autorizada)
 
#2 - Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.
idade_juliana = int(input())
idade_cris = int(input())

entrada_autorizada = idade_juliana > 17 or idade_cris

print("Entrada autorizada:", entrada_autorizada)

#3 - Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em laranja e as impressões de seu código em branco.
idade = int(input("Digite sua idade:"))
jogou_input = input("Já jogou pelo menos 3 jogos de tabuleiro? (sim/nao):").lower()
jogou = jogou_input == "sim"
jogos_venceu = int(input("Quantos jogos já venceu?:"))

apto = (idade >= 16 and idade <= 18) and jogou and (jogos_venceu >= 1)

print("Apto para ingressar no clube de jogos de tabuleiro?:", apto)
#4 - Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:
#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
#Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.
#O programa deve imprimir False se os pontos de atributo não são consistentes com a classe escolhida. Segue um exemplo de interação com seu código no terminal, com entradas de dados destacadas em laranja e as impressões de seu código em branco.
escolha_classe = input("Escolha a classe (Guerreiro, Mago ou Arqueiro):")
pontos_força = input("Digite os pontos de força (de 1 a 20)?:")
pontos_magia = input("Digite os pontos de magia (de 1 a 20):")
pontos_atributo = input("Pontos de atributo consistentes com a classe escolhida:")

if escolha_classe == "Guerreiro": valido = (pontos_força >= 15 and pontos_magia <= 10)
elif escolha_classe == "Mago": valido = (pontos_força <= 10 and pontos_magia >= 15)
elif escolha_classe == "Arqueiro": valido = (pontos_força > 5 and pontos_magia > 5 and pontos_força <= 15)
else: valido = False

print("Pontos de atributo consistentes com a classe escolhida: True",valido)

#5 - Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:

#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos
#C: Ou ter 60 anos  e trabalhado pelo menos 25.
genero = int(input())
idade = int(input())
tempo_servico = int(input())

a = (genero == "F" and idade >= 60) or (genero == "M" and idade >= 65)
b = tempo_servico >= 30
c = idade >= 60 and tempo_servico >= 25

aposentadoria_aprovada = a or b or c

print("Aposentadoria aprovada", aposentadoria_aprovada)