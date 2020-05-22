import random
# hiiii
nickname = ["The bulldog", "Cool guy", "Coder", "Sleepyhead", "Hungry"]

print("Please enter your name")
firstname = input("Enter first name:")
lastname = input("Enter last name:")

#choose options
print("Choose options")
print("1: Display all possible nicknames")
print("2: Display a random nickname")

choice = input("Enter choice: 1/2:")

if choice == '1':
    for i in range( len(nickname)):
        print(firstname + " " + nickname[i] + " " + lastname)
elif choice == '2':
    randomnickname = random.choice(nickname)
    print(firstname + " " +randomnickname + " " + lastname)
elif choice == '3'
    

elif choice == '4 '