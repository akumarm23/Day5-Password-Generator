## PyPassword Generator

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-passing-brightgreen.svg)](https://github.com/your-username/your-repository/actions)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Introduction

This Python script generates secure and customizable passwords by combining lowercase and uppercase letters, numbers, and symbols. Users are prompted to input the desired number of letters, symbols, and numbers for the password.

## Usage

### Requirements

- Python 3.8

### How to Run

1. **Clone or Download:**
   Clone the repository or download the script to your local machine.
   ```
   git clone https://github.com/your-username/PyPassword-Generator.git](https://github.com/akumarm23/Day5-Password-Generator.git)
   cd PyPassword-Generator
   ```
2. **Run the Script:**
   Execute the script in a Python environment.
    ```
   python password_generator.py <nr_letters> <nr_symbols> <nr_numbers>
    ```
   Replace `<nr_letters>`, `<nr_symbols>`, and `<nr_numbers>` with the desired number of letters, symbols, and numbers in the password, respectively.

## Code Overview

This script utilizes the `random` and `string` modules for robust password generation. The characters are intelligently shuffled to bolster the password's security.

### Variables

- **letters:** A list of lowercase and uppercase letters.
- **numbers:** A list of numbers from 0 to 9.
- **symbols:** A list of common symbols ('!', '@', '#', '$', '%', '&', '+', '*', '(', ')').

### User Input

- **nr_letters:** Number of letters in the password.
- **nr_symbols:** Number of symbols in the password.
- **nr_numbers:** Number of numbers in the password.

### Password Generation (Hard Level)

1. The script initializes an empty list, **password_list**, to store generated characters.
2. For the specified number of letters, random letters are added to the list.
3. For the specified number of symbols, random symbols are added to the list.
4. For the specified number of numbers, random numbers are added to the list.
5. The **password_list** is shuffled, randomizing the character order.
6. The shuffled characters are concatenated, forming the final password.

### Display

The generated password is presented to the user.

## Testing

The script includes unit tests to ensure its functionality. To run the tests locally, use the following command:
 ```
python -m unittest test_password_generator.py
 ```

## GitHub Actions

This repository is configured with GitHub Actions to automatically run tests whenever changes are pushed to the `main` branch. The workflow is defined in the `.github/workflows/test.yml` file.

## Notes

- Adjust the password length, symbols, and numbers to meet your security criteria.
- This script provides a customizable and secure solution for generating strong passwords across various applications.

Feel free to use and modify this script for your password generation needs. Stay secure!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License (MIT)
=====================

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


