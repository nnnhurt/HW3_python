a = list(map(int, input().split()))
b = a[len(a)-1] #
for i in range(len(a)-1, -1, -1):
    a[i] = a[i-1] #сдвигаем вправо
a[0] = b #присваеваем
print(*a)
