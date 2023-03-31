def symmetric(a):
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False #если находится неравенство, то сразу же возвращаем фолс
    return True


n = int(input())
b = [list(map(int, input().split())) for i in range(n)]
if symmetric(b):
    print('YES')
else:
    print('NO')


