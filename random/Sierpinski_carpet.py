import numpy as np 
from PIL import Image 
  
print('Введите глубину фрактала:')
depth = int(input())
size = 3 ** depth 
  
# Создание рисунка 
square = np.empty([size, size, 3], dtype = np.uint8) 
color = np.array([255, 255, 255], dtype = np.uint8) 
square.fill(8) 
  
for i in range(0, depth + 1): 
    lvl = 3 ** (depth - i) 
    for x in range(0, 3 ** i): 

# Поиск центрального квадрата и замена цвета
        if x % 3 == 1: 
            for y in range(0, 3 ** i): 
                if y % 3 == 1: 
                    square[y * lvl : (y + 1) * lvl, x * lvl : (x + 1) * lvl] = color 
  
# Визуализация
Image.fromarray(square).save("carpet.jpg") 
Image.open("sierpinski.jpg").show() 

