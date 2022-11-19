
import pytest
import pandas as pd
import logging
import os
import getpass
import sys

# removed the file when using docker because the file is in the container and no logs are written
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s') #, filename="helloworld.log")



logging.info("hello world 1")
logging.info("added pandas")

d = pd.array([1])

logging.info("Current Directory: " + os.getcwd())
logging.info("Current UserID: " + getpass.getuser())
logging.info("Current Python: " + sys.version)
