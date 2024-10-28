from experimental_chatbot.setup.bot_setup import ChatbotSetup

class TestChatbotSetup(unittest.TestCase):
    def setUp(self):
        self.setup = ChatbotSetup()

    def test_check_python_version(self):
        self.assertTrue(self.setup.check_python_version())

    def test_check_and_install_package(self):
        self.assertTrue(self.setup.check_and_install_package("requests", "2.25.1"))

    def test_download_nltk_resources(self):
        self.assertTrue(self.setup.download_nltk_resources())

    def test_create_default_config(self):
        self.assertTrue(self.setup.create_default_config())

    def test_verify_system_resources(self):
        self.assertTrue(self.setup.verify_system_resources())

    def test_setup(self):
        self.assertTrue(self.setup.setup())

    def test_initialize_bot(self):
        self.assertIsNotNone(self.setup.initialize_bot())

