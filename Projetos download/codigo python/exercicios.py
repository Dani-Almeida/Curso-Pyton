#Faça um programa que receba quatro números inteiros, calcule e mostre a soma desses números.
'''n1 = int(input("Informe o primeiro número:\n"))
n2 = int(input("Informe o segundo número:\n"))
n3 = int(input("Informe o terceiro número:\n"))
n4 = int(input("Informe o quarto número:\n"))

soma = n1 + n2 + n3 + n4

print("Resultado da soma: ", soma)'''
#fim


#Faça um programa que receba três notas, calcule e mostre a média aritmética entre elas.
'''nota1 = float(input("Informe a primeira nota:\n"))
nota2 = float(input("Informe a segunda nota:\n"))
nota3 = float(input("Informe a terceira nota:\n"))

media = (nota1 + nota2 + nota3) / 3

print("Média: ", media)'''
#fim




#Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas.
'''nota1 = float(input("Insira a primeira nota:\n"))
peso1 = float(input("Insira o peso da primeira nota:\n"))
nota2 = float(input("Insira a segunda nota:\n"))
peso2 = float(input("Insira o peso da segunda nota:\n"))
nota3 = float(input("Insira a terceira nota:\n"))
peso3 = float(input("Insira o peso da terceira nota:\n"))

media = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso3)

print("Média ponderada: ", media)'''
#fim




#Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%
'''salario = float(input("Insira o salário:\n"))

aumento_percentual = 25

novo_salario = salario + (salario * aumento_percentual / 100)
#ou novo_salario = salario + salario*0.25

print("O novo salário é: ", novo_salario)'''
#fim




# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
'''sal = float(input("Insira o salario:\n"))
perc = float(input("Insira o percentual de aumento:\n"))

aumento = sal * perc/100
novo_sal = sal + aumento

print("Valor do aumento: ", aumento)
print("Novo salárioo: ", novo_sal)'''
#fim




# Faça um programa que receba o salário-base de um funcionário, calcule e mostre o salário a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga imposto de 7% sobre o salário-base.
'''sal = float(input("Insira o salário base:\n"))

liquido = sal + sal*0.05 - sal*0.07

print("Salário a receber: ", liquido)'''
#fim




# Faça um programa que receba o salário-base de um funcionário, calcule e mostre o seu salário a receber, sabendo-se que esse funcionário teve gratificação de R$ 600,00 e paga imposto de 10% sobre o salário base.
'''sal = float(input("Insira o salário base:\n"))

liquido = sal + 600 - sal*0.10

print("Salário a receber: ", liquido)'''
#fim





# Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento.


'''valor = float(input("Insira o valor do depósito:\n"))

taxa = float(input("Qual é a taxa?\n"))

rendimento = valor * taxa/100
total = valor + rendimento


print("Rendimento: ", rendimento)
print("Valor total: ", total)'''





#Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que: Área = (base * altura)/2.

'''base = float(input("Insira a base:\n"))
altura = float(input("Insira a altura:\n"))

area = (base*altura)/2

print("Área do triângulo: ", area)'''



#Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = Pi * R², aonde Pi = 3,14.

'''raio = float(input("insira o raio:\n"))

pi = 3.14

area = (raio*raio) * pi
# area = pi * raio**2

print("Área do círculo: ", area)'''




# Jeremias possui um cronômetro que consegue marcar o tempo apenas em segundos. Sabendo disso, desenvolva um algoritmo que receba o tempo cronometrado, em segundos, e diga quantas horas, minutos e segundos se passaram a partir do tempo cronometrado.

'''seg = int(input("Insira o tempo em segundos: \n"))

hora = int(seg / 3600)
seg = seg % 3600
mi = int(seg / 60)
seg = seg % 60

print("Horas: ", hora)
print("Minutos: ", mi)
print("Segundos: ", seg)'''



#Desenvolva um algoritmo que simule um caixa eletrônico. O usuário deve inserir o valor total a ser sacado da máquina e o algoritmo deve informar quantas notas de 100, 50, 20, 10, 5 ou 2 reais serão entregues. Deve-se escolher as notas para que o usuário receba o menor número de notas possível.
'''saque = float(input("Insira o valor a sacar:\n"))

cem = int(saque / 100)
saque = saque % 100
cinq = int(saque / 50)
saque = saque % 50
vinte = int(saque / 20)
saque = saque % 20
dez = int(saque / 10)
saque = saque % 10
cinco = int(saque / 5)
saque = saque % 5
dois = int(saque / 2)

print("nº notas R$ 100,00: ", cem)
print("nº notas R$ 50,00: ", cinq)
print("nº notas R$ 20,00: ", vinte)
print("nº notas R$ 10,00: ", dez)
print("nº notas R$ 5,00: ", cinco)
print("nº notas R$ 2,00: ", dois)'''


# Faça um programa que receba um número positivo e maior que zero, calcule e mostre: a) o número digitado ao quadrado; b) o número digitado ao cubo; c) a raiz quadrada do número digitado; d) a raiz cúbica do número digitado.


'''import math

num = float(input("Insira um número:\n"))

qua = num**2
cub = num**3
rquad = math.sqrt(num)
rcub = num**(1/3)

print("Quadrado: ", qua)
print("Cubo: ", cub)
print("Raiz quadrada: ", rquad)
print("Raiz cúbica: ", rcub)'''




#Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.

'''A = float(input("Insira o primeiro número:\n"))
B = float(input("Insira o segundo número:\n"))
potencia = A**B
print("Resultando: ", potencia)'''




# Sabe-se que: 1 pé = 12 polegadas; 1 jarda = 3 pés; 1 milha = 1760 jardas; Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados. a) polegadas; b) jardas; c) milhas.

'''pes = float(input("Insira a medida em pés:\n"))

pol = pes*12
jar = pes/3
mil = jar/1760

print("Polegadas: ", pol)
print("Jardas: ", jar)
print("Milhas: ", mil)'''



# Faça um programa que receba o ano de nascimento de uma pessoa e ano atual, calcule e mostre: a) a idade dessa pessoa; b) quantos anos essa pessoa terá em 2030;

ano = int(input("Insira o ano de nascimento:\n"))

anoAtual =int (input("Insira ano atual:\n"))


print("Idade atual: ", anoAtual - ano )
print("Idade em 2030: ", 2030 - ano)

