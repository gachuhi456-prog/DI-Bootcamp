print("Hello world\n" * 4)
result = (99 ** 3) * 8
print(result)  # Output: 7762392
5 < 3      # False
3 == 3     # True
3 == "3"   # False (int vs string)
3 > 3   # TypeError (can't compare string and int)
"Hello" == "hello"  # False (case-sensitive)
computer_brand = "Apple"  # or your actual brand
print(f"I have a {computer_brand} computer.")
name = "Alex"
age = 25
shoe_size = 42
info = f"My name is {name}, I'm {age} years old, and I wear size {shoe_size} shoes. Fun fact: I once hiked a mountain in these!"
print(info)
a = 10
b = 5

if a > b:
    print("Hello World")
    number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")
    my_name = "Alex"  # change to your name
user_name = input("What's your name? ")

if user_name.lower() == my_name.lower():
    print("No way! We have the same name! Are you my clone? ")
else:
    print(f"Nice to meet you, {user_name}! At least ONE of us has good taste in names ")
    height = int(input("What is your height in centimeters? "))

if height > 145:
    print("You're tall enough to ride! Enjoy the roller coaster! ")
else:
    print("You need to grow some more to ride. Come back when you've had a growth spurt! ")
