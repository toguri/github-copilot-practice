# fizz-buzz問題のコード
# 1から100までの数字をプリントするプログラムを書け。
# ただし、3の倍数のときは数字の代わりに「Fizz」と、 
# 5の倍数のときは「Buzz」とプリントし、 
# 3と5両方の倍数の場合には「FizzBuzz」とプリントすること。
for i in range(1,101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else: 
        print(i)





