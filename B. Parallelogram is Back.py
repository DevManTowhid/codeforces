
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

result = []


dx1 = b[0] + c[0] - a[0]
dy1 = b[1] + c[1] - a[1]
result.append((dx1, dy1))

dx2 = a[0] + c[0] - b[0]
dy2 = a[1] + c[1] - b[1]
result.append((dx2, dy2))

dx3 = a[0] + b[0] - c[0]
dy3 = a[1] + b[1] - c[1]
result.append((dx3, dy3))

print(3)

for p in result:
    print(p[0], p[1])