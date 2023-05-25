# Ley de la suma
def f(n):

    # n pasos
    for i in range(n):
        print(i)

    # n pasos
    for i in range(n):
        print(i)

# Big O notation:
# O(n) + O(n) = O(n + n) = O(2n) = O(n)
# Función con crecimiento de tiempo lineal respecto de n
# Da lo mismo si es 2n o n.

# ---------------------


# Ley de la suma
def f(n):

    # n pasos
    for i in range(n):
        print(i)

    # n**2 pasos
    for i in range(n*n):
        print(i)


# Big O notation:
# O(n) + O(n*n) = O(n + n**2) = O(n**2)
# Función con crecimiento de tiempo cuadratico respecto de n
# Sólo importa el término más grande

# ---------------------


# Ley de la multiplicación
def f(n):

    # n pasos
    for i in range(n):
        print(i)

        for j in range(n):
            print(i, j)


# Big O notation:
# O(n) * O(n) = O(n * n) = O(n**2)


# ---------------------

# Recursividad múltiple
def fibonnaci(n):
    if n == 0 or n == 1:
        return 1

    return fibonnaci(n - 1) + fibonnaci(n - 2)

# Big O notation:
# O(2**n)
# Por cada llamada a fibonnaci lo llamamos 2 veces. Crecimiento exponencial.