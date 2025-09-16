#1.Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
#A lista ordenada, sem modificar a lista original
#A lista original
#O índice do maior valor da lista
#O índice do menor valor da lista
import random
aleatorios = []
for i in range(20):
    valor = random.randint(-100,100)
    aleatorios.append(valor)
print(sorted(aleatorios))
print(aleatorios)
print(aleatorios.index(max(aleatorios)))
print(aleatorios.index(min(aleatorios)))



#2.Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:
#A lista elementos
#A soma dos valores da lista
#A média dos valores da lista
import random
num_elementos = random.randint(5,10)
elementos = random.randint(1,10)
soma = sum (elementos)
media = soma / num_elementos
print("Quantidade de elementos:", num_elementos)
print("Lista de elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", round(media,2))


#3.Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
#Ambas as listas
#A lista intersecção ordenada
#A quantidade de vezes que cada elemento aparece em cada lista
#Atenção, a lista de intersecções não pode ter duplicatas. 
import random
lista1, lista2 = [], []
for i in range(20):
    lista2.append(random.randint(0,50))
    lista1.append(random.randint(0,50))
intersecao = []
for i in lista1:
    if i in lista2 and i not in intersecao:
        intersecao.append(i)
intersecao.sort()
for i in intersecao:
    print(f"{i}: ({lista1.count(i)}, {lista2.count(i)}")

#4.Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
#Exemplo de interação via terminal (entradas em laranja): 
 
n1 = int(input("Digite a quantidade de elementos da Lista1:"))
list1 = []
print(f"Digite os {n1} elementos da Lista1:")
for i in range(n1):
    valor = int(input())
    list1.append(valor)
n2 = int(input("Digite a quantidade de elementos da Lista2:"))
lista2 = []
print(f"Digite os {n2} elementos da Lista2:")
for i in range(n2):
    valor = int(input())
    lista2.append(valor)
lista_intercalada = []
i, j = 0,0 
while i < n1 and j < n2:
    lista_intercalada.append(list1[i])
    i += 1
    lista_intercalada.append(lista2[j])
    j += 1
print("Lista intercalada:", lista_intercalada)


 