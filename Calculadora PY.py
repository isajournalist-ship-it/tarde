''''numero1 = int(input("Digite um numero"))
numero2 = int(input("Digite um numero"))
soma = numero1+numero2
divisao = numero1/numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
potenciacao = numero1**numero2

print(f"O resultado da operaçao e soma")'''

operacao = input('Digite a operacao desejada (+, -, /, *, **): ')
numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))
soma = numero1+numero2
divisao = numero1/numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
potenciacao = numero1**numero2

"""

if operacao == "+":
    print(f"soma: {soma}")
elif operacao == "-":
    print(f"subtracao: {subtracao}")
elif operacao == "/":
    print(f"divisao: {divisao}")
elif operacao == "*":
    print(f"multiplicacao: {multiplicacao}")
elif operacao == "**":
    print(f"potenciacao: {potenciacao}")
else:
    print ("Operaçao invalida!")
"""

operacao = input('Digite a operacao desejada (+, -, /, *, **): ')

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if operacao == "+":
    print(f"soma: {numero1 + numero2}")
elif operacao == "-":
    print(f"subtracao: {numero1 - numero2}")
elif operacao == "/":
    if numero2 != 0:
        print(f"divisao: {numero1 / numero2}")
    else:
        print("Erro: divisao por zero!")
elif operacao == "*":
    print(f"multiplicacao: {numero1 * numero2}")
elif operacao == "**":
    print(f"potenciacao: {numero1 ** numero2}")
else:
    print("Operacao invalida!")

    