

def solve():
    x, y = map(int, input().split())
    if x > y:
        if x % 2 == 0:
            print(x**2 - y + 1)
        else:
            print((x - 1)**2 + y)
    else:
        if y % 2 == 0:
            print((y - 1)**2 + x)
        else:
            print(y**2 - x + 1)


for t in range(int(input())):
    solve()
