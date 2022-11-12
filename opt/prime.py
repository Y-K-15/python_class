# 例題 与えられた整数が素数かどうか判定する

n = 71
d = 2

while d <= n-1:
    # if n % d == 0:
    #     break
    # d = d + 1
    
    
if d == n:
    print(n , "is prime number")
else:
    print(n , "is not prime number")


#  割る数を中間までという方針に変えた場合，
# プログラムをどのように変更したらよいか？

n = 12
d = 2

while d**2 <= n:     # この <= の = はとても重要！
    if n % d == 0:
        break
    d = d + 1

if d**2 <= n:
    print(n , "is not prime number")
else: #d = d + 1　を最後にしているから最後までwhileを回しきったら　d^2はｎより大きくなっている。
    print(n , "is prime number")


# while d**2 <= n:     # この <= の = はとても重要！
# →→これをしないと平方数が素数になってしまう