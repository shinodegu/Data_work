from time import sleep

class auto (object):

    def __init__(self, brand, mark, age, color = "black", weight = 1330):
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
       self.age += 1
       print(self.age)


class truck (auto):
    def __init__(self, brand, mark, age, max_loud):
        super().__init__(brand, mark, age)
        self.max_loud = max_loud

    def move(self):
        print("Attention move")

    def load(self):
        delay = 1
        sleep(delay)
        print('load')
        sleep(delay)




class car (auto):
    def __init__(self, brand, mark, age, max_speed):
        super().__init__(brand, mark, age)
        self.max_speed = max_speed

    def move(self):
        print('move', "max_speed is", self.max_speed)

c = truck('man', 'aboba', 20, 500)

c.move()
print(c.max_loud)
print(c.brand)
print(c.mark)
print(c.age)
c.load()
c.birthday()
c.birthday()


b = car("toyota", "supra", 25, 300)
b.move()
print(b.brand)
print(b.mark)
print(b.age)
print(b.max_speed)
b.birthday()
b.birthday()