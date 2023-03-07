n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print("1")
else:
    for count in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)

fibonacci = [0, 1]

while fibonacci[-1] < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if n in fibonacci:
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")
