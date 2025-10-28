import sys
import logging

def error_message_detail(error, error_details:sys):
    _,_,exc_tab=error_details.exc_info
    file_name=exc_tab.tb_frame.f_code.co_filename
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tab.tb_lineo,str(error))
    return error_message
class CustomException(Exception):
    def __init__(self, error_message, error_message_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_details=error_message_detail)


    def __str__(self):
        return self.error_message
    

