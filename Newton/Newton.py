import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Рисует графики
## Может не запускаеться автоматически. Возможно понадобиться перейти в 
## директорию, где храниться соответствующий файл с данными


with open("Newton.txt", "r") as file:
    x =  file.readline().split(" ")
    y = file.readline().split(" ")
    x.remove('\n')
    y.remove('')
    x = list(map(float, x))
    y = list(map(float, y))


print(list(map(float, y)))
plt.plot(x, y)
plt.show()

    