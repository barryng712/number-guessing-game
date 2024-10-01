import unittest
from unittest.mock import patch
from io import StringIO
import cli

class TestNumberGuessingGame(unittest.TestCase):

    def test_display_welcome_msg(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cli.display_welcome_msg()
            self.assertIn("Welcome to the Number Guessing Game!", fake_out.getvalue())
            self.assertIn(f"I'm thinking of a number between {cli.MIN} and {cli.MAX}.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['a', '4', '2'])
    def test_choose_difficulty_level(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = cli.choose_difficulty_level()
            self.assertEqual(result, 2)
            self.assertIn("Invalid input. Please enter a number.", fake_out.getvalue())
            self.assertIn("Invalid choice. Please enter 1, 2, or 3.", fake_out.getvalue())
            self.assertIn("You have selected the Medium difficulty level.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['a', '0', '101', '50'])
    def test_get_valid_guess(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = cli.get_valid_guess()
            self.assertEqual(result, 50)
            self.assertIn("Invalid input. Please enter a number.", fake_out.getvalue())
            self.assertIn(f"Please enter a number between {cli.MIN} and {cli.MAX}", fake_out.getvalue())

    @patch('cli.get_valid_guess', side_effect=[50, 75, 62, 68, 65])
    def test_play_win(self, mock_get_valid_guess):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = cli.play(2, 65)  # Medium difficulty, correct number is 65
            self.assertTrue(result)
            self.assertIn("Congratulations! You guess the correct number", fake_out.getvalue())

    @patch('cli.get_valid_guess', side_effect=[50, 75, 62, 68, 70])
    def test_play_lose(self, mock_get_valid_guess):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = cli.play(2, 65)  # Medium difficulty, correct number is 65
            self.assertFalse(result)
            self.assertIn("No more chances left. The correct number should be 65 You lose!", fake_out.getvalue())

    @patch('cli.play', return_value=True)
    @patch('cli.choose_difficulty_level', return_value=2)
    @patch('builtins.input', side_effect=['yes', 'no'])
    def test_main(self, mock_input, mock_choose_difficulty, mock_play):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cli.main()
            self.assertIn("Thanks for playing! Goodbye", fake_out.getvalue())
            self.assertEqual(mock_play.call_count, 2)

if __name__ == '__main__':
    unittest.main()
