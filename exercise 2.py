try:
    message = input("Enter a short note/message: ")
    with open("notes.txt", "w") as file:
        file.write(message)

    with open("notes.txt", "r") as file:
        print("\nFile content:")
        print(file.read())

    new_note = input("\nEnter another note/message: ")
    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)

    with open("notes.txt", "r") as file:
        print("\nUpdated file content:")
        print(file.read())

except FileNotFoundError:
    print("Error: File not found.")