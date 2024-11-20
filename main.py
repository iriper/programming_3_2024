class Cat:
    def __init__(self, colour, breed, age):
        self.colour = colour
        self.breed = breed
        self.age = age

    def sleep(self):
        print('Zzz..')

    def eat(self):
        print('Wi wi wi...')

    def hunt(self):
        print('...')

    def run(self):
        print('Meow-w-w-w')


whiskers = Cat('grey', 'russian blue', 5)
print(whiskers.colour)


class HomeCat(Cat):
    def __init__(self, petname, master, colour, breed, age):
        super().__init__(colour, breed, age)
        self.petname = petname
        self.master = master

    def ask_food(self):
        print('Meow! Meow!')


patches = HomeCat('Patches', 'Alex', 'grey', 'russian blue', 5)
print(patches.petname)
