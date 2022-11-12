#問1

n = int(input("自然数を入力してください = "))

while True:
  print(n)
  if n == 1:
    break
  elif n % 2 == 0:
    n = n / 2
  else:
    n = 3 * n + 1

print(n)