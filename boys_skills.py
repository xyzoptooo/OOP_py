class Boy:
    def __init__(self, name, skill, nickname):
        self.name = name
        self.skill = skill
        self.nickname = nickname

    def introduce(self):
        return f"I am {self.nickname}, also known as {self.name}."

    def perform_skill(self):
        return f"{self.nickname} shows off {self.skill}!"

class SingingBoy(Boy):
    def __init__(self, name, skill, nickname, vocal_range):
        super().__init__(name, skill, nickname)
        self.vocal_range = vocal_range

    def perform_skill(self):
        # Polymorphism: override perform_skill method
        return f"{self.nickname} sings in {self.vocal_range} range with skill {self.skill}!"

if __name__ == "__main__":
    boy1 = Boy("John", "guitar playing", "Johnny")
    print(boy1.introduce())
    print(boy1.perform_skill())

    boy2 = SingingBoy("Mike", "singing", "Mikey", "tenor")
    print(boy2.introduce())
    print(boy2.perform_skill())
