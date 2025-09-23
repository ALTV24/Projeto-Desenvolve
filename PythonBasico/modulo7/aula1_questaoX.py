#1. Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
palavra = input("Digite seu nome:")
for i in range(1, len(palavra)+1):
	print(palavra[:i])

#2. Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.
nome = input("Digite seu nome:")
sobrenome = input ("Digite seu sobrenome:") 
nome_completo = nome + "" + sobrenome
print("Bem-vinda,", nome_completo)
#3. Escreva um script que dado uma frase conta os espaços em branco.
frase = input("Digite uma frase:")
def contar_espaços(frase):
    contador = 0
    for caractere in frase:
        if caractere == ' ':
            contador += 1
    return contador
print(f"Espaços em branco:", contar_espaços(frase))

#4. Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
numero = input("Digite o número:")
if len(numero) == 8:
     numero = '9' + numero
elif len(numero) == 9:
     if numero[0] != '9':
          print("Número inválido! O numero de 9 dígitos deve começar com 9")
          exit()
numero_formatado = numero[:5]+'-'+ numero[5:]
print("Número completo:", numero_formatado)           

#5. Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:
frase = "O meu amor mora em Roma e me deu um ramo de flores"
count_vogais = 0
indice = []
for i in range(len(frase)):
     if frase[i] in "aeiouAEIOU":
          count_vogais += 1
          indice.append(i)
print(count_vogais)
print(indice)

#6. Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.
frase = "O meu amor mora em Roma e me deu um ramo de flores"
objetivo = sorted ('amor')
frase_lower = frase.lower()
lst_palavras = frase_lower.split(" ")
for palavra in lst_palavras:
     if sorted(palavra) == objetivo:
         print(palavra)

#7. Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:
#Chave de criptografia: gere um valor n aleatório entre 1 e 10
#Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
import random
def encrypt(lista):
     chave = random.randint(1, 10)
     criptografados = []
     for nome in lista:
          novo_nome = ""
          for char in nome:
               codigo = ord(char)
               codigo_cripto = ((codigo - 33 + chave) % (126 - 33 + 1)) + 33
               novo_nome += chr(codigo_cripto)
          criptografados.append(novo_nome)
     return criptografados, chave
nomes = ["Fulana", "Ju", "Deivi", "Vivi", "Pedro"]
nomes_cripto, chaves = encrypt (nomes)
print("Nomes Criptografados", nomes_cripto)

#8. Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 
#O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2, como no exemplo abaixo:
#Em seguida somamos o resultado: 10+9+8+28+24+20+28+21+14 = 162
#Pegamos o resultado e dividimos por 11:  162 / 11 = 14 com resto 8
#Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
#Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
#No nosso exemplo temos que o resto é 8 então faremos 11-8 = 3. Logo o primeiro dígito verificador é 3. Então sabemos que o CPF deve ser:  111.444.777-3X
#Para  calcular o segundo dígito vamos usar o primeiro dígito já calculado. Vamos montar a mesma tabela de multiplicação usada no cálculo do primeiro dígito. Só que desta vez usaremos na segunda linha os valores 11,10,9,8,7,6,5,4,3,2 já que estamos incluindo mais um dígito no cálculo:
def validar_cpf(cpf: str) -> str:
    cpf = cpf.replace(".", "").replace("-", "")
    if not cpf.isdigit() or len(cpf) != 11:
        return "Inválido"
    numeros = cpf[:9]
    soma = 0
    multiplicador = 2
    for digito in numeros[::-1]: 
        soma += int(digito) * multiplicador
        multiplicador += 1
    resto = soma % 11
    if resto < 2:
        primeiro_dv = 0
    else:
        primeiro_dv = 11 - resto
    numeros = cpf[:9] + str(primeiro_dv)
    soma = 0
    multiplicador = 2
    for digito in numeros[::-1]:
        soma += int(digito) * multiplicador
        multiplicador += 1
    resto = soma % 11
    if resto < 2:
        segundo_dv = 0
    else:
        segundo_dv = 11 - resto
    cpf_calculado = cpf[:9] + str(primeiro_dv) + str(segundo_dv)
    if cpf == cpf_calculado:
        return "Válido"
    else:
        return "Inválido"
print(validar_cpf("111.444.777-35")) 
print(validar_cpf("545.315.761-52"))  
print(validar_cpf("545.315.761-12"))  