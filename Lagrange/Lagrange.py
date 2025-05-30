import matplotlib.pyplot as plt

# Рисует графики
## Может не запускаеться автоматически. Возможно понадобиться перейти в 
## директорию, где храниться соответствующий файл с данными


with open("Lagrange.txt", "r") as file:
    x =  file.readline().split(" ")
    y = file.readline().split(" ")
    x.remove('\n')
    y.remove('\n')
    x = list(map(float, x))
    y = list(map(float, y))
    pointsx = file.readline().split(" ")
    pointsy = file.readline().split(" ")
    pointsx.remove('\n')
    pointsy.remove('')

print(x)
print(y)
plt.plot(x, y, color = "Blue")
plt.scatter(pointsx, pointsy, color = "Red")

plt.show()



    