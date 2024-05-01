class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

dog1=Dog("Dino","Poodle")

print(isinstance(dog1,Dog))