numero = int(input("Digite um número para ser verificado:"))

resto = numero % 2
if (numero <=0):
    print("Valor inválido!")
elif (resto == 0):
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é IMPAR!")