import numpy as np
import logging

def compute(a, b):
    "Correcting documentation in function from 'conflicting-branch'"
    return a + b

def log_warning(msg):
    logging.warning(msg)
def log_info(msg):
    "This function is added by a child branch whose parent is 'conflicting-branch"
    logging.info(msg)