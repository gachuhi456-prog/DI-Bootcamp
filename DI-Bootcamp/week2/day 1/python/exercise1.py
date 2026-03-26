#1
print("Hello world\nHello world\nHello world\nHello world")

#2
print((99**3) * 8)

#3
print(15 < 8)        # False
print(5 < 3)         # False
print(3 == 3)        # True
print(3 == "3")      # False
print("3" > 3)       # Error (can't compare str and int)
print("Hello" == "hello")  # False

#4
computer_brand = "HP"  # change to your brand
print(f"I have a {computer_brand} computer.")

#5
name = "Alex"       # change to your name
age = 20            # your age
shoe_size = 42      # your shoe size

info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

#6
a = 10
b = 5

if a > b:
    print("Hello World")

#7
 number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#8
my_name = "Alex"  # change to your name
user_name = input("What is your name? ")

if user_name == my_name:
    print("Whoa! We have the same name 😄")
else:
    print("Nice to meet you, but that's not my name 😄")

 #9 height = int(input("Enter your height in cm: "))

if height > 145:
    print("You are tall enough to ride 🎢")
else:
    print("You need to grow some more to ride 🎢")  
