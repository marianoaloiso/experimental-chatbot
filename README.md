# Experimental Chatbot with Terminal Interface

This project is an experimental chatbot that features a dynamic personality and "weirdness" modes. It includes a terminal-based interface powered by [Rich](https://github.com/Textualize/rich) for enhanced display. The chatbot can interact with users, manage chat histories, respond to secret commands, and offer unique glitch effects in its responses.

## Features
- **Chatbot Personality:** The bot has personality traits like "neutral," "dreamy," "mysterious," and more, which change based on the conversation or secret commands.
- **Weirdness Level:** Introduces randomness in responses, adding "glitch" effects when the weirdness level increases.
- **Secret Commands:** Unlock hidden modes such as `void`, `chaos`, and `dream` modes for varied interactions.
- **Terminal Interface:** An interactive, text-based interface using Rich, featuring dynamic styling for user-bot conversations.
- **Memory and State:** The bot keeps a chat history and adjusts responses based on the current conversation.

## Prerequisites
- Python 3.8 or higher
- Install required dependencies:

```bash
pip install -r requirements.txt
```

### Key Libraries
- `requests`: For making API calls (production mode).
- `pyyaml`: For handling configuration in YAML format.
- `rich`: For rich text formatting and terminal interface.

## Configuration
Make sure `config.yaml` file stores the necessary configuration for the chatbot:

```yaml
api_endpoint: "https://api.example.com/chat"
authorization_header: "Bearer YOUR_TOKEN"
bot_name: "Experimental Bot"
```

- `api_endpoint`: API endpoint for the chatbot's backend.
- `authorization_header`: The authorization token required to interact with the API.
- `bot_name`: The name of the chatbot.

## Usage

### Run the Bot
To start the chatbot, use the following command:

```bash
python3 run_bot.py
```

### Available Commands
- `quit`: Exit the program.
- `clear`: Clear the chat history.
- `help`: Display available commands.
- `change username`: Change the user's name.

### Secret Commands
- `void`: Enter a mysterious, dark mode with maximum weirdness.
- `chaos`: Gradually increases the weirdness level.
- `dream`: Activate a dreamy, ethereal mode with light weirdness.

### Example Session

```
> python3 run_bot.py
Initializing chatbot...
╔════════════════════════════╗
║     Bot Terminal Interface ║
║    Type 'help' for commands║
╚════════════════════════════╝

Welcome to Chatbot!

> Hello bot!
You> Hello, User! How can I help you today?
> chaos
Bot> Chaos is rising... 🔥
> dream
Bot> ✨ Entering dreamscape... ✨
```

## Customization
### Modify Weirdness Levels
You can adjust the weirdness level by calling the hidden `chaos` command multiple times or directly modifying the code in `Chatbot` class.

### Add More Personality Modes
You can expand the chatbot's personality by adding more secret modes in the `Chatbot` class, modifying the `personality` state.

## Error Handling
The bot handles exceptions gracefully and displays detailed error traces in the terminal using `Rich`'s traceback feature.

## Contributing
Feel free to submit pull requests or suggest new features!

## License
This project is licensed under the MIT License.
