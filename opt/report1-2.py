#問2

#三角形の各辺の長さをa,b,cとして入力させ、それらをそれぞれ変数に入れる
a = float(input("辺aの長さ = "))
b = float(input("辺bの長さ = "))
c = float(input("辺cの長さ = "))

if (a <= 0) or (b <= 0) or (c <= 0): #辺が長さが０以下の場合に処理を進ませない
  print("０より大きい数を入力してください")
else:
  if (a < b + c) and (b < c + a) and (c < a + b): # 三角形の成立条件で三角形が成立するか判定
    print("三角形は成立します")
  else:
    print("三角形は成立しません")
