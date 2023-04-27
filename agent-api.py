import requests
import dotenv
import os

print(os.getcwd())

FIXIE_API_KEY = dotenv.dotenv_values(
    ".env")["FIXIE_API_KEY"]
print(FIXIE_API_KEY)
