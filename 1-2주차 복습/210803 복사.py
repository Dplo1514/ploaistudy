#정수형 (int)는 불변타입이기 때문에 x값을 변경했을 때에도 y에 할당된 x값은 그대로
x = 5
y = x
x = 29
print(x)
print(y)
#리스트형 데이터타입은 가변이기 때문에 a값을 변경하면 b값도 자동 변경됨
a = [2,4,6]
b = a
print(a)
print(b)

a[0] = 99
print(a)
print(b)