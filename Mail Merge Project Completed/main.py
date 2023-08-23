import os

# Get the absolute path to the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the placeholder
PLACEHOLDER = "[name]"

# Read names
with open(os.path.join(BASE_DIR, "Input/Names/invited_names.txt")) as names_file:
    names = names_file.readlines()

# Create personalized letters
with open(os.path.join(BASE_DIR, "Input/Letters/starting_letter.txt")) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(os.path.join(BASE_DIR, f"Output/ReadyToSend/letter_for_{stripped_name}.txt"), mode="w") as completed_letter:
            completed_letter.write(new_letter)
