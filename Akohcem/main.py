import random

class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.stress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.stress += 5

    def to_sleep(self):
        print("I will rest")
        self.progress += 3
        self.stress -= 1

    def to_chill(self):
        print("Chill")
        self.progress += 0.1
        self.gladness -= 5
        self.stress -= 2

    def to_eat(self):
        print("Eat")
        self.progress += 0.1
        self.gladness += 2
        self.stress -= 3


    def to_alive(self):
        if self.progress < -0.5:
         print("Cast out...")
         self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.progress >= 20:
            print("Shesofrenia...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.gladness, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name+ " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)

        if live_cube == 1:
            self.to.study()
        if live_cube == 2:
            self.to.sleep()
        if live_cube == 3:
            self.to.chill()
        if live_cube == 4:
            self.to.eat()


        self.end_of_day()
        self.is_alive()
    nick = Student(name="Nick")

    for day in range(1, 366):
        if nick.alive == False:
            break

        nick.live(day)

