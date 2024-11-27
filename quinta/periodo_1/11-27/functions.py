def fibonacci_1(n):
    """Stampa la successione di Fibonacci < n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

def fibonacci_2(n):
    fibonacci_seq = []
    a, b = 0, 1
    while a < n:
        fibonacci_seq.append(a)
        a, b = b, a+b
    return fibonacci_seq

def fibonacci_3(n, a = 0, b = 1):
    fibonacci_seq = []
    while a < n:
        fibonacci_seq.append(a)
        a, b = b, a+b
    return fibonacci_seq

somma_prodotto = lambda x,y: (x+y, x*y)

moltiplicazione = lambda a,b: a*b

fibonacci_1(90)

sequenza = fibonacci_2(90)
print(sequenza)

print(fibonacci_3(90))
print(fibonacci_3(90, 8, 13))

x, y = 5.4, 8.1

somma, prodotto = somma_prodotto(x, y)
print(f"La somma di {x} e {y} è {somma}")
print(f"Il prodotto di {x} e {y} è {prodotto}")

print(moltiplicazione(5, 6))