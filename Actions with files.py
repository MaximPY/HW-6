

def book_creation():
    cook_book = {}
    with open('Recipe.txt', 'r', encoding='UTF-8') as file:
         for lines in file:
            lines = lines.strip()
            cook_book[lines] = []
            counter = int(file.readline().strip())
            for i in range(counter):
                ing = file.readline().strip().split('|')
                temp_dict = {'ingridient_name': ing[0], 'quantity': ing[1], 'measure': ing[2]}
                cook_book[lines].append(temp_dict)
            file.readline()
    return cook_book
print(book_creation())

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = book_creation()
    shop_dict = {}
    if type(dishes) != list:
        temp_list = []
        temp_list.append(dishes)
    else:
        temp_list = dishes
    for i in temp_list:
        if i in cook_book.keys():
            for dictionaries in cook_book[i]:
                number = int(dictionaries['quantity']) * person_count
                shop_dict[dictionaries['ingridient_name']] = {'measure': dictionaries['measure'], 'quantity': number}

    print(shop_dict)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)

