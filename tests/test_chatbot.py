import unittest
from experimental_chatbot.bot.chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_send_message(self):
        message = "Hello, how are you?"
        response = self.chatbot.send_message(message)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

    def test_handle_special_commands(self):
        user_input = "/void"
        response = self.chatbot.handle_special_commands(user_input)
        self.assertIsInstance(response, str)
        self.assertEqual(response, "Entering the void... 🌑")

if __name__ == '__main__':
    unittest.main()

    