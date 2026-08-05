import unittest

from game_logic_connector import GameLogicConnector


class TestGameLogicConnector(unittest.TestCase):
    def setUp(self):
        self.connector = GameLogicConnector()
        self.connector.correct_answer = "halv åtta"

    def test_correct_answer_does_not_remove_a_life(self):
        is_correct, score, game_over = self.connector.submit_answer("Halv åtta")

        self.assertTrue(is_correct)
        self.assertEqual(score, 10)
        self.assertEqual(self.connector.fetch_lives(), 3)
        self.assertFalse(game_over)

    def test_wrong_answer_removes_one_life(self):
        is_correct, score, game_over = self.connector.submit_answer("wrong")

        self.assertFalse(is_correct)
        self.assertEqual(score, 0)
        self.assertEqual(self.connector.fetch_lives(), 2)
        self.assertFalse(game_over)

    def test_third_wrong_answer_ends_the_game(self):
        self.connector.submit_answer("wrong")
        self.connector.submit_answer("wrong")
        is_correct, score, game_over = self.connector.submit_answer("wrong")

        self.assertFalse(is_correct)
        self.assertEqual(score, 0)
        self.assertEqual(self.connector.fetch_lives(), 0)
        self.assertTrue(game_over)

    def test_end_game_prepares_three_lives_for_the_next_game(self):
        self.connector.game.lives = 0

        self.connector.end_game()

        self.assertEqual(self.connector.fetch_lives(), 3)

    def test_hint_content_is_available_on_click(self):
        self.assertEqual(
            self.connector.provide_hint(),
            "Think about 'över' and 'i'.",
        )


if __name__ == "__main__":
    unittest.main()
