s = input()
l = len(s)
if "f" in s:
    i = s.index("f")
    s = s[i + 1:][::-1] #если найдена буква ф то оставшаяся сторона строки режется и переворачивается
#проверыяем есть ли в слове f, если да, то делаем срез
    if "f" in s:
        print(i, l - s.index("f") - 1) #после опять пробегаемся и ищем ф если она есть
    else:
        print(i)
#проверяем вновь есть ли, тогда выводим, если нет, то ничего не выводим



