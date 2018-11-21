with open('CookBook.txt', 'w') as cook_file:
    cook_file.write('''Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт''')


def read_file():
    with open('CookBook.txt') as cook_file:
        cook_book = {}
        for line in cook_file:
            ingridient_list = []
            dish_name = line.strip()
            counter_ingridients = int(cook_file.readline().strip())
            for i in range(counter_ingridients):
                ingridient = cook_file.readline().strip()
                ingridient_dict = {'ingridient_name': ingridient.split(' | ')[0],
                                   'quantity': ingridient.split(' | ')[1],
                                   'measure': ingridient.split(' | ')[-1]}
                ingridient_list.append(ingridient_dict)
            cook_file.readline()
            cook_book[dish_name] = ingridient_list

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_file()
    dish_dict = {}
    for dish, ingridient in cook_book.items():
        for order_dish in dishes:
            if dish == order_dish:
                for ingridient_for_order in ingridient:
                    if ingridient_for_order['ingridient_name'] in dish_dict.keys():
                        print(ingridient_for_order['quantity'])
                        ingridient_for_order['quantity'] = int(ingridient_for_order['quantity']) * person_count
                        print(ingridient_for_order['quantity'])
                        dish_dict[ingridient_for_order['ingridient_name']] = str(int(dish_dict[ingridient_for_order['ingridient_name']]['quantity']) + ingridient_for_order['quantity'])
                    else:
                        ingridient_for_order['quantity'] = str(int(ingridient_for_order['quantity']) * person_count)
                        dish_dict[ingridient_for_order['ingridient_name']] = {'measure':ingridient_for_order['measure'],
                                                                              'quantity' : ingridient_for_order['quantity']}

    return(dish_dict)


print(read_file())
print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))


