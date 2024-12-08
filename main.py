# Set dictionary to insert the morse code key and values
morse_dict = {" ": "/"} # The '/' will replace the space

# Open the .csv file containing the morse code
with open("morse.csv", "r") as file:
    # Iterate through each row and add them as key and values in the dictionary
    for row in file:
        key, value = row.split(",") # Split the row and save the key and value separately
        morse_dict[key] = value[:-1] # Remove the '\n' from the values

# Ask for user input
original_string = input("Write what you want to convert to Morse Code: ")

# Create a list with the encoded version of the user input
morse_string = [morse_dict[char] if char in morse_dict else char for char in original_string.upper()]

# Print the unpacked version of the list to keep the spaces between each code
print(*morse_string)