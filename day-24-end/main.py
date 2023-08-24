import os

# Check if 'my_file.txt' exists. If so, read and print its content.
if os.path.exists("my_file.txt"):
    with open("my_file.txt") as file:
        contents = file.read()
        print(contents)
else:
    print("my_file.txt does not exist.")

# Append text to 'my_file.txt' without overwriting its existing content.
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# Create (or overwrite) 'file_that_doesnt_exist.txt' with the content "New text."
with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.")
