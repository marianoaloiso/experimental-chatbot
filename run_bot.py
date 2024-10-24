#!/usr/bin/env python3
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.traceback import install

# Add src directory to Python path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

# Import interface and chatbot classes
from experimental_chatbot.bot.chatbot import Chatbot
from experimental_chatbot.interface.terminal import TerminalInterface

# Install rich traceback handler for better error display
install(show_locals=True)

def main():
    """Main entry point for the chatbot"""
    console = Console()
    
    try:
        # Initialize system
        console.print("[cyan]Initializing chatbot...[/]")
        
        # Create bot and terminal interface
        chatbot = Chatbot()
        terminal = TerminalInterface(chatbot)

        # Display startup message
        terminal.run()
        
        return 0
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Goodbye![/]")
        return 0
        
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/]")
        console.print_exception()
        return 1

if __name__ == "__main__":
    sys.exit(main())

    