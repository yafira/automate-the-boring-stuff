#!/usr/bin/env python3

"""Program to Detect Wheter a Password is Strong or Not."""

import re
import pyperclip

# Strong Password Regexes
pw_length_regex = re.compile(r'.{8,}')       # >= 8 characters
pw_upper_regex = re.compile(r'[A-Z]')        # Contains an upper case letter
pw_lower_regex = re.compile(r'[a-z]')        # Contains a lower case letter
pw_digit_regex = re.compile(r'[0-9]')        # Contains a digit


# Function to check the above regexes
def pw_strength_checker(text):
    """Check if a password is strong."""
    if pw_length_regex.search(text) is None:
        return False
    if pw_upper_regex.search(text) is None:
        return False
    if pw_lower_regex.search(text) is None:
        return False
    if pw_digit_regex.search(text) is None:
        return False
    else:
        return True

# Retrieve Password from clipboard
password = str(pyperclip.paste())

# Run and print relevant message to the console
if pw_strength_checker(password) is True:
    print('That\'s a strong password. Remember to use it for one site only.')
else:
    print('That\'s a weak password. I wouldn\'t recommend using it.')
