
class Animals:
    state = 'Животное голодно'
    def __init__(self, name = str, weight = float, voice = str):
        self.name = name
        self.weight = weight
        self.voice = voice

    def voice_enable(self):
        print(f'{self.name} говорит {self.voice}')

    def feeding(self, value = 1):
        self.state = 'Животное накормлено'
        self.weight += value
        print(f'{self.sub_class_name} накормлена(о) и теперь вес составляет {self.weight}')
    pass

class Udders(Animals):
    sub_class_name = 'Парнокопытное'
    udder_state = 'Животное не доено'
    def milk(self):
        self.udder_state = 'Животное надоено'
        print(f'Животное по имени {self.name} надоено')
    pass

class Poultry(Animals):
    sub_class_name = "Птица"
    eggs = 'Яйца снесены, но не собраны'
    def eggs_collection(self, amount=2):
        self.eggs = 'Яйца собраны'
        print(f'У птицы по имени {self.name} были собраны яйца в количестве {amount} штук')

    pass
class Sheep(Animals):
    sub_class_name = 'Овца'
    fur_state = 'Шерсть необходимо состричь'
    def shaving(self):
        self.fur_state = 'Шерсть сострижена'
        print(f'Овца по имени {self.name} была подстрижена')
#------------------------------------------------------------------------------------------------------------------------------
cow = Udders('Манька', 200, 'Му-му')
goat_1 = Udders('Рога', 20, 'Ме-ме')
goat_2 = Udders('Копыта', 25, 'Ме-ме')
chicken_1 = Poultry("Ко-Ко", 2, 'Ко-ко')
chicken_2 = Poultry("Кукареку", 3, 'Ко-ко')
goose_1 = Poultry('Серый', 6, 'Га-га')
goose_2 = Poultry('Белый', 4, 'Га-га')
duck1 = Poultry('Кряква', 3, 'Кря-кря')
sheep1 = Sheep('Барашек', 40, 'Бе-бе')
sheep2 = Sheep('Кудрявый', 38, 'Бе-бе')
animals_weight_list = [cow, goat_1, goat_2, chicken_1, chicken_2, goose_1, goose_2, duck1, sheep1, sheep2]


goat_1.feeding(), goat_1.milk()
goat_2.feeding(), goat_2.milk()
chicken_1.feeding(), chicken_1.eggs_collection()
chicken_2.feeding(), chicken_2.eggs_collection()
goose_1.feeding(), goose_1.eggs_collection()
goose_2.feeding(), goose_2.eggs_collection()
duck1.feeding(), duck1.eggs_collection()
sheep1.feeding(), sheep1.shaving()
sheep2.feeding(), sheep2.shaving()
cow.feeding(10), cow.milk()


def animals_weight(list):
    animals_attributes = {}
    temp_list = []
    for elements in list:
        animals_attributes[elements.name] =  elements.weight
        temp_list.append(elements.weight)

    print(f'Суммарная масса всех животных составляет {sum(temp_list)} кг')
    print(f'Самаое тяжелое животное на ферме - {max(animals_attributes, key=animals_attributes.get)}')

animals_weight(animals_weight_list)
