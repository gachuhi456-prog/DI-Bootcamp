import random

# ============================================
# 🌟 Exercise 1: Pets
# ============================================
print("=" * 50)
print("Exercise 1: Pets")
print("=" * 50)

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1: Create the Siamese class
class Siamese(Cat):
    pass

# Step 2: Create a list of cat instances
bengal_obj = Bengal("Leo", 3)
chartreux_obj = Chartreux("Milo", 5)
siamese_obj = Siamese("Luna", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
print("Taking cats for a walk:")
sara_pets.walk()


# ============================================
# 🌟 Exercise 2: Dogs
# ============================================
print("\n" + "=" * 50)
print("Exercise 2: Dogs")
print("=" * 50)

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        
        if my_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif other_power > my_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"

# Step 2: Create dog instances
dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Max", 7, 35)

# Step 3: Test dog methods
print(dog1.bark())
print(f"{dog2.name}'s run speed: {dog2.run_speed():.2f}")
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))


# ============================================
# 🌟 Exercise 3: Dogs Domesticated
# ============================================
print("\n" + "=" * 50)
print("Exercise 3: Dogs Domesticated")
print("=" * 50)

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
        dog_names = [self.name]
        for dog in args:
            if isinstance(dog, Dog):
                dog_names.append(dog.name)
        names_str = ", ".join(dog_names)
        print(f"{names_str} all play together")
    
    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", 
                     "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
buddy = PetDog("Buddy", 3, 15)
max_dog = PetDog("Max", 4, 20)

print("\nTraining Fido:")
my_dog.train()

print("\nPlaying together:")
my_dog.play(buddy, max_dog)

print("\nDoing tricks:")
my_dog.do_a_trick()
buddy.do_a_trick()  # Not trained yet

print("\nTraining Buddy and trying again:")
buddy.train()
buddy.do_a_trick()


# ============================================
# 🌟 Exercise 4: Family and Person Classes
# ============================================
print("\n" + "=" * 50)
print("Exercise 4: Family and Person Classes")
print("=" * 50)

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""
    
    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
    
    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
        print(f"Welcome to the family, {first_name} {self.last_name}!")
    
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents accept that you will go out with your friends")
                else:
                    print(f"Sorry, you are not allowed to go out with your friends.")
                return
        print(f"{first_name} is not in this family.")
    
    def family_presentation(self):
        print(f"\nThe {self.last_name} Family:")
        print("-" * 30)
        for member in self.members:
            print(f"  {member.first_name} {member.last_name}, {member.age} years old")

# Test the classes
smith_family = Family("Smith")

# Add members
smith_family.born("John", 45)
smith_family.born("Jane", 42)
smith_family.born("Tommy", 15)
smith_family.born("Alice", 20)

# Display family
smith_family.family_presentation()

# Check majority
print("\nChecking majority:")
smith_family.check_majority("Tommy")
smith_family.check_majority("Alice")
smith_family.check_majority("Unknown")


print("\n" + "=" * 50)
print("All inheritance exercises completed!")
print("=" * 50)