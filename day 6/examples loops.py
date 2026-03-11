'''#installing a bullet while then inside until zero when bullet is zero then we will stop the loop and print the message that bullet is empty and game over the max bullet count is 10
bullet = 10
while bullet > 0:
    print(f"Bullet count: {bullet}")
    shoot = input("Do you want to shoot? (yes/no): ")
    if shoot.lower() == "yes":
        bullet -= 1
        print("Bang!")
    elif shoot.lower() == "no":
        print("You chose not to shoot.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
print("Bullet is empty. Game over!")


#candycrush game so when moves are done and then the game will be over i need tho slect which side to move where i can select up down left right and then the moves will be reduced by one and when moves are zero then the game will be over
moves = 5
while moves > 0:'
    print(f"Moves left: {moves}")
    move = input("Enter your move (up/down/left/right): ")
    if move.lower() in ["up", "down", "left", "right"]:
        moves -= 1
        print(f"You moved {move}.")
    else:
        print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")
print("No moves left. Game over!")

#using an for loop taking student attendance like in need for an dictionary to store the data of student name age class and attendance and then print the attendance of the student
students = {
    "Manoj": {"age": 20, "class": "10th", "attendance": []},
    "Bob": {"age": 21, "class": "11th", "attendance": []},
    "Bhuvan": {"age": 22, "class": "12th", "attendance": []}
}   
for student in students:
    name = student
    age = students[student]["age"]
    class_ = students[student]["class"]
    attendance = students[student]["attendance"]
    print(f"Name: {name}, Age: {age}, Class: {class_}")
    present = input("Is the student present? (yes/no): ")
    if present.lower() == "yes":
        attendance.append("Present")
    elif present.lower() == "no":
        attendance.append("Absent")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
print("\nAttendance Summary:")
for student in students:
    name = student
    attendance = students[student]["attendance"]
    print(f"{name}: {', '.join(attendance)}")

#declaring a list of names and then using a for loop to print the names in the list without using the index of the list and then print the names in the list with the index of the list
names = ["Manoj", "Bob", "Bhuvan"]
print("Names without index:")
for name in names:
    print(name)
print("\nNames with index:")
for index, name in enumerate(names):
    print(f"{index}: {name}")
'''
