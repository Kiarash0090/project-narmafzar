import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x_data = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y_data = np.array([1, 3, 5, 8, 5, 2], dtype=float)

x = sp.Symbol('x')
n = len(x_data)

P = 0
for i in range(n):
    L_i = 1
    for j in range(n):
        if i != j:
            L_i *= (x - x_data[j]) / (x_data[i] - x_data[j])
    P += y_data[i] * L_i

P = sp.expand(P)

print("Lagrange Polynomial:")
print(P)
print("\nLagrange Coefficients (Highest degree first):")
print(sp.Poly(P, x).all_coeffs())

cs = CubicSpline(x_data, y_data, bc_type='natural')

print("\nCubic Spline Coefficients per interval:")
for i in range(len(x_data) - 1):
    a = cs.c[0, i]
    b = cs.c[1, i]
    c = cs.c[2, i]
    d = cs.c[3, i]
    print(f"\nInterval [{x_data[i]}, {x_data[i+1]}]:")
    print(f"S{i}(x) = {a:.6f}(x-{x_data[i]})^3 + {b:.6f}(x-{x_data[i]})^2 + {c:.6f}(x-{x_data[i]}) + {d:.6f}")

xx = np.linspace(1, 6, 400)
P_func = sp.lambdify(x, P, 'numpy')
yy_lagrange = P_func(xx)
yy_spline = cs(xx)

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'ro', label='Data Points')
plt.plot(xx, yy_lagrange, 'b-', label='Lagrange Interpolation')
plt.plot(xx, yy_spline, 'g--', label='Cubic Spline')
plt.legend()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange vs Cubic Spline Interpolation')
plt.show()