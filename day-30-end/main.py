def read_file():
    try:
        with open("a_file.txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        with open("a_file.txt", "w") as file:
            file.write("Something")
            return "Something"


def fetch_dictionary_key(a_dictionary, key):
    try:
        return a_dictionary[key]
    except KeyError as error_message:
        print(f"The key {error_message} does not exist.")
        return None


def calculate_bmi(height, weight):
    if height > 3:
        raise ValueError("Human Height should not be over 3 meters.")
    return weight / height ** 2


def main():
    # Handle file
    file_content = read_file()
    if file_content:
        print(file_content)

    # Dictionary demonstration
    sample_dict = {"key": "value"}
    print(fetch_dictionary_key(sample_dict, "key"))

    # BMI Calculation
    try:
        height = float(input("Height (in meters): "))
        weight = int(input("Weight (in kg): "))
        bmi = calculate_bmi(height, weight)
        print(f"Your BMI is: {bmi}")
    except ValueError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
