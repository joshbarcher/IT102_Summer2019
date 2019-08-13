class Dog:
    # fields
    breed = ""
    name = ""
    nickname = ""
    age = 0

    # constructor (a function used to create an object)
    def __init__(self, breed, name, nickname, age):
        self.breed = breed
        self.name = name
        self.nickname = nickname
        self.age = age

    # methods (aka functions)
    def makeNoise(self):
        print("Bark, bark!")

    def callToYourself(self):
        print("Come over here,", self.name)

# instantiate the class
sam = Dog("Great Dane", "Sam", "Samson", 10)
sam.nickname = "Samson the Mighty"

# sam.breed = "Great Dane"
# sam.name = "Sam"
# sam.nickname = "Samson"
# sam.age = 10

sam.makeNoise()
sam.callToYourself()

# chewy = Dog()
# chewy.name = "Chewy"