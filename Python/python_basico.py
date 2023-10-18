# -*- coding: utf-8 -*-
"""Python-basico.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1APBS5CTVKYtujLYukzys1pAMd3kKV799
"""

#TIPOS PRIMITIVOS
x = 2
print(type(x))

x = 'Olá Mundo!'
print(x)
print(type(x))

y = 3
x = 3
print(x == y)

#OPERADORES ARITMÉTICOS
x = 2**3
print(x)

x = 10//3
print(x)

x = 10%3
print(x)

#OPERADORES RELACIONAIS
a = 2
b = 3
print(a>=b)

#FUNÇÃO PRINT
print('Olá mundo, 2.5, 2, True, False')

numero = 10
print(f'O número no conjunto é:{numero}')

#FUNÇÃO INPUT
brinquedo = input ('Qual o seu brinquedo favorito: ')
bebida = input ('Você bebe alguma coisa?')
idade = input ('Digite sua idade: ')

print(f'Seu brinquedo favorito é {brinquedo} sua bebida é {bebida} e você tem {idade} anos')

idade = input ('Digite sua idade: ')
print(f'você tem {idade} anos')
print(type(idade))
#O input vem setado como string e tem que converter para inteiro

idade = int(input ('Digite sua idade: '))
print(f'você tem {idade} anos')
print(type(idade))

peso = float(input('Digite o seu peso: '))
print(f'o seu peso é {peso}KGs')
print(type(peso))

#ESTRUTURAS CONDICIONAIS
num = int(input('Digite um número: '))
if num % 2 == 0:
  print(f'O número {num} é par')
else:
  print(f'O número {num} é impar')

#ESTRUTURAS CONDICIONAIS ANINHADAS E O ELIF
num = int(input('Digite um número: '))
if num > 0:
  print(f'O número {num} é Positivo')
elif num == 0:
  print(f'O número {num} é Neutro')
else:
  print(f'O número {num} é Negativo')

#OPERADOR LÓGICO AND
resposta = int(input('Qual a sua idade? '))
if resposta >=18 and resposta <=65:
  print('Você é obrigado a votar')
else:
  print('Você não é obrigado a votar')

#OPERADOR LÓGICO OR
print('1.Idoso')
print('2.Gestante')
print('3.Cadeirante')
print('4.Nenhum desses')
resposta = int(input('Qual é você? '))
if (resposta == 1) or (resposta == 2) or (resposta == 3):
  print('Você se encaixa na fila de prioridade')
else:
  print('Você não se encaixa na fila de prioridade')

#OPERADOR LÓGICO NOT

#VETORES E MATRIZES
imc = [1.81, #altura
       100, #peso
       40] #idade

print(imc)

def vet_add(vet1,vet2):
  return [ vet1_i + vet2_i
          for vet1_1, vet2_1 in zip(vet1, vet2)]
#utilização de cadastro e armazenar em um veto de nome

def vet_sub(vet1,vet2):
  return [ vet1_i - vet2_i
          for vet1_1, vet2_1 in zip(vet1, vet2)]

def vet_sum(vets):
  return reduz(vet_add,vets,vetX,vetD)
vet_sum = part(reduz,vet_sum)

def scalar_mult(n, v):
  return{n * v_i for v_i in v}

#MATRIZES
import numpy as np

matriz = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(matriz)

#elementos de matriz
elemento = matriz[0,1]
#Obtém o elemento na linha 0 e coluna 1(valor2)
#Obtendo o número de linhas e colunas
num_linhas = matriz.shape[0]
num_colunas = matriz.shape[1]
#Iterando sobre elementos da matriz
for linha in matriz:
  for elemento in linha:
    print(elemento)

matriz1 = np.array([[1,2], [3,4]])
matriz2 = np.array([[5,6], [7,8]])

soma = matriz1 + matriz2
produto = np.dot(matriz1, matriz2)
print(produto)

#matriz_transposta = matriz.exemplo


a=1
b=2
a=b
print(a)

#indexação booleana

matriz = np.array([[0,1,2], [3,4,5], [6,7,8]])
condicao = matriz > 5
#croa uma matriz de booleanos baseada na condição
elementos_maiores_que_5 = matriz [condicao]
#obtém elementos maiores que 5
#Outra operações uteis incluem: média,mínimo,máximo]
media = np.mean(matriz)
valor_minimo = np.min(matriz)
valor_maximo = np.max(matriz)
print(matriz)
print(valor_minimo)
print(valor_maximo)
print(media)