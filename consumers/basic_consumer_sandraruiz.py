# basic_consumer_case.py

import sys
import os
import random
import time

# Add the path to the utils directory
sys.path.append(r'C:\Users\19564\Documents\CL7SDRuiz\utils')

# Import functions from local modules
from utils_logger import logger

def get_log_file_path() -> str:
    """Return the path to the log file being generated."""
    return r'C:\Users\19564\Documents\CL7SDRuiz\logs\project_log.log'  # path

def process_message(log_file) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r") as file:
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and patiently waiting for a new log msg...")

        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue

            message = line.strip()
            print(f"Consumed log message: {message}")

            if "I just loved a concert! It was fun." in message:
                print(f"ALERT: A special message was found! \nA feeling of Love")
                logger.warning(f"ALERT: The special message was found! \n#LOVE")

def main() -> None:
    """Main entry point."""

    logger.info("START...")

    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")

    logger.info("END.....")

if __name__ == "__main__":
    main()

