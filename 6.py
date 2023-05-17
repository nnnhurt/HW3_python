def symmetric(a, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False ##если находится неравенство в противополож оси, то сразу же возвращаем фолс
    return True


n = int(input())
b = [list(map(int, input().split())) for i in range(n)] #ввод матрицы
if symmetric(b,n): #если функция вернула истину то все ок
    print('YES')
else:
    print('NO')

