n = int(input())
v = [int(x) for x in input().split()]


def solution1():
    # Agar yoqolgan sonni x desak, v ni barchasi va x lar yigindisi 1..n bo'lgan sonlar yig;indisiga teng
    print(n * (n+1) // 2 - sum(v))


def solution2():
    has = [False for _ in range(n+1)]
    for x in v:
        has[x] = True
    for i in range(1, n+1):
        if not has[i]:
            print(i)
            break


solution1()
