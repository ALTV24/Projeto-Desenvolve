#1. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Dica: usando listas você não precisa fazer um "if" para cada mês.
meses = {1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maior", 6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}
dia = int(input("Digite o dia:"))
mes = int(input("Digite o mês (1-12):"))
ano = int(input("Digite o ano:"))
if 1<= mes <= 12:
   print(f"Você nasceu em {dia} de {meses[mes]} de {ano}")
else:
   print("Mês inválido! Digite entre 1-12.")

#2. Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
frase = input("Digite uma frase:")
vogais = "aeiouAEIOU"
frase_modificadas = ""
for letra in frase:
   if letra in vogais:
      frase_modificadas += "*"
   else:
      frase_modificadas += letra
print("Frases modificadas", frase_modificadas)
   
#3. Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".
while True:
   frase = input("Digite uma frase(digite 'fim' para encerrar):")
   if frase.lower() == 'fim':
      break
   frase_limpa = frase.replace("","").lower()
   if frase_limpa == frase_limpa[::-1]:
      print("A frase é palíndromo")
   else:
      ("A frase não é palíndromo")

#4. Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
#Pelo menos 8 caracteres de comprimento.
#Contém pelo menos uma letra maiúscula e uma letra minúscula.
#Contém pelo menos um número.
#Contém pelo menos um caractere especial (por exemplo, @, #, $).
def validador_senha(senha):
   if len(senha) <8:
      return False
   tem_maiuscula = any(c.supper()for c in senha)
   tem_maiuscula = any(c.islower()for c in senha)
   tem_numero = any(c.isdigit() for c in senha)
   especiais = "@#$%&*!?"
   tem_especial= any(c in especiais for c in senha)
   return tem_maiuscula and tem_maiuscula and tem_numero and tem_especial
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "SenhaFraca"
print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))

#5. Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
#Dica: use a biblioteca random.
import random
def embaralhar_palavras(frases):
   palavra = frase.split
   resultado = []
   for palavra in palavra:
      if len(palavra) > 3:
         meio = list(palavra[1:-1])
         random.shuffle(meio)
         nova_palavra = palavra[0] + "".join(meio) + palavra[-1]
         resultado.append(nova_palavra)
      else:
         resultado.append(palavra)
      return "". join(resultado)
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)