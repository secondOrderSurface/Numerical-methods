import numpy as np
import matplotlib.pyplot as plt
import bisect

### Кубический сплайн с естественными граничными условиями


### Создает трехдиагональную матрицу
def CreateTriMatrix(n):
    A = [h(i) / (h(i) + h(i + 1)) for i in np.arange(n - 2)] + [0]
    B = [2] * n
    C = [0] + [(h(i + 1) / (h(i) + h(i + 1))) for i in np.arange(n - 2)]
    return A, B, C

### Создает столбец решение для системы [TDM][x] = [D] 
def CreateD(n):
    print([0] + [6 * ((f_i[i + 1] - f_i[i]) / h(i) - (f_i[i] - f_i[i - 1]) / h(i - 1)) / (h(i) + h(i-1)) for i in range(1, n - 1)] + [0])
    return [0] + [6 * ((f_i[i + 1] - f_i[i]) / h(i) - (f_i[i] - f_i[i - 1]) / h(i - 1)) / (h(i) + h(i-1)) for i in range(1, n - 1)] + [0]

### Находит решение системы
def SolveTriDiag(A, B, C, D):
    c_p = C + [0]
    d_p = [0] * len(B)
    X = [0] * len(B)
    
    c_p[0] = C[0] / B[0]
    d_p[0] = D[0] / B[0]
    for i in np.arange(1, len(B)):
        c_p[i] = c_p[i] / (B[i] - c_p[i - 1] * A[i - 1])
        d_p[i] = (D[i] - d_p[i - 1] * A[i - 1]) / (B[i] - c_p[i - 1] * A[i - 1])
        
    X[-1] = d_p[-1]
    for i in np.arange(len(B) - 2, -1, -1):
        X[i] = d_p[i] - c_p[i] * X[i + 1]
        
    return X

### Находит значение сплайна в точке val
def Spline(val):
    idx = min(bisect.bisect(x_i, val)-1, n-2)
    z = (val - x_i[idx]) / h(idx)
    C = coefficients[idx]
    return (((C[0] * z) + C[1]) * z + C[2]) * z + C[3]

x_i = list(map(float, input("Введите значения x : \n").split(" ")))
f_i = list(map(float, input("Введите значения f(x) : \n").split(" ")))

h = lambda i: x_i[i+1] - x_i[i]
n = len(x_i)

### Создание соотвествующих диагоналей и столбца решений
A, B, C = CreateTriMatrix(n)
D = CreateD(n)

### Поиск решение и вычисление коэффицентов сплайна
M = SolveTriDiag(A, B, C, D)
coefficients = [[(M[i+1]-M[i])*h(i)*h(i)/6, M[i]*h(i)*h(i)/2, (f_i[i+1] - f_i[i] - (M[i+1]+2*M[i])*h(i)*h(i)/6), f_i[i]] for i in np.arange(n-1)]


### Графики
xRange = np.arange(min(x_i), max(x_i) + 0.1, 0.01)
yRange = []
for i in xRange:
    yRange.append(Spline(i))

plt.scatter(x_i, f_i, color = "Blue")
plt.plot(xRange, yRange, color = "Red")
plt.show()
