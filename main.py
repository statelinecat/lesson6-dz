class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  # Здесь будет реализация

    def eat(self):
        print(f"{self.name} ест.")


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} чирикает.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} мяукает.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит.")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Питомец {animal.name} принят в зоопарк')

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f'В зоопарке теперь есть {staff_member.name}')


class ZooKeeper(Zoo):
    def __init__(self):
        self.name = "зоокипер"
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Zoo):
    def __init__(self):
        self.name = "ветеринар"

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

class Сleaner(Zoo):
    def __init__(self):
        self.name = "уборщик"

    def clean_animal(self, animal):
        print(f"{self.name} чистит {animal.name}.")


import pickle

def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)

def load_zoo(filename):
    try:
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
    except FileNotFoundError:
        zoo = Zoo()
    return zoo



zoo_name = input("Введите название зоопарка: ")


zoo = load_zoo(zoo_name)

print("Список сотрудников зоопарка:")
if len(zoo.staff) < 1:
    print('Сотрудников пока нет, сейчас наберем;)')
else:
    for staff in zoo.staff:
        print(staff.name)

print("Список питомцев зоопарка:")
if len(zoo.animals) < 1:
    print('Питомцев пока нет, сейчас будем заселять;)')
else:
    for animal in zoo.animals:
        print(animal.name)

if len(zoo.animals) < 1:
    birds = [Bird("Птица", 1), Bird("Кукушка", 2)]
    mammals = [Mammal("Хищник", 3), Mammal("Собака", 4)]
    reptiles = [Reptile("Змея", 5)]
    animal_sound(birds + mammals + reptiles)
    animals = birds + mammals + reptiles
    for animal in animals:
        zoo.add_animal(animal)

if len(zoo.staff) < 1:
    staffs = [ZooKeeper(), Veterinarian(), Сleaner()]
    for staff in staffs:
        zoo.add_staff(staff)

save_zoo(zoo, zoo_name)
