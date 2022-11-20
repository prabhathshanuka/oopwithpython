import Dog

class BullDog(Dog.Dog):
    def speak(self, sound="grrrrrr"):
        return f"{self.name} says {sound}"