# Tabuada Automática
# Peça um número e exiba a tabuada de 1 a 10 usando for.

n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
