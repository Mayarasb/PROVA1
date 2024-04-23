lista = []
for i in range(3):
    numero = float(input("Digite um número: "))
    lista.append(numero)
lista.sort(reverse=True)
print(f"Números em ordem descrescente: {lista}")

