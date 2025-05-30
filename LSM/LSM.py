import numpy as np
import matplotlib.pyplot as plt

### Поиск наилучшешго аппроксимирующего полинома по МНК 
def LSMCoefs(x_i, f_i):
    
    n = len(x_i)
    bestA = np.zeros(1)
    infelicity = 0
    mWin = 1 
    for m in np.arange(1, n):
        s = np.zeros((m + 1))
        q = np.zeros((m + 1))
        p = np.zeros((m + 1, n))
        
        ### Вычисляем значения ортоганальный полиномов в точках x
        for i in np.arange(0, m+1):
            if (i == 0):
                for j in np.arange(0, n):
                    p[0][j] = 1.0
            elif (i == 1):
                for j in np.arange(0, n):
                    p[i][j] = (x_i[j] - q[i-1] / s[i-1])
            else:
                for j in np.arange(0, n):
                    p[i][j] = (x_i[j] - q[i-1] / s[i-1]) * p[i-1][j] - (s[i-1] / s[i-2]) * p[i-2][j]
            for j in np.arange(0, n):
                s[i] += p[i][j] ** 2
                q[i] += (p[i][j] ** 2) * x_i[j]
                
        
        ### Вычисляем соотвествующие ckj   
        c = np.diag(np.ones(m+1))
        for k in np.arange(1, m+1):
            for j in np.arange(0, k):
                if (j == 0):
                    c[k][j] = (-(q[k-1] / s[k-1]) * c [k-1][j])
                elif (j == k + 1):
                    c[k][j] = c[k-1][j-1] - (q[k-1] / s[k-1]) * c [k-1][j]
                else:
                    c[k][j] = c[k-1][j-1] - (q[k-1] / s[k-1]) * c [k-1][j] - (s[k-1] / s[k-2]) * c [k-2][j]
                        
        
        ### Находим коэффиценты при ортогональный полиномах             
        b = np.zeros(m+1)
        for k in np.arange(0, m+1):
            for i in np.arange(0, n):
                b[k] += ((f_i[i] * p[k][i]) / s[k])
        
        ### Коэффиценты аппроксимирующего полинома 
        a = np.zeros(m+1)
        
        for j in np.arange(0, m+1):
            for k in np.arange(j, m+1):
                a [j] += b[k] * c[k][j]
        
        
        ### Анализ погрешностей для полинома степени m+1
        localInfelicity = 0 
        for i in np.arange(0, n):
            localInfelicity += ((f_i[i] - Polynom(x_i[i], a)) ** 2)
        
        if (m == 1):
            infelicity = localInfelicity
            bestA = a
            mWin = m
        elif (localInfelicity < infelicity):
            infelicity = localInfelicity
            bestA = a
            mWin = m
    
    print(mWin + 1)
    return bestA

### Значение полинома с набором коэффицентов a в точке x
def Polynom(x, a):
    result = 0
    for i in np.arange(0, len(a)):
        result += a[i] * (x ** i)
    return result


###x_i = list(map(float, input("Введите значения x : \n").split(" ")))
###f_i = list(map(float, input("Введите значения f(x) : \n").split(" ")))

x_i = np.random.randint(100, size= 50)
f_i = np.random.randint(100, size= 50)

a = LSMCoefs(x_i, f_i)

xRange = np.arange(min(x_i) - 1, max(x_i) + 1, 0.1)
yRange = Polynom(xRange, a)

polyfitCoefs = np.flip(np.polyfit(x_i, f_i, len(a) -1))

plt.scatter(x_i, f_i, color = "Blue")
plt.plot(xRange, yRange, color = "Red", label = "LSM")
plt.plot(xRange, Polynom(xRange, polyfitCoefs), color = "Green", label = "Polyfit")

plt.legend()
plt.show()

