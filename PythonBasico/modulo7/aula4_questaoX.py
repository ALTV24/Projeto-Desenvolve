#1. Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.
import os
frase = input ("Digite uma frase:")
arquivo = "frase.txt"
with open(arquivo,"w",encoding="utf-8")as f:
    f.write(frase)
caminho = os.path.abspath(arquivo)
print("Frase salva em {caminho}")    

#2. Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
import re
with open("frase.txt", "r", encoding = "utf-8") as f: 
    conteudo = f.read()
palavra = re.findall(r"\w+", conteudo)
with open("palavras.txt", "w", encoding="utf-8") as f:
    for p in palavra:
        f.write(p + "\n")
with open("palavras.txt","r", encoding= "utf-8") as f:
    print(f.read())    

#3. Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt". Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
#O texto das primeiras 25 linhas
#O número de linhas do arquivo
#A linha com maior número de caracteres
#O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).
with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readline()
print("Primeiras 25 linhas:\n")
for l in linhas[:25]:
    print(l.strip())
print("\nNúmeros de linhas", len(linhas))
linha_maior = max(linhas, key=len)
print("\nLinhas com mais caracteres:",
      linha_maior.strip())
print("Quantidade de caracteres:", len(linha_maior))
texto = "".join(linhas).lower()
num_nonato = texto.count("nonato")
num_iria = sum(1 for w in texto.split() if w == "íria")
print("\nMenções:")
print("Nonato:", num_nonato)
print("íria", num_iria)

#4. Vamos fazer o jogo da forca! Antes de programar: 
#Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
#Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.
#Escreva um programa em Python para executar o jogo, de acordo com as definições:
#Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
#Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
#No início exiba o número de letras na palavra como underscores;
#Permita que o jogador insira letras para adivinhar a palavra;
#Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
#Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
#Limite o número de tentativas para 6 (as partes do enforcado).
import random
def imprime_enforcado(erros, estagios):
    print(estagios[erros])
with open("gabarito_forca.txt","r",
encoding="utf-8")as f:
    conteudo = f.read().split("\n\n")
    estagio = [etapa.strip() for etapa in conteudo]
palavra = random.choice(palavra).lower()
progresso = ["_"]*len(palavra).lower
tentativa = len(estagio) - 1
erros = 0
letras_usadas = []
print("Bem-vindo ao Jogo da Forca!\n")
while erros < tentativa and "_" in progresso:
    print("\nPalavra:", "".join(progresso))
    print("Letras usadas",",".join(letras_usadas))
    imprime_enforcado(erros, estagio)
    letra = input("Digite uma letra:"). lower()
    if letra in letras_usadas:
        print("Você já tentou essa letra!")
    letras_usadas.append(letra)
    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                progresso[i] = letra
        print("Boa! Letra correta.")
    else:
        erros += 1
        print("Letra errada!")
imprime_enforcado(erros, estagio)
if "_" not in progresso:
    print("\nParabéns, você ganhou! A palavra era:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)

#5. A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.
#Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
#No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
#Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
#A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
#Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.
import csv
arquivo = "meus_livros.csv"
livros = [
    ["Meu Pé de Laranja Lima, José Mauro de Vasconcelos, 1968, 192"],
    ["Dom Quixote, Itamar Vieira Junior, 1602, 1246"],
    ["O Pequeno Princípe, Antoine de Saint-Exupéry, 1943, 96"],
    ["A BÍBLIA, Jeová (Deus), 100EC, 900"], 
    ["Como Eu Era Antes de Você, Jojo Moyes, 2012, 320"],
    ["Título, Pierre Weil e Roland Tompakow, 1991, 288"],
    ["Meu Pé de Laranja Lima, Claudia Gray, 2017, 397"],
    ["Dom Quixote, Anne Frank, 1947, 377"],
    ["O Pequeno Princípe, Maurice Leblanc, 1907, 192"],
    ["Moby Dick, Herman Melville, 1851, 1030"],
]
with open(arquivo,"w",newline="",encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(livros)
print(f"Arquivos'{arquivo}'criado com sucesso")

#6. amos descobrir as músicas mais populares do Spotify nos últimos 10 anos! 
#Crie uma conta no Kaggle, uma das principais plataformas de ciência de dados e aprendizado de máquina. Em disciplinas avançadas vamos trabalhar com bases de dados provenientes de lá!
#Baixe o arquivo spotify-2023.csv no final da página que apresenta os dados.
#No Python, abra o arquivo para leitura e imprima as cinco primeiras linhas
#Para abrir o arquivo, defina o parâmetro encoding='latin-1'
#Após compreender a estrutura do arquivo (divisão em colunas, caracter separador de coluna, etc.) passamos para a etapa de extração de informações.
#O arquivo está estruturado da seguinte forma: cada linha representa uma música e contém as seguintes informações separadas por vírgula (CSV):
#track_name,artist(s)_name,artist_count,released_year,released_month,released_day,in_spotify_playlists,in_spotify_charts,streams,in_apple_playlists
#Usaremos apenas informações das colunas:
import csv
with open("top10.csv", "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    musicas = list(leitor)
print("Todas as músicas:")
for m in musicas:
    print(f"{m['Música']} - {m['Artista']} ({m['Ano']}) | Streams: {m['Streams']}")
print("\nNomes das músicas:")
for m in musicas:
    print(m["Música"])
print("\nArtistas (únicos):")
artistas = {m["Artista"] for m in musicas}
for a in artistas:
    print(a)
print("\nMúsicas lançadas em 2022:")
for m in musicas:
    if m["Ano"] == "2022":
        print(m["Música"])
mais_tocada = max(musicas, key=lambda x: int(x["Streams"]))
print("\nMúsica com mais streams:")
print(f"{mais_tocada['Música']} - {mais_tocada['Artista']} ({mais_tocada['Streams']} streams)")

