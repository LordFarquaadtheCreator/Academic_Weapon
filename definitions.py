import os
from dotenv import dotenv_values

#File Paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

#API configs
CONFIG = dotenv_values(ROOT_DIR + '\\.env')
#add error handling...
BING_API_KEY = CONFIG['BING_API_KEY']
OPENAI_API_KEY = CONFIG['OPENAI_API_KEY']
