import sys
from logging.handlers import TimedRotatingFileHandler
import logging

def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   formatter = logging.Formatter('%(asctime)s : %(name)s - %(levelname)s - %(message)s')
   console_handler.setFormatter(formatter)
   return console_handler

def get_file_handler():
   file_handler = TimedRotatingFileHandler('app.log', when='D', interval=30, backupCount=3)
   formatter = logging.Formatter('%(asctime)s : %(name)s - %(levelname)s - %(message)s')
   file_handler.setFormatter(formatter)
   return file_handler
