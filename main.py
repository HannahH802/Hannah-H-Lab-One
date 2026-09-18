name = input("What is your name: ")
print(name)
age = int(input("What is your age: "))
print(age)
color = input("What is your favorite color:")
print(color)
print("Hello", name , "you are", age ," years old and your favorite color is ", color)

if age < 13:
	print("You are a kid - enjoy being young!")
elif age < 20:
	print("You are a teenager - exciting years ahead!")
elif age < 65:
	print("You are an adult - keep pursuing your goals!")
else:
	print("You are a senior - enjoy sharing your wisdom!")