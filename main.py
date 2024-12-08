import csv

# Open the .csv file containing the morse code
with open("morse.csv", "r") as file:
    # Use the csv module in Python the read the .csv file
    morse_raw = csv.reader(file, delimiter=",", quotechar="'") # configure the parameters to save ',' as a key
    morse_dict = {row[0]: row[1] for row in morse_raw} # Convert the .csv file to dictionary

# Ask for user input
original_string = input("Text to convert to Morse Code: ")

# Create a list with the encoded version of the user input
morse_string = [morse_dict[char] if char in morse_dict else char for char in original_string.upper()]

# Print the unpacked version of the list to keep the spaces between each code
print(*morse_string)