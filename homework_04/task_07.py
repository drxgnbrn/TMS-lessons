#Напишите функцию generate_natural_cubes(n),
#которая принимает число n и возвращает список,
#состоящий из кубов первых n натуральных чисел.

def generate_natural_cubes(n):
  return [i**3 for i in range(1, n+1)]

n = int(input("Enter a number: "))
print(generate_natural_cubes(n))