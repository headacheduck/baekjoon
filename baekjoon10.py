a = int(input())
b = input()

list_b = list(b)
j = len(list_b)

for i in range (len(list_b)):
    print(a*int(list_b[j-1]))
    j -= 1

print(a*int(b))