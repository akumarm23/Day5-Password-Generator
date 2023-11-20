# Password Generator Project

## Introduction
This Python script generates a secure and customizable password using a combination of lowercase and uppercase letters, numbers, and symbols. The user is prompted to input the desired number of letters, symbols, and numbers for the password.

## Usage
1. Clone the repository or download the script.
2. Run the script in a Python environment.
3. Follow the prompts to specify the length of the password and the number of symbols and numbers.

## Code Overview
The code utilizes the `random` and `string` modules to generate random characters for the password. The characters are then shuffled to enhance the password's security.

### Variables
- **letters**: A list containing both lowercase and uppercase letters.
- **numbers**: A list containing numbers from 0 to 9.
- **symbols**: A list containing common symbols ('!', '@', '#', '$', '%', '&', '+', '*', '(', ')').

### User Input
- **nr_letters**: Number of letters in the password.
- **nr_symbols**: Number of symbols in the password.
- **nr_numbers**: Number of numbers in the password.

### Password Generation (Hard Level)
1. The script creates an empty list named **password_list** to store the generated characters.
2. For the specified number of letters, random letters are added to the list.
3. For the specified number of symbols, random symbols are added to the list.
4. For the specified number of numbers, random numbers are added to the list.
5. The **password_list** is shuffled to randomize the order of characters.
6. The shuffled characters are concatenated to form the final password.

### Display
The generated password is displayed to the user.

## Notes
- Adjust the length of the password and the number of symbols and numbers according to your security requirements.
- This script provides a customizable and secure way to generate strong passwords for various applications.

Feel free to use and modify this script for your password generation needs. Stay secure!
