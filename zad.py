def sq_sum(a, b):
    return (a+b)**2
# TUTAJ PSUJ


assert sq_sum(1, 1) == 4, "FAILED"
print("First PASSED")
assert sq_sum(2.5, 1.5) == 16, "FAILED"
print("Sec PASSED")

assert sq_sum(-2, -1) == 9, "FAILED"
print("Third PASSED")
assert sq_sum(0, 0) == 0, "FAILED"
print("Fourth PASSED")


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
#rekurencja !


assert factorial(5) == 120, "FAILED"
print("Factorial PASSED")

assert factorial(0.5) == 1, "FAILED"
print("Silnia przyjmuje tylko liczby całkowite")

