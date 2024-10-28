import subprocess
import sys
import importlib
from typing import List, Tuple
import logging

class ChatbotSetup:
    def __init__(self):
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('ChatbotSetup')
        
    def check_python_version(self) -> bool:
        """Verify Python version is compatible"""
        required_version = (3, 7)
        current_version = sys.version_info[:2]
        
        if current_version < required_version:
            self.logger.error(
                f"Python {required_version[0]}.{required_version[1]} or higher is required. "
                f"You are using Python {current_version[0]}.{current_version[1]}"
            )
            return False
        return True

    def get_required_packages(self) -> List[Tuple[str, str]]:
        """Define required packages and their versions"""
        return [
            ('textblob', '0.17'),
            ('emoji', '2.2'),
            ('rich', '13.3'),
            ('pyyaml', '6.0'),
            ('requests', '2.28')
        ]

    def check_and_install_package(self, package_name: str, required_version: str) -> bool:
        """Check if a package is installed and install if necessary"""
        try:
            module = importlib.import_module(package_name)
            if hasattr(module, '__version__'):
                current_version = module.__version__
                self.logger.info(f"Found {package_name} version {current_version}")
            return True
        except ImportError:
            try:
                self.logger.info(f"Installing {package_name}>={required_version}")
                subprocess.check_call([
                    sys.executable, 
                    "-m", 
                    "pip", 
                    "install", 
                    f"{package_name}>={required_version}"
                ])
                return True
            except subprocess.CalledProcessError as e:
                self.logger.error(f"Failed to install {package_name}: {str(e)}")
                return False

    def download_nltk_resources(self) -> bool:
        """Download required NLTK resources"""
        try:
            import nltk
            required_resources = [
                'punkt_tab',
                'averaged_perceptron_tagger',
                'wordnet',
                'vader_lexicon'
            ]
            
            for resource in required_resources:
                try:
                    self.logger.info(f"Checking NLTK resource: {resource}")
                    nltk.data.find(f'tokenizers/{resource}')
                except LookupError:
                    self.logger.info(f"Downloading NLTK resource: {resource}")
                    nltk.download(resource, quiet=True)
            
            return True
        except Exception as e:
            self.logger.error(f"Error downloading NLTK resources: {str(e)}")
            return False

    def create_default_config(self) -> bool:
        """Create default config file if it doesn't exist"""
        import os
        import yaml
        
        config_path = 'config.yaml'
        if not os.path.exists(config_path):
            try:
                default_config = {
                    'api_endpoint': 'http://localhost:5000/chat',
                    'authorization_header': 'your-auth-token',
                    'bot_name': 'Chatbot',
                    'user_name': 'You',
                }
                
                with open(config_path, 'w') as f:
                    yaml.dump(default_config, f, default_flow_style=False)
                
                self.logger.info(f"Created default config file: {config_path}")
                return True
            except Exception as e:
                self.logger.error(f"Failed to create config file: {str(e)}")
                return False
        return True

    def verify_system_resources(self) -> bool:
        """Check if system has sufficient resources"""
        import psutil
        
        try:
            # Check available memory (minimum 500MB)
            available_memory = psutil.virtual_memory().available / (1024 * 1024)  # Convert to MB
            if available_memory < 500:
                self.logger.warning(f"Low memory available: {available_memory:.0f}MB")
                return False
                
            # Check available disk space (minimum 100MB)
            disk_usage = psutil.disk_usage('.')
            available_space = disk_usage.free / (1024 * 1024)  # Convert to MB
            if available_space < 100:
                self.logger.warning(f"Low disk space available: {available_space:.0f}MB")
                return False
                
            return True
        except Exception as e:
            self.logger.error(f"Error checking system resources: {str(e)}")
            return True  # Continue anyway if we can't check resources

    def setup(self) -> bool:
        """Run complete setup process"""
        try:
            print("🤖 Starting chatbot setup...")
            
            # Check Python version
            if not self.check_python_version():
                return False
                
            # Install required packages
            for package_name, version in self.get_required_packages():
                if not self.check_and_install_package(package_name, version):
                    return False
                    
            # Download NLTK resources
            #if not self.download_nltk_resources():
            #    return False
                
            # Create default config
            if not self.create_default_config():
                return False
                
            # Verify system resources
            if not self.verify_system_resources():
                print("⚠️  Warning: System resources might be insufficient")
                # Continue anyway with a warning
                
            print("✅ Setup completed successfully!")
            return True
            
        except Exception as e:
            self.logger.error(f"Setup failed: {str(e)}")
            return False

def initialize_bot():
    """Initialize the bot with all necessary setup"""
    setup = ChatbotSetup()
    if setup.setup():
        # Import and create bot only after successful setup
        try:
            from experimental_chatbot.bot.chatbot import Chatbot
            return Chatbot()
        except Exception as e:
            setup.logger.error(f"Failed to initialize bot: {str(e)}")
            return None
    return None

if __name__ == "__main__":
    setup = ChatbotSetup()
    setup.setup()

