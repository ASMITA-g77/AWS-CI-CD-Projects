import sys
import os
from src.logger import logging
from datetime import datetime

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python scripts name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)    
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message


# basic config needed
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(), "logs")
# os.makedirs(logs_path, exist_ok=True)
# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# only needed to import logging

# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info(f"exception occured {e}")
#         raise CustomException(e,sys)
    


# Without super().__init__()
# class CustomException(Exception):
#     def __init__(self, error_message):
#         self.error_message = error_message

# Your own variable self.error_message exists, so if you print it using your custom __str__(), it still works.

# However, the parent Exception never receives the original message.

# Some Python features, logging libraries, debugging tools, or frameworks rely on the parent Exception being initialized correctly. Without super().__init__(), they may not behave as expected.


# error_details is the reference to the sys
# error_detail.exc_info() give the tracekback containing 


# str
# If a class defines __str__(), then print(object) automatically prints whatever __str__() returns.
# We use __str__() so that whenever our CustomException object is printed, it displays our custom detailed error message instead of the default exception message.