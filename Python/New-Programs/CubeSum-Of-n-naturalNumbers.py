number = 7

# print(5%10)
# print(5/10)
# print(5//10)

sum = 0
for i in range(0,number+1):
  print("Number is :",i)
  sum = sum + i*i*i
  print("Sum Of Numbers :", sum)

# (n*(n+1)/2)

def cubes_number(n):
  x = (n*(n+1)/2) # 7 * 8/2 = 32
  return (int)(x*x) # 32*32

print(cubes_number(7))

even_Cubes = []
odd_Cubes = []

def cubes(n):
  x = 0
  if n % 2 == 0:
    x = (n/2)*(n+1)
    even_Cubes.append(x)
  else:
    x = ((n+1)/2)*n
    odd_Cubes.append(x)
  return (int)(x*x)

print(cubes(10))

print(even_Cubes)
print(odd_Cubes)

