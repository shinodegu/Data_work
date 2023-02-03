class auto(object):
    brand = print("Koenigsegg")
    mark = print("Agera")
    age = 13
    print(age)
    color = "black"
    weight = 1330

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
mashina.birthday()
