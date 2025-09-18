#1. Escreva um script python que use compreensão de listas para criar as seguintes listas:
#Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
pares = [x for x in range(20, 51)if x % 2 == 0]
print("Pares", pares)

#Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
quadrados = [x**2 for x in range(1,11)]
print("Quadrados", quadrados)

#Todos os números entre 1 e 100 que sejam divisíveis por 7.
div = [x for x in range(1, 101) if x % 7 == 0]
print("Divisíveis por 7", div)

#Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar']) 
paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(30)]
print("Paridade", paridade)
 
#2. Solicite uma frase do usuário e usando compreensão de listas imprima:
#A lista de vogais da frase, ordenada alfabeticamente.
frase = input("Digite uma frase:"). lower()
vogais = sorted([letra for letra in frase if letra in "aeiou"])
print("Vogais:", vogais)

#A lista de consoantes da frase (remova espaços em branco)
consoantes = [letra for letra in frase if letra.isalpha() and letra not in "aeiou"]
print("Consoantes:", consoantes)

#3. Reescreva o código a seguir para construir a lista pagamentos usando compreensão de listas, ou seja, eliminando o laço de repetição.
horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = [ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora-40) for hora in horas_trabalhadas]
print(pagamentos)

#4. Reescreva o código a seguir para construir a lista aprovados usando compreensão de listas, ou seja, eliminando o laço de repetição.
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
aprovados = [alunos[i] for i in range(len(notas))
  if notas[i] >= 60]
print(aprovados)