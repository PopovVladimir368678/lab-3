


stuffdict = {"в": (3, 25),
              "п": (2, 15),
              "б": (2, 15),
              "а": (2, 20),
              "н": (1, 15),
              "т": (3, 20),
              "о": (1, 25),
              "ф": (1, 15),
              "д": (1, 10),
              "к": (2, 20),
              "р": (2, 20)   # ингалятора тут нет, я его уже взял и метта уже не 9,а 8
              }
def get_area_and_value(stuffdict):
    area = [stuffdict[item][0] for item in stuffdict] # создаю список размеров
    value = [stuffdict[item][1] for item in stuffdict] # создаю список ценности
    return area, value    # Разделяем списки значений исходного словаря


def get_memtable(stuffdict, A=8):
    area, value = get_area_and_value(stuffdict)
    n = len(value)  # находим размеры таблицы

    # создаём таблицу из нулевых значений
    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            # базовый случай
            if i == 0 or a == 0:
                V[i][a] = 0

            # если площадь предмета меньше площади столбца,
            # максимизируем значение суммарной ценности
            elif area[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a - area[i - 1]], V[i - 1][a])

            # если площадь предмета больше площади столбца,
            # забираем значение ячейки из предыдущей строки
            else:
                V[i][a] = V[i - 1][a]
    return V, area, value



def get_selected_items_list(stuffdict, A=8):
    V, area, value = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]  # начинаем с последнего элемента таблицы
    a = A  # начальная площадь - максимальная
    items_list = []  # список площадей и ценностей

    for i in range(n, 0, -1):  # идём в обратном порядке
        if (res <= 0):  # условие прерывания - собрали "рюкзак"
            break
        if res == V[i - 1][a]:  # ничего не делаем, двигаемся дальше
            continue
        else:
            # "забираем" предмет
            items_list.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]  # отнимаем значение ценности от общей
            a -= area[i - 1]  # отнимаем площадь от общей

    selected_stuff = ["и"]

    # находим ключи исходного словаря - названия предметов
    for search in items_list:
        for key, value in stuffdict.items():
            if value == search:
                selected_stuff.append(key)
                stuffdict[key] = (10,value[1])  # заставляю программу не повторять вещи
                break        #и не брать за 1 цикл по search два идентичных элимента.

    return selected_stuff

symma_v = 5 # это инголятор

selected_stuff = get_selected_items_list(stuffdict, A=8)

for i in selected_stuff:
    if i != "и":
        a = stuffdict[i][1]
        symma_v += a

stuffdict = {"в": (3, 25),
              "п": (2, 15),
              "б": (2, 15),
              "а": (2, 20),
              "н": (1, 15),
              "т": (3, 20),
              "о": (1, 25),
              "ф": (1, 15),
              "д": (1, 10),
              "к": (2, 20),
              "р": (2, 20)
             }  # записываю заного так как менял в процессе
y = 0
print('Ответ:')

for i in selected_stuff:
    if i == 'и':
        print(i + ' ', end='')
        y += 1
        continue
    if stuffdict[i][0] == 1:
        print(i + ' ', end='')
        y += 1
        if y % 3 == 0:
            print()
    elif stuffdict[i][0] == 2:
        print(i + ' ', end='')
        y += 1
        if y % 3 == 0:
            print()
        print(i + ' ', end='')
        y += 1
        if y % 3 == 0:
            print()
    else:
        print(i + ' ', end='')
        y += 1
        if y % 3 == 0:
            print()
        print(i + ' ', end='')
        y += 1
        if y % 3 == 0:
            print()
        print(i + ' ', end='')
        y += 1
        if y % 3 == 0:
            print()
print()   # вывожу в форме рюкзака




symma = 25 + 15 + 15 + 20 + 15 + 20 + 25 + 15 + 10 + 20 + 20
bazobaia = 15
obchaia = bazobaia + 2 * symma_v - symma    # считаю общую сумму балов выживания.
print('Итоговые очки выживания:')
print(obchaia)