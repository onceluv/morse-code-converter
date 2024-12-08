import csv

# Open the .csv file containing the morse code.
with open("morse.csv", "r") as file:
    # Use the csv module in Python the read the .csv file.
    morse_raw = csv.reader(file, delimiter=",", quotechar="'") # Configure the parameters to save ',' as a key.
    morse_dict = {row[0]: row[1] for row in morse_raw} # Convert the .csv file to dictionary.

# Variable to keep track if user want to stop the program.
stop_program = False

# While the 'stop_program' is False, the program will repeat.
while not stop_program:
    # Ask for user input.
    original_string = input("Text to convert to Morse Code: ")

    # Create a list with the encoded version of the user input.
    morse_string = [morse_dict[char] if char in morse_dict else char for char in original_string.upper()]

    # Print the unpacked version of the list to keep the spaces between each code.
    print(*morse_string)

    # Ask if user want to save the Morse Code in a .txt file.
    save_code = input("Do you want to save the Morse Code in a .txt file? (yes/no) ")
    if save_code.lower() == "yes":
        name_txt = input("Name of the file (Without '.txt'): ") # Ask for name of the .txt file.
        with open(f"{name_txt}.txt", "w") as new_txt:
            new_txt.write(" ".join(morse_string))

    # Ask user if he wants to convert another string.
    repeat = input("Convert again? (yes/no) ")
    # Change 'stop_program' to false if user don't want to convert another string.
    if repeat.lower() == "no":
        stop_program = True