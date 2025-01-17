"""
basic_consumer_case.py

Read a log file as it is being written.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import sys
import os
import random
import time

# Add the path to the utils directory
sys.path.append(r'C:\Users\19564\Documents\CL7SDRuiz\utils')

# Import functions from local modules
from utils_logger import logger

#####################################
# Define a function to get the log file path
#####################################

def get_log_file_path() -> str:
    """Return the path to the log file being generated."""
    # Adjust this path according to where your log file is stored
    return r'C:\Users\19564\Documents\CL7SDRuiz\logs\project_log.log'

if not os.path.exists(log_file_path):
    print(f"Log file does not exist at {log_file_path}")

log_folder = os.path.dirname(log_file_path)
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    print(f"Log folder created at: {log_folder}")



#####################################
# Define a function to process a single message
#####################################

def process_message(log_file) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r") as file:
        # Move to the end of the file
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and patiently waiting for a new log msg...")

        # Use while True loop so the consumer keeps running forever
        while True:
            # Read the next line of the file
            line = file.readline()

            # If the line is empty, wait for a new log entry
            if not line:
                # Wait a second for a new log entry
                delay_seconds = 1
                time.sleep(delay_seconds)
                # Keep checking for new log entries
                continue

            # We got a new log entry!
            # Remove any leading/trailing white space and log the message
            message = line.strip()
            print(f"Consumed log message: {message}")

            # Monitor and alert on special conditions
            if "I just loved a concert! It was fun." in message:
                print(f"ALERT: A special message was found! \n"{A feeling of Love}")
                logger.warning(f"ALERT: The special message was found! \n"{#LOVE}")
                    
 print(f"ALERT: A special message was found! \nA feeling of Love")
logger.warning(f"ALERT: The special message was found! \n#LOVE")



#####################################
# Define main function for this script.
#####################################

def main() -> None:
    """Main entry point."""

    logger.info("START...")

    # Call the function to get the path to the log file
    log_file_path = get_log_file_path()  # Ensure this function is defined
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        # Try to call the process_message function with the log file path
        # as an argument. We know things will go wrong
        # eventually when the user stops the process, so we use a try block.
        process_message(log_file_path)

    except KeyboardInterrupt:
        print("User stopped the process.")

    logger.info("END.....")

#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    main()

