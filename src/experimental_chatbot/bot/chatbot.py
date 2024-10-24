import random, requests, yaml

class Chatbot:
    def __init__(self, config_path='config.yaml'):
        # Load configuration
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            
        # Core settings
        self.api_endpoint = config['api_endpoint']
        self.authorization = config['authorization_header']
        self.bot_name = config['bot_name']
        self.user_name = config['user_name']
        
        # State variables
        self.chat_history = []
        self.weirdness_level = 0.0  # Probability of weird responses
        self.personality = ["neutral"]
        
        # Easter eggs and hidden features
        self.secret_commands = {
            "void": self._enter_void_mode,
            "chaos": self._increase_chaos,
            "dream": self._enter_dream_mode
        }

    def _generate_glitch_text(self, text, intensity=0.3):
        """Add weird glitch effects to the text"""
        if random.random() < intensity:
            glitch_chars = "¯̮̮́́═̶̶░̴̴█̷̷▒̸̸▓̡̡"
            return ''.join(char + random.choice(glitch_chars) if random.random() < intensity else char for char in text)
        return text

    # Secret modes
    def _enter_void_mode(self):
        self.weirdness_level = 1.0
        self.personality = ["mysterious", "dark"]
        self.bot_name = "Void Seeker"
        return "Entering the void... 🌑"

    def _increase_chaos(self):
        self.weirdness_level = min(1.0, self.weirdness_level + 0.1)
        if self.weirdness_level > 0.5:
            self.personality = ["chaotic", "unpredictable"]
            self.bot_name = "Chaos Seeker"
        return "Chaos is rising... 🔥"

    def _enter_dream_mode(self):
        self.weirdness_level = 0.2
        self.personality = ["dreamy", "ethereal"]
        self.bot_name = "Dreamer"
        return "✨ Entering dreamscape... ✨"

    def send_message(self, message):
        
        # Check for secret commands
        if message.lower() in self.secret_commands:
            return self.secret_commands[message.lower()]()

        # Update chat history with the user messages
        self.chat_history.append({"sender": "user", "message": message})

        # Prepare request with enhanced context
        request_data = {
            "memory": self._generate_memory_context(),
            "prompt": "start chat",
            "bot_name": self.bot_name,
            "user_name": self.user_name,
            "chat_history": self.chat_history
        }

        # For testing
        #response = {"response": self._generate_test_response(message)}
        
        # For production
        response = requests.post(
            self.api_endpoint,
            json=request_data,
            headers={"Authorization": self.authorization}
        )
        response_text = response.json().get(
            "model_output",
            "I'm sorry, I cannot respond at the moment."
        )
        
        # Apply reality glitches and personality
        if self.weirdness_level > 0:
            response_text = self._generate_glitch_text(response_text, self.weirdness_level)
        
        # Update chat history with the bot's response
        self.chat_history.append({"sender": "bot", "message": response_text})
        
        return response_text

    def _generate_test_response(self, message):
        """Generate a test response based on user message"""
        responses = [
            f"Hello, {self.user_name}! How can I help you today?",
            f"My name is {self.bot_name}. What can I do for you?",
        ]
        return random.choice(responses)

    def _generate_memory_context(self):
        """Generate a memory context for the bot"""
        memory_string = (
            f"I am {self.bot_name}, a bot with the following traits: "
            f"{', '.join(self.personality)}. "
            f"""My weirdness level is {self.weirdness_level:.2f}.
            This is the probabiliy of being weird.
            """
        )
        return memory_string

    def handle_special_commands(self, user_input):
        if user_input.lower() == "quit":
            return self._generate_glitch_text("Reality shutdown initiated... 🚨", 0)
        elif user_input.lower() == "clear":
            self.clear_chat_history()
            return "Memory purged... 🧠"
        elif user_input.lower() == "change username":
            new_username = input("Enter new username: ")
            self.user_name = new_username
            return f"Username changed to {new_username}"

    def clear_chat_history(self):
        self.chat_history = []
        self.weirdness_level = 0.0
        self.personality = ["neutral"]

