import unittest
from unittest.mock import patch
from io import StringIO
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    @patch('builtins.input', side_effect=['4', '2', '3'])
    def test_generate_password_length(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            generated_password = generate_password(4, 2, 3)

        self.assertEqual(len(generated_password), 9)

    @patch('builtins.input', side_effect=['5', '3', '2'])
    def test_generate_password_character_types(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            generated_password = generate_password(5, 3, 2)

        self.assertTrue(any(char.isalpha() for char in generated_password))  # At least one letter
        self.assertTrue(any(char.isdigit() for char in generated_password))  # At least one number
        self.assertTrue(any(not char.isalnum() for char in generated_password))  # At least one symbol

    @patch('builtins.input', side_effect=['0', '0', '0'])
    def test_generate_password_zero_length(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            generated_password = generate_password(0, 0, 0)

        self.assertEqual(len(generated_password), 0)

if __name__ == '__main__':
    unittest.main()
