"""
Programa adulto
Descrição: Este programa pergunta a idade de uma pessoa.
Se a idade for maior do que 18 anos, o programa imprime
na tela o texto "Oi! Você e um adulto.". Caso contrário, imprima ”Oi! Vocˆe  ́e menor de idade"
Autor: Nelson
Data: 24/03/2026
Versão: 0.1.0
"""


# Alocação de memória

idade = 0

texto = ""



# Entrada de dados

idade = int(input("\nQual é a sua idade? "))


# Processamento de dados

if idade >= 18:
    texto = "Oi! Você e um adulto."
else:
    texto = "Oi! Você e menor de idade"


# Saída de dados

print(texto)
