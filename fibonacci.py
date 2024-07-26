def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Número de termos que você quer exibir
num_terms = 20
fibonacci_sequence = fibonacci(num_terms)

print(f"Sequência de Fibonacci com {num_terms} termos:")
for number in fibonacci_sequence:
    print(number)