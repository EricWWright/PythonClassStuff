class Human(object):
    
    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender 
        self.race = race
    def introduce_self(self):
        print("Hello my name is", self.name)
    def discribe_self(self):
        print("I have", self.hair_color, "hair")
        print("I have", self.eye_color, "eyes")
        print("I am", self.height, " in tall")
        print("I weigh", self.weight, "lbs")
        print("I am a", self.race, self.gender, "with an IQ of", self.iq)
    def bmi(self):
        """Calculates bmi for Human""" 
        kg = self.weight * 0.45
        m = self.height * 0.025
        m2 = m * m
        objBmi = kg / m2
        print("My bmi is",objBmi)
        if objBmi <= 18.5:
            print("I am severely underweight")
        elif objBmi >= 18.5 and objBmi <= 25:
            print("Im a healthy weight")
        elif objBmi >=25:
            print("I'm overweight")


eric = Human("Eric", "Black", "Brown", 68,
             195, 300, "Male", "White")
eric.introduce_self()
eric.discribe_self()
eric.bmi()

bob = Human("Bob", "Blonde", "Blue", 76,
             200, 94, "Male", "White")
bob.introduce_self()
bob.discribe_self()
bob.bmi()

green_giant = Human("Green", "Green", "Green", 7200,
                     2000000, None, "Male", "Green Giant")
green_giant.introduce_self()
green_giant.discribe_self()
green_giant.bmi()