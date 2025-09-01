# 1 - Transforme o seguinte algoritmo em código. Lembre-se das funções print e type que já conhecemos de forma geral.
# Armazene o valor 5 em uma variável e o valor 2 em outra variável
raio=5
trovão=2
# Imprima o tipo de dados dessas duas variáveis
print(type(raio))
print(type(trovão))
# Divida a primeira variável (com o valor 5) pela segunda variável (com o valor 2) e armazene o resultado em uma terceira variável
tormenta=raio/trovão
# Imprima a terceira variável e também o seu tipo.
print(tormenta)
print(type(tormenta))

#2 - Transforme o seguinte algoritmo em código. Lembre-se das funções print e type que já conhecemos de forma geral.
# Armazene o texto "o resultado é"  em uma variável, o valor 10 em outra variável, e o valor 3.5 numa terceira variável.
vtexto="o resultado é"
vnum1=10
vnum2=3.5
# Some os valores da segunda e terceira variável e armazene em outra variável.
vnum3=vnum2+vnum2
# Imprima todas as variáveis na ordem de criação e imprima também seus tipos.
print(vtexto)
print(type(vtexto))
print(vnum1)
print(type(vnum1))
print(vnum2)
print(type(vnum2))
print(vnum3)
print(type(vnum3))

#3 - Dadas duas variáveis v1 = 10 e v2 = 20, utilize uma terceira variável para trocar os valores entre as duas variáveis. Ou seja, ao final v1 terá o valor de v2, e v2 o valor de v1. Você deve usar uma variável auxiliar de troca, não podendo atribuir os novos valores diretamente. 
v1=10
v2=20
aux=v1
v1=v2
v2=aux
print(v1)
print(v2)

#4 - Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. Reescreva esse código usando apenas duas variáveis.
juros=1.01
saldo=500.00
saldo=saldo*juros
print(saldo)
saldo=saldo*juros
print(saldo)
saldo=saldo*juros
print("Após 3 meses meu novo saldo é")
print(saldo)
 


