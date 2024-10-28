import unittest
from experimental_chatbot.interface.terminal import TerminalInterface

class TestTerminalInterface(unittest.TestCase):
    def setUp(self):
        self.interface = TerminalInterface()

    def test_send_message(self):
        message = "Hello, world!"
        response = self.interface.send_message(message)
        self.assertEqual(response, "Message sent: Hello, world!")

    def test_receive_message(self):
        message = "Hello, world!"
        self.interface.send_message(message)
        received_message = self.interface.receive_message()
        self.assertEqual(received_message, "Received message: Hello, world!")

if __name__ == '__main__':
    unittest.main()

