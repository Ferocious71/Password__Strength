# Python program to check the password strength. 
import string

# User-input of Password
pswd = input("Enter the password: \n") 

# function to validate the password
def check_password_strength(pwd):

# keeping all the values as false to later set it accordingly for Password Strength    
    has_number = False
    has_special_char = False
    special_characters = set(string.punctuation)  # Set of all special characters
    has_upper = False
    has_lower = False
    has_length = False
    length = len(pswd)  # persisting the length of the password user entered

    for char in pswd:

        #password length condition should be atleast 8 characters
        if length >= 8:
            has_length = True

        #checking if the password has any Upper case letter by calling In-built function
        if char.isupper():
            has_upper = True
        
        #checking if the password has any Lower case letter  by calling In-built function
        if char.islower():
            has_lower = True

        #checking if the password has any digit  by calling In-built function
        if char.isdigit():
            has_number = True

        #checking if the password has any sppecial chracters  by calling In-built function
        if char in special_characters:
            has_special_char = True
            
        # If all are found
        if has_length and has_number and has_special_char and has_upper and has_lower:
            print("Strong Password")
            return True
    
    print("Weak Password : Should fulfil below condiions - \n 1.  Minimum length: The password should be at least 8 characters long. \n 2.  Contains both uppercase and lowercase letters. \n 3. Contains at least one digit (0-9). \n 4. Contains at least one special character (e.g., !, @, #, $, %). ")
    return False        


check_password_strength(pswd)

