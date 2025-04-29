class Boy:
    def __init__(self, name, age):
        self.__name = name          
        self.__age = age            

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def action(self):
        print(f"{self.get_name()} is just being a boy!")

class SingingBoy(Boy):
    def __init__(self, name, age, vocal_range):
        super().__init__(name, age)
        self.__vocal_range = vocal_range 

    def get_vocal_range(self):
        return self.__vocal_range

    def action(self):
        print(f"{self.get_name()} is singing a song 🎤 in {self.get_vocal_range()} range")

class DancingBoy(Boy):
    def __init__(self, name, age, dance_style):
        super().__init__(name, age)
        self.__dance_style = dance_style  

    def get_dance_style(self):
        return self.__dance_style

    def action(self):
        print(f"{self.get_name()} is dancing to the {self.get_dance_style()} beat 💃")

def perform_action(boy):
    boy.action()

if __name__ == "__main__":
    boy1 = Boy("John", 15)
    boy2 = SingingBoy("Mike", 16, "tenor")
    boy3 = DancingBoy("Alex", 17, "hip-hop")

    for b in (boy1, boy2, boy3):
        perform_action(b)
