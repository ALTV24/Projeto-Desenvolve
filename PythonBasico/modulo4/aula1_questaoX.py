#Transforme em código o fluxograma a seguir:
#1.
x = int(input("Digite um número:"))
if x>5:
    print("Maior que 5")
print("Fim")

#2.
n = int(input("Digite um número:"))
cont=0
while cont < n:
    cont = cont + 1
    print(cont)
print("Fim")

#3.
n1,n2,n3 = int(input())
m = (n1 + n2 + n3)/3
if m >=60:
    print("Aprovado")
elif m>=40:
    print("Recuperação")
else:
    print("Reprovado")
print("fim")

#4. 
n = int(input("Digite a quantidade de números a serem lidos (n):"))
maior = 0
while n>0:
    x = int(input("Digite um número(x):"))
if x > maior:
    maior = x
    n = n-1
else:
    n = n-1
print(f"O maior número digitado foi: {maior}")

#5. Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.
#(idade1 + idade2 + idade3 + … + idade_n)/N
n = (input ())
soma = 0
cont = 0
while cont < n:
    idade = int(input())
    soma += idade
    cont += 1
print (soma/n)

#6. Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 
#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).
#Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas
n =n (input())
cont = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0
while cont < n:
    quantidade, tipo = int (input())
    if tipo == 'S':
        soma_sapo += quantidade
    elif tipo == 'R':
        soma_rato += quantidade
    elif tipo == 'C':
        soma_coelho += quantidade
    cont += 1
print ("Total de cobaias: ", soma_sapo + soma_rato + soma_coelho)
print ("Total de sapos: ", soma_sapo)
print ("Total de ratos:", soma_rato)
print ("Total de coelhos:", soma_coelho)