a = [int(b) for b in input().split()]
c = 0
for k in range(len(a)): # прохржу по длине 
    for j in range(k + 1, len(a)): #и проверяю с каждым равны ли они друг другу
        if a[k] == a[j]:
            c += 1
print(c)

# просто проходимся по списку, проверяем сколько одинаковых чисел есть в списке, куда вписали любые числа.
# если одинаковое число встречается, то к счетчику присваиваем и прибавляем 1.

