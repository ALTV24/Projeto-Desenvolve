#1. Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
#A lista original
#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … )
num = []
print("Digite pelo menos 4 números inteiros. Para parar, digite 'sair'.")
while True:
    entrada = input("Número inteiro:")
    if entrada.lower() == "sair" and len(num) >= 4: break
    elif entrada.lower() == "sair":
        print("Você precisa digitar pelo menos 4 números antes de sair.")
    else:
        num.append(int(entrada))
print("Lista completa", num)
print("4 primeiros elementos:", num[:4])
print("3 últimos elementos:", num[-3:])
print("Lista ivertida:", num[::-1])
print("Índices pares:", num[0::2])
print("Índices ímpares:", num[1::2])


#2. Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios, conforme exemplo a seguir. 
urls = [
    "www.google.com", "www.gmail.com", "www.yahoo.com", "www.reddit.com", "www.github.com"
]
dominios = [url.split('.')[1]for url in urls]
print("Domínios principais:", dominios)

#3. Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.
import random
lista = [random.randint(-10,10) for _ in range(20)]
print("Lista original:", lista)
maior_abs = max(lista, key = abs)
lista.remove(maior_abs)
lista.append(maior_abs)
print("Lista modificada:", lista)

