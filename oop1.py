class auto(object):
    brand = "Koenigsegg"
    mark = "Agera"
    age = 13
    color = "black"
    weight = 1330

    def __init__(self, brand = "Koenigsegg", mark = "Agera", age = 13):
        self.brand = brand
        self.mark = mark
        self.age = age

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
       self.age += 1
       print(self.age)


mashina = auto()
mashina.move()
mashina.stop()
mashina.birthday()
mashina.birthday()
