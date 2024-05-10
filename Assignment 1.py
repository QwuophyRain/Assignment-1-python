# 1. Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"

# 2. Store a message in a variable, and then print that message
message1 = "Hello, this is a stored message."
print(message1)

# 3. Store a message in a variable and print that message. Then change the value of your variable to a new message, and print the new message
message2 = "This is the original message."
print(message2)
message2 = "This is the new message."
print(message2)

# 4. Store a person’s name in a variable and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
person_name = "Eric"
print(f"Hello {person_name}, would you like to learn some Python today?")

# 5. Store a person’s name in a variable, then print that person’s name in lowercase, uppercase, and title case.
person_name = "John Doe"
print("Lowercase:", person_name.lower())
print("Uppercase:", person_name.upper())
print("Title case:", person_name.title())

# 6. Store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.
famous_person = "Albert Einstein"
message = f"{famous_person} once said, 'Imagination is more important than knowledge.'"
print(message)

# 7. Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.
favorite_number = 7
print(f"My favorite number is {favorite_number}.")

# 8. Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
age = 30
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an Elder.")
