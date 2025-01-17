import sys
import os
import random
import time

# Add the path to the utils directory
sys.path.append(r'C:\Users\19564\Documents\CL7SDRuiz\utils')

# Print sys.path to verify
print("sys.path:", sys.path)

# Now import the logger from utils_logger
from utils_logger import logger

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Define getter function for message interval
def get_message_interval() -> int:
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval

# Lists for generating buzz messages
ADJECTIVES = ["fun", "inspiring", "boring", "exciting", "weird", "shocking", "puzzling"]
ACTIONS = ["watched", "experienced", "tried", "shared", "loved"]
TOPICS = ["a movie", "a concert", "an app", "a wedding", "a story"]

# Generate a stream of buzz messages
def generate_messages():
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        yield f"I just {action} {topic}! It was {adjective}."

# Main function to run this producer
def main() -> None:
    logger.info("START producer...")
    logger.info("Generating 100 messages...")

    interval_secs = get_message_interval()

    try:
        # Generate 100 messages
        for i, message in enumerate(generate_messages()):
            if i >= 100:  # Stop after generating 100 messages
                break
            logger.info(message)
            time.sleep(interval_secs)  # Delay between messages
    except Exception as e:
        logger.error(f"Error generating messages: {e}")

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")

if __name__ == "__main__":
    main()







        


 

