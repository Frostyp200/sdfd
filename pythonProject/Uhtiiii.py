import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.notbored = True

    def to_eat(self):
        print("Eating time")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("Sleeping time")
        self.progress += 2

    def to_play(self):
        print("Time to play")
        self.progress += 0.1
        self.gladness -= 5

    def to_notbored(self):
        if self.progress < -0.5:
         print("A bit bored")
         self.alive = False
        elif self.gladness <= 0:
            print("Bored...")
            self.alive = False
        elif self.progress > 5:
            print("Happy")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.gladness, 2)}")

    def notbored(self, day):
        day = "Day " + str(day) + " of " + self.name+ " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)

        if live_cube == 1:
            self.to.eat()
        if live_cube == 2:
            self.to.sleep()
        if live_cube == 3:
            self.to.play()

        self.end_of_day()
        self.is_notbored()
    orel = Cat(name="Cat")

    for day in range(1, 366):
        if orel.alive == False:
            break

        orel.live(day)

