class auto(object):
   
    def __init__(self, brand, mark, age, color = 'black', weight = 1330):
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


mashina = auto("Niva", "4x4", 39)
mashina.move()
mashina.stop()
mashina.birthday()
print(mashina.mark)
print(mashina.age)
print(mashina.brand)
