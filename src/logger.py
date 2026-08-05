"""Python Logging - Quick Summary
Logging is used to record a program's execution, errors, and important events.
It is preferred over print() because logs can be saved to a file, include timestamps, line numbers, and different severity levels.
Logging is mainly used for debugging, monitoring, and tracking errors in real-world applications.
Logging Levels
Level	Meaning
DEBUG	Detailed information for developers (debugging).
INFO	Normal execution information.
WARNING	Something unexpected happened, but the program can continue.
ERROR	An operation failed due to an error.
CRITICAL	A severe error that may stop the entire application.
Severity Order
DEBUG < INFO < WARNING < ERROR < CRITICAL

If you set:

logging.basicConfig(level=logging.INFO)

Only these levels are logged:

INFO
WARNING
ERROR
CRITICAL

DEBUG messages are ignored.

One-line Interview Answer

Logging is a Python module used to record a program's execution, errors, and important events with different severity levels, making debugging and monitoring easier than using print().

"""

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# if __name__=="__main__":
#     logging.info("Logging started")
    
    