X = int(input())
N = int(input())

total_price = 0

for i in range(N):
    price, num = map(int,input().split())
    total_price += price*num

if X == total_price:
    print("Yes")
else:
    print("No")