import os
from dotenv import load_dotenv

def get_api_token(key:str):
  """ Get the api key based on token you need.

  Args:
    key: String. A key value to get your API token. 

  Return:
    String. Returns an API token. 
  """
  load_dotenv()
  return os.getenv(key)
