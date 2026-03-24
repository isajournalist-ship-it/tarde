
letra = input("Digite a letra do estado civil (C, S, D, V, O): ").upper()

if letra == "C":
    print("C - Casado")
elif letra == "S":
    print("S - Solteiro")
elif letra == "D":
    print("D - Divorciado")
elif letra == "V":
    print("V - Viúvo")
elif letra == "O":
    print("O - Outros")
else:
    print("Letra inválida")