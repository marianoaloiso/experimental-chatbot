from ..bot.chatbot import Chatbot

from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
import os, random, sys, time

class TerminalInterface:
    def __init__(self, chatbot):
        # Initialize Rich console with minimal theme
        self.theme = Theme({
            "bot": "magenta",
            "user": "blue",
            "system": "cyan",
            "error": "red"
        })
        self.console = Console(theme=self.theme)
        self.chatbot = chatbot
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_startup(self):
        """Display a startup sequence with the welcome message"""
        self.clear_screen()
        
        startup_text = f"""
        [system]╔════════════════════════════╗
        ║     Bot Terminal Interface    ║
        ║    Type 'help' for commands   ║
        ╚════════════════════════════╝[/]

        [cyan]Welcome to Chatbot![/]

        [green]Available Commands:[/]
        • [bold]help[/] - Show available commands
        • [bold]quit[/] - Exit the program
        • [bold]clear[/] - Clear screen
        • [bold]change username[/] - Change your username

        [yellow]Tips:[/]
        • Type your message and press Enter to chat
        • Press Ctrl+C at any time to exit

        [cyan]Ready to start chatting![/]
        """
        self.console.print(startup_text)

    def show_help(self):
        """Display available commands"""
        help_text = """
        [system]Available commands:
        • quit - Exit the program
        • clear - Clear the screen
        • status - Show bot status
        • reset - Reset bot state[/]
        """
        self.console.print(help_text)

    def display_message(self, text, style="bot"):
        """Display a message with optional typing effect"""
        if style == "bot" and self.chatbot.weirdness_level > 0.5:
            # Add simple effects for weird responses
            text = f"✨ {text} ✨" if random.random() > 0.5 else f"🌌 {text} 🌌"
        
        title = self.chatbot.bot_name if style == "bot" else self.chatbot.user_name
        panel = Panel(
            text,
            border_style=style,
            title=title,
            title_align="left"
        )
        self.console.print(panel)

    def run(self):
        """Main interaction loop"""
        self.display_startup()
        
        while True:
            try:
                # Simple prompt with weirdness indicator
                weird_level = "~" * int(self.chatbot.weirdness_level * 10)
                prompt = f"{weird_level}> "
                
                # Get user input
                user_input = self.console.input(f"[user]{self.chatbot.user_name}{prompt}[/]")
                
                # Handle special commands
                command_response = self.chatbot.handle_special_commands(user_input)
                if command_response:
                    if user_input.lower() == "change username":
                        continue

                    self.display_message(command_response, "system")
                    if user_input.lower() == "quit":
                        break
                else:
                    # Send user input to chatbot and display response
                    response = self.chatbot.send_message(user_input)
                    self.display_message(response)
                    
            except KeyboardInterrupt:
                self.console.print("\n[error]Exiting...[/]")
                break
            except Exception as e:
                self.console.print(f"[error]Error: {str(e)}[/]")

