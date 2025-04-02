'''В высотном доме 5 подъездов по 20 квартир каждый. На каждом этаже 4 квартиры. Нумерация квартир идёт подряд, снизу
вверх: на первом этаже первого подъезда 1, 2, 3, 4. На втором этаже первого подъезда находятся квартиры 5, 6, 7, 8
и т. д. Напишите скрипт, который получает номер квартиры и выводит на экран номер подъезда и этажа'''

import math

apart_number = input("What's the apartment number? ")
int(apart_number)
number_ent = math.ceil(int(apart_number) / 20)
print(math.ceil(int(number_ent)), "entrance", "\n")
if number_ent == 1: print(math.ceil(int(apart_number) / 4), "floor")
else:
    print(math.ceil((int(apart_number) - 20 * (math.ceil(int(number_ent)) - 1)) / 4), "floor")












