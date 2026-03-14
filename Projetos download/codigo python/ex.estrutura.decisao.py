
#Faça um programa que receba dois números e mostre o maior deles. Caso eles sejam iguais, deve-se mostrar a mensagem "Os números são iguais".
'''
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

if num1 > num2:
    print("O maior é: ", num1)
elif num2 > num1:
    print("O maior é: ", num2)
else:
    print("Os números são iguais")'''



#) Desenvolva um algoritmo que receba três números. O algoritmo deve imprimir "Condição satisfeita", na tela, caso o primeiro dado inserido seja maior do que os outros dois (o primeiro não pode ser igual a nenhum). Caso contrário, deve ser impressa a 
#mensagem: "Erro".
'''
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

if num1 > num2 and num3:
    print("Condição satisfeita")
else:
    print("Erro")'''




#) Faça um programa que receba um número inteiro e verifique se esse número é par ou ímpar
'''
num = int(input("Insira um número inteiro: "))

resultado =  num % 2 # O % é utilizado para calcular o resto da divisão por 2. Se o resto for zero, é par, se não, é ímpar.

if resultado == 0:
    print("O número", num, "é par.")
if resultado != 0:
    print("O número", num, "é ímpar.")'''




#Desenvolva um algoritmo que receba dois números, calcule e mostre a multiplicação entre eles, se ambos forem iguais. Caso o primeiro seja maior que o segundo, mostre a subtração do primeiro pelo segundo. Caso contrário, mostre a soma entre os dois.

'''
valor1 = int(input("Insira o primeiro valor "))
valor2 = int(input("Insira o segundo valor: "))

if valor1 == valor2:
    print("Multiplicação: ", valor1*valor2)
if valor1 > valor2:
    print("Subtração: ", valor1-valor2)
if valor1 < valor2:
    print("Soma: ", valor1+valor2)'''




#Desenvolva um algoritmo que simule uma calculadora. Você deve dar a opção de o usuário escolher entre: 1 - Somar; 2 - Subtrair; 3 - Multiplicar; 4 - Dividir. O usuário só conseguirá processar dois números inteiros por vez.
'''
print("Digite 1 para somar;")
print("Digite 2 para subtrair;")
print("Digite 3 para multiplicar;")
print("Digite 4 para dividir;")

op = input()

n1 = float(input("Insira o primeiro valor:\n"))
n2 = float(input("Insira o segundo valor:\n"))

if op == "1":
    r = n1 + n2
    print("Soma: ", r)

if op == "2":
    r = n1 - n2 
    print("Subtração: ", r)

if op == "3":
    r = n1 * n2
    print("Multiplicação: ", r)

if op == "4":
    if n2 != 0:
        r = n1 / n2
        print("Divisão: ", r)
    else:
        print("Divisão por zero.")    '''



#Desenvolva um algoritmo que peça para que o usuário informe a base e a altura de um 
#retângulo, e um terceiro número inteiro "op". Caso o usuário escolha "op" igual a 0, 
#calcule e mostre o perímetro do retângulo. Caso o usuário insira um valor 1 para "op", 
#calcule e mostre a área do retângulo. Se o usuário inserir um valor diferente de 0 e 1 
#para "op", mostrar a mensagem "Opção inválida.".
'''
base = float(input("Insira a base:"))
altura = float(input("Insira a altura:"))

print("Ipções de processamento:")
print("Insira 0 para calcular o perímetro;")
print("Insira 1 para calcular a área.")
op = input()

if op == "0" or op == "1":
    if op == "0":
        calc = 2*altura + 2*base
        print("Perímetro: ", calc)
    if op == "1":
        calc = base*altura
        print("Área: ", calc) 
else:
    print("Opção inválida.")'''




