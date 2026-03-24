"""
Programa adulto
Descrição: Este programa que pergunte a idade de uma pessoa. Se a
idade for menor que 13 anos, imprima na tela ”Oi! Vocˆe  ́e uma
crian ̧ca.”Se idade for de 13 a 17, imprima ”Oi, Vocˆe  ́e um
adolescente.”. Se a idade maior que 17 anos imprima ”Oi! Voce
eh um adulto.”
Autor: Nelson
Data: 24/03/2026
Versão: 1.0.0
"""


# Alocação de memória

idade = 0

texto = ""


# Entrada de dados

idade = int(input("\nQual é a sua idade? "))


# Processamento de dados

if idade >= 18:
    texto = "Oi! Você e um adulto."

elif idade > 13 and idade <=17:
    texto = "Oi, Você e um adolescente."   
    
else:
    texto = "Oi! Você é criança"



# Saída de dados

print(texto)