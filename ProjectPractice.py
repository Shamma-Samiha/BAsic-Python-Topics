# MADLIB GAME
"""
username = input("What is your name?")
boyfie = input("What is your boyfriends name?")
job = input("what is your occupation?")
country = input("Which country do you want to visit this year?")

print(f"Will the day ever come, when the world will go silent and {username} will get her beloved {boyfie}, "
      f"and live hapily everafter in {country}, doing simple job like {job}.")
"""

# NUMBER GUSSEING GAME
"""
import random
RandomNumber = random.randrange(1,5)
userinput = int(input("Guess the number:"))
if userinput > RandomNumber:
    print(RandomNumber)
    print("The number you guessed is too high.")
elif userinput < RandomNumber:
    print(RandomNumber)
    print("The number you guessed is too low.")
else:
    print(RandomNumber)
    print("!!!!CORRECT!!!!")
"""
# TEXT-BASED ADVENTURE GAME

"""
answer = input("Do you want to play this adventure game? [yes/no]")
if answer == "yes":
     print("!!!!Welcome to the game!!!!")
     answer = input("Where do you want to go?[hill/sea]")
     if answer == "hill":
          print("There is a cottage at the top of this mountain.")
          answer = input("Do you want to go to the cottage?[yes/no]")
          if answer == "yes":
              print("The cottage is warm. You are SAVED!!")
          elif answer == "no":
              print("You die of COLD!!")
          else:
              print("Wrong Answer!!")
     elif answer == "sea":
        print("There is a shark. It eats you. You DIE!!")
     else:
         print("The answer is wrong.")
else:
    print("At least play the game once!!")
"""

# Dice Rolling Simulator Game
"""
import random
DiceRolling = True
while DiceRolling:
    print(random.randint(1,6))
    PlayAgain = input("Do you want to play again? [yes/no]")
    if PlayAgain == "yes" or PlayAgain == "Yes" or PlayAgain == "YES":
        continue;
    else:
        print("Game Over!")
        break
"""

# Hangman Game

"""
word = "Coffee"
GuessAdd = []
chance = 3
done = 0

# User guess logic
while not done and chance > 0:
    # Display the current state of the word
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()  # Move to the next line

    # User input validation
    MyGuess = input(f"Enter your guess. You have {chance} chances: ").strip().lower()
    if len(MyGuess) != 1 or not MyGuess.isalpha():
        print("Please enter a single valid letter.")
        continue

    # Add the guess to the list if not already present
    if MyGuess not in GuessAdd:
        GuessAdd.append(MyGuess)

    # Reduce chances if the guess is incorrect
    if MyGuess not in word.lower():
        chance -= 1
        print(f"Wrong guess! Chances left: {chance}")

    # Check if the word is fully guessed
    done = 1
    for letter in word:
        if letter.lower() not in GuessAdd:
            done = 0
            break

# Final Result
if done:
    print(f"You won! The word is '{word}'.")
else:
    print(f"You lost! The word was '{word}'.")
"""

# Merge PDf
"""
from PyPDF2 import PdfMerger

Allpdf  = ["2. Supervised, Unsupervised Learning.pdf", "1. Introduction.pdf"]
OurMerger = PdfMerger()

for Newpdf in Allpdf:
    OurMerger.append(Newpdf)

OurMerger.write("Latest.pdf")
OurMerger.close()
"""
# Desktop Notifier
"""
from win10toast import ToastNotifier
Toast = ToastNotifier()

Toast.show_toast("DO PYTHON","Time to do python project", duration=10)
"""

# Contact Book App
"""
ContactBook = {}

# Method to display phonebook
def Show():
    print(ContactBook.items())
    print("Name:\t\tContact:")

    for key in ContactBook:
        print("{}\t{}".format(key,ContactBook.get(key)))

while True:
    choice = int(input("1. Add new contact.\n"
                   "2. Search Contact\n"
                   "3. Display Contact\n"
                   "4. Edit Contact.\n"
                   "5. Delete Contact.\n"
                   "6. Exit.\n"
                   "Please choose a number between [1-6]"))

    if choice == 1:
        name = input("Add contact name: ")
        phone = input("Add number: ")

        print("Contact added successfully.")
        ContactBook[name] = phone

    elif choice == 2:
        searchcontact = input("Search the Contact: ")

        if searchcontact in ContactBook:
            print(searchcontact,"Contact Number is: " , ContactBook[searchcontact])
        else:
            print("Number Not Found.")


    elif choice == 3:
        if not ContactBook:
            print("Contact book is empty")

        else:
            Show()

    elif choice == 4:
        edit_contact = input("Edit the contact:")
        if edit_contact in ContactBook:
            newnumber = input("Write new number: ")
            ContactBook[edit_contact]= newnumber
            print("Contact Updated Successfully.")
            Show()
        else:
            print("Contact not found")

    elif choice == 5:
        delcontact = input("Which contact do you want to delete: ")

        if delcontact in ContactBook:
            confirmdel = input("Do you want to delete this contact?[y/n]")

            if confirmdel == "y" or confirmdel == "Y":
                ContactBook.pop(delcontact)
                Show()

            else:
                print("Contact not Found.")
    else:
        break
"""
"""
import random
# Loop to repeatedly ask
while True:
    userinput = input("Do you wanna Roll the dice? (y/n): ")
    if userinput == 'y':
        print(random.randint(1, 6))
    else:
        print("Goodbye")
        break
"""
Contact = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    Contact[name] = number
    print("Contact added successfully.")

def search_contact():
    name = input("Enter name: ")
    if name in Contact:
        print("Number: ", Contact[name])
    else:
        print("Contact not found")

def delete_contact():
    name = input("Enter name: ")
    if name in Contact:
        del Contact[name]
        print("Contact deleted")
    else:
        print("Contact not found")

def display_contacts():
    if Contact:
        print("All contacts:")
        for key, value in Contact.items():
            print(key, ":", value)
    else:
        print("No contacts found")

while True:
    choice = int(input("Enter 1 to add contact \n"
                       "Enter 2 to search contact \n"
                       "Enter 3 to delete contact \n"
                       "Enter 4 to display all contacts \n"
                       "Enter 5 to exit \n"))
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        display_contacts()
    elif choice == 5:
        break
    else:
        print("Invalid choice, please try again.")