#A nota final de um estudante é calculada a 
#partir de três notas atribuídas respectivamente a um trabalho de laboratório, a uma 
#avaliação semestral e a um exame final. A média das três notas mencionadas 
#anteriormente obedece aos pesos a seguir:
#Nota Peso
#Trabalho de laboratório 2
#Avaliação semestral 3
#Exame final 5
#Faça um programa que receba as três notas, calcule e mostre a média ponderada e o 
#conceito que segue a tabela abaixo:
#Média ponderada Conceito
#8,0 ~ 10,0 A
#7,0 ~ 8,0 B
#6,0 ~ 7,0 C
#5,0 ~ 6,0 D
#0,0 ~ 5,0 E

'''
trab = float(input("Insira a nota do trabalho: \n"))
aval = float(input("Insira a nota da avaliação:\n"))
exam = float(input("Insira a nota do exame:\n"))

med = (trab*2 + aval*3 + exam*5)/10

if med >= 8 and med <= 10:
 print("Conceito A.")
if med >= 7 and med < 8:
 print("Conceito B.")
if med >= 6 and med < 7:
 print("Conceito C.")
if med >= 5 and med < 6:
 print("Conceito D.")
if med >= 0 and med < 5:
 print("Conceito E.")'''




#Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem que segue a tabela abaixo. 
#Para alunos de exame, calcule e mostre a nota que deverá ser tirada no exame para 
#aprovação, considerando que a média no exame é 6,0.
#Média aritmética Mensagem
#0,0 ~ 3,0 Reprovado
#3,0 ~ 7,0 Exame
#7,0 ~ 10,0 Aprovado

'''
n1 = float(input("Insira a primeira nota:\n"))
n2 = float(input("Insira a segunda nota:\n"))
n3 = float(input("Insira a terceira nota:\n"))

med = (n1 + n2 + n3)/3

print("Média: ", med)

if med >= 7 and med <= 10:
    print("Aprovado! Parabéns.")

if med >= 3 and med < 7:
    print("Exame.")
    exam = 12 - med
    print("É preciso tira", exam, "no exame")

if med >= 0 and med < 3:
 print("Reprovado.")'''




# Faça um programa que receba três números distintos e mostre-os em ordem crescente.

'''
n1 = float(input("Insira o primeiro número:\n"))
n2 = float(input("Insira o segundo número:\n"))
n3 = float(input("Insira o terceiro número:\n"))

if n1 < n2 and n1 < n3:
    if n2 < n3:
        print(n1, "-", n2, "-",n3)
    else:
        print(n1, "-", n3, "-", n2)
          
if n2 < n1 and n2 < n3:
    if n1 < n3:
        print(n2, "-", n1, "-", n3)
    else:
         print(n2 , "-", n3, "-", n1)

if n3 < n1 and n3 < n2:
    if n1 < n2:
         print(n3 , "-", n1, "-", n2)
    else:
         print(n3 , "-", n2, "-", n1)'''




#Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga esta regra. Mostre, em seguida, os quatro números em ordem não-crescente.


'''
n1 = float(input("Insira o primeiro número:\n"))
n2 = float(input("Insira o segundo número:\n"))
n3 = float(input("Insira o terceiro número:\n"))
n4 = float(input("Insira o quarto número:\n"))

if n4 > n3:
    print(n4, "-", n3, "-", n2, "-", n1)

if n4 > n2 and n4 <= n3:
    print(n3, "-", n4, "-", n2, "-", n1)

if n4 > n1 and n4 <= n2:
    print(n3, "-", n2, "-", n4, "-", n1)

if n4 <= n1:
    print(n3, "-", n2, "-", n1, "-", n4)'''


#Desenvolva um algoritmo que peça ao usuário que informe os coeficientes a, b e c de uma equação de segundo grau: ax² + bx + c. Com base na Fórmula de Bhaskara, calcule e mostre as raízes da respectiva equação de segundo grau.


import math

a = int(input("Insira o coeficiente a:\n"))
b = int(input("Insira o coeficiente b:\n"))
c = int(input("Insira o coeficiente c:\n"))

delta = b**2 - 4*a*c

if delta < 0:
    print("Raízes fora do domínio dos números reais.")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Raiz x':", x1)
    print("Raiz x'':", x2)



