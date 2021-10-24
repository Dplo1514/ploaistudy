a = [1,3,5,2,6,-1,8,2,1,4,2,5]
x = 0
sum = 0
while x < len(a):
    if a[x] <0:
        break
    sum = sum +a[x]
    x = x + 1
else:
    print("리스트 전체의 합")

print(sum)