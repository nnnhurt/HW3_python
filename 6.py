def symmetric(a, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False ##если находится неравенство в противополож оси, то сразу же возвращаем фолс
    return True


n = int(input())
b = [list(map(int, input().split())) for i in range(n)]
if symmetric(b,n):
    print('YES')
else:
    print('NO')

