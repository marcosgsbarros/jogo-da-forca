import os
from random import choice
import time

#(Jogo da forca) o jogador terá 6 chances para acertar a palavra sorteada aleatóriamente pelo computador

''' Código abaixo faz a leitura dos arquivos de texto 'txt' 
e retorna uma lista de palavras de acordo com o nível escolhido pelo jogador 
'''
with open('palavras_dificuldade_baixa.txt','r') as palavras_faceis:
    lista_palavras_faceis = [palavra.replace('\n','') for palavra in palavras_faceis]
with open('palavras_dificuldade_media.txt','r') as palavras_medias:
    lista_palavras_medias = [palavra.replace('\n','') for palavra in palavras_medias]
with open('palavras_dificuldade_alta.txt','r') as palavras_dificeis:
    lista_palavras_dificeis = [palavra.replace('\n','') for palavra in palavras_dificeis]
    
lista_letras_digitadas = [] # Lista que recebe todas as letras digitadas
letra = '' # Essa variável recebe a ultima letra digitada
palavra_oculta = [] # Lista recebe '-' traços em cada letra da palavra sorteada
erros = 0 # Variável recebe acumula o total do contador de erros

def mostrar_inicio(): #Inicio do jogo, mostra a tela de boas vindas 
    print('=' *40)      
    print('Bem vindo ao jogo da forca')
    print('=' *40)
    print('Escolha uma opção')
    print('0-Iniciar jogo / 1-Sair')
    inicio = input()
    if inicio == '0':
        print('Escolha o nivel de dificuldade das palavras') #opções de nível do jogo
        print('0 - Fácil | 1 - Médio | 2 - dificil')
        nivel_jogo = input()
        os.system('cls')
        iniciar_jogo(nivel_jogo)                
    elif inicio == '1':
        exit()

def iniciar_jogo(nivel_do_jogo):#Inicia o jogo, faz o sorteio da palavra de acordo com o nivel escolhido acima
    if nivel_do_jogo == '0':
        jogo = 'Nível fácil'
        os.system('cls')
        palavra = choice(lista_palavras_faceis)
        palavra = palavra.upper()
        jogo_nivel(jogo,palavra)
    elif nivel_do_jogo == '1':
        jogo = 'Nível médio'
        os.system('cls')
        palavra = choice(lista_palavras_medias)
        palavra = palavra.upper()
        jogo_nivel(jogo,palavra)
    elif nivel_do_jogo == '2':
        jogo = 'Nível difícil'
        os.system('cls')
        palavra = choice(lista_palavras_dificeis)
        palavra = palavra.upper()
        jogo_nivel(jogo,palavra)
    return palavra

def jogo_nivel(nivel,palavra_sorteada:str):                             
    for i in range(len(palavra_sorteada)): #Essa função esconde a palavra sorteada 
        palavra_oculta.append('-')
    while True:
        print(nivel)
        print(f'A palavra contem {len(palavra_sorteada)} letras')
        while True:
            letra = input('Digite uma letra:') #solicita uma letra para o jogador  
            letra = letra.upper()
            for y in lista_letras_digitadas: 
                if letra == y:
                    print('Essa letra ja foi digitada')
                    time.sleep(1)
                    lista_letras_digitadas.remove(letra)#se a letra foi digitada ela é excluida da lista
            if len(letra) > 1:
                print('Você só pode digitar uma caractere por vez')
            elif letra == '' or letra == ' ' or letra.isdigit():#verifica se o jogador digitou uma letra
                print('Você não digitou uma letra')
            else:
                break        
        os.system('cls')
        print('Letras Digitadas')
        lista_letras_digitadas.append(letra) # adiciona as letras digitadas numa lista e exibe na tela
        print('-'.join(lista_letras_digitadas))
        print('=' * 40)
        verificar_letra(letra,palavra_sorteada)
        
def verificar_letra(letra_digitada,palavra_sorted):#Função que verifica cada letra digitada 
    if letra_digitada not in palavra_sorted: 
        global erros #verifica se o jogador atingiu o limite máximo de erros              
        erros += 1
        if erros == 6:
            print(f'Você perdeu!! A palavra era {palavra_sorted}')
            exit()
    if letra_digitada in palavra_sorted:
        for i,x in enumerate(palavra_sorted):
            if letra_digitada == x: #se a letra estiver
                palavra_oculta[i] = x #na palavra sorteada a função exibe a letra na determinada posição
    if not '-' in palavra_oculta:
        print('PARABÉNS! Você descobriu a palavra')#Se acertar todas as letras te parabeniza
        print(*palavra_oculta)
        exit()
    print(*palavra_oculta)#Exibe as letras corretas da palavra oculta
    

mostrar_inicio() #chama a função que inicia o jogo


