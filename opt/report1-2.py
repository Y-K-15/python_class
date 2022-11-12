#問2

a = int(input("辺a = "))
b = int(input("辺b = "))
c = int(input("辺c = "))

if (a <= 0) or (b <= 0) or (c <= 0):
  print("入力は０より大きい数でしてください")
else:
  if (a < b + c) and (b < a + c) and (c < a + b):
    print("三角形は成立します")
  else:
    print("三角形は成立しません")
