import csv

# Open the .csv file containing the morse code.
with open("morse.csv", "r") as file:
    morse_raw = csv.reader(file, delimiter=",", quotechar="'") # Configure the parameters to save ',' as a key.
    morse_dict = {row[0]: row[1] for row in morse_raw} # Convert the .csv file to dictionary.

def main():
    # Variable to keep track if user want to stop the program.
    stop_program = False

    # While the 'stop_program' is False, the program will repeat.
    while not stop_program:

        # Ask if user want to encode or decode.
        task = input("Encode or decode? ").lower()

        if task in ["encode", "en"]:
            # Ask for user input.
            original_str = input("Text to convert to Morse Code: ").upper()

            # Create a list with the encoded version of the user input.
            encoded_list = [morse_dict[char] if char in morse_dict else char for char in original_str]

            # Print the unpacked version of the list to keep the spaces between each code.
            print(*encoded_list)

            # Ask if user want to save the Morse Code in a .txt file.
            while True:
                save_code = input("Save Morse Code in a .txt file? (yes/no) ").lower()
                if save_code in ["yes","y"]:
                    name_txt = input("Name of the file (Without '.txt'): ") # Ask for name of the .txt file.
                    with open(f"{name_txt}.txt", "w") as new_txt:
                        new_txt.write(" ".join(encoded_list))
                    break
                elif save_code in ["no", "n"]:
                    break
                # Repeat the question if invalid answer
                else:
                    print("Answer not recognized. Type 'yes' or 'no'.")

            # Call function to ask if user wants to stop the program.
            stop_program = stop()

        # If user want to decode a Morse Code.
        elif task in ["decode", "de"]:
            # Invert key-values in morse_dict to decode Morse Code.
            inverted_morse_dict = {value: key for key, value in morse_dict.items()}

            str_to_decode = input("Text to decode (Code format: . - ): ")
            decoded_list = [inverted_morse_dict[char] if char in inverted_morse_dict else char for char in
                            str_to_decode.split(" ")]
            print(*decoded_list)

            # Call function to ask if user wants to stop the program.
            stop_program = stop()

        # Repeat main function if invalid answer.
        else:
            print("Answer not recognized. Type 'encode' or 'decode'.")

def stop() -> bool:
    """Function to return True if user want to stop the program, False if not"""
    while True:
        repeat = input("Encode or decode again? (yes/no) ").lower()
        if repeat in ["no", "n"]:
            return True
        elif repeat in ["yes", "n"]:
            return False

        # Repeat the function if invalid answer
        else:
            print("Answer not recognized. Type 'yes' or 'no'.")

main()