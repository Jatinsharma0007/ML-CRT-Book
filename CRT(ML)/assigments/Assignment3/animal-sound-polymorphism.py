class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo! Moo!"

def play_sound(animal):
    return animal.make_sound()

def main():
    dog = Dog()
    cat = Cat()
    cow = Cow()
    
    animals = [dog, cat, cow]
    
    print("Animal Sounds:")
    for animal in animals:
        print(f"{animal.__class__.__name__} says: {play_sound(animal)}")

if __name__ == "__main__":
    main()
