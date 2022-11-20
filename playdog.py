import Dog
import inheritance
import extendfun


buddy = Dog.Dog("Buddy", 9)
print(buddy.age)
print(buddy.species)

print(buddy.speak("woof"))

miles = inheritance.JackRusselTerrier("Miles", 6)
print(miles.speak("woof woof"))


jack = inheritance.Bulldog("Jack", 8)
print(jack.speak("Bow wow"))


lob = extendfun.BullDog("Lob",4)
print(lob.speak())
