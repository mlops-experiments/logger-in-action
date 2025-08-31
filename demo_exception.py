# # below code is to check the exception config
from src.logger import logging
from src.exception import MyException
import sys
try:
    a = 1+'Z'
except Exception as e:
    print(e)
    logging.info(e)
    raise MyException(e, sys) from e