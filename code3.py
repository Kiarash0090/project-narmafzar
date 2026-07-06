import numpy as np
from scipy.integrate import fixed_quad

def f(x):
    return np.exp(x**2)

def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        n += 1
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

a = 0.0
b = 1.0
n = 100
gauss_n = 5

trap_result = trapezoidal_rule(f, a, b, n)
simpson_result = simpson_rule(f, a, b, n)
gauss_result, _ = fixed_quad(f, a, b, n=gauss_n)

reference_result = simpson_rule(f, a, b, 10000)

trap_error = abs(reference_result - trap_result)
simpson_error = abs(reference_result - simpson_result)
gauss_error = abs(reference_result - gauss_result)

print("Integral of exp(x^2) on [0,1]")
print("-" * 40)
print(f"Trapezoidal Rule : {trap_result:.12f}")
print(f"Simpson Rule     : {simpson_result:.12f}")
print(f"Gaussian Quad    : {gauss_result:.12f}")
print(f"Reference Value  : {reference_result:.12f}")
print("-" * 40)
print(f"Trapezoidal Error: {trap_error:.12e}")
print(f"Simpson Error    : {simpson_error:.12e}")
print(f"Gaussian Error   : {gauss_error:.12e}")
print("-" * 40)

if trap_error < simpson_error and trap_error < gauss_error:
    best_method = "Trapezoidal Rule"
elif simpson_error < trap_error and simpson_error < gauss_error:
    best_method = "Simpson Rule"
else:
    best_method = "Gaussian Quadrature"

print("Comparison Report:")
print(f"The integral of exp(x^2) over [0,1] was computed using three methods.")
print(f"Among the methods, {best_method} produced the closest result to the reference value.")
print("Trapezoidal Rule is less accurate because it uses linear approximation.")
print("Simpson Rule is more accurate because it uses quadratic approximation.")
print("Gaussian Quadrature is usually very accurate with fewer evaluation points.")