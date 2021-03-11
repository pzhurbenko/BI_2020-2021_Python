# правильно ли я выполнил задание? Или необходимо было сделать без itertools?

from itertools import product
n = int(input("Введите длину: "))

def all_DNA(n):
  result = []
  DNA = ["A", "T", "G", "C"]
  for i in range(1, n + 1):
    iteration = [''.join(word) for word in product(DNA, repeat = i)]
    result.extend(iteration)
  print(result)

all_DNA(n)
