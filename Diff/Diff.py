import numpy as np
import matplotlib.pyplot as plt
import itertools as it


### Раскладывает логарифм в ряд и вычисляет соответсвующие конечные разности функции f
def DecompositionLn(x, presion):
    decomposition = 0
    for k in np.arange(1, presion + 1):
        deltaKF = 0
        for s in np.arange(0, presion + 1):
            ### Биноминальный коэффициент для вычисления k конечной разности от f
            c_k_s = len(list(it.combinations(np.arange(0, k), s)))
            deltaKF += c_k_s * ((-1) ** s) * f(x + (k - s) * h)
        decomposition +=  ((((-1) ** (k+1)) * deltaKF) / k)
        
    return decomposition

h = 1
f = lambda x: np.exp(x)
delta = lambda x: f(x+h) - f(x)
dfdx = lambda x, presion: (1/h) * DecompositionLn(x, presion)

xR = np.arange(-1.5, 3.5, 0.01)
fR = f(xR)
dfdxR = dfdx(xR, 2)

plt.plot(xR, fR, color = "Blue", label = "Функция")
plt.plot(xR, dfdxR, color = "Red", label = "Производная")

plt.legend()
plt.show()