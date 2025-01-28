numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))

op = input("Digite a operação(+, -, *, /): ")

if op == '+':
    print(numero1 + numero2)
elif op == '-':
    print(abs(numero1 - numero2))
elif op == '*':
    print(numero1 * numero2)
elif op == '/':
    print(numero1 / numero2)
else:
    print("Operação inválida!")
