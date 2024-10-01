realhour, realminute = map(int,input().split())
cooktime = int(input())

cookhour = cooktime//60
cookminute = cooktime%60

totalhour = realhour + cookhour
totalminute = realminute + cookminute

if totalminute >= 60:
    totalminute %= 60
    totalhour += 1

if totalhour >= 24:
    totalhour %= 24

print(totalhour, totalminute)