from dotenv import load_dotenv
load_dotenv()
import os

app = {
    "REGIONAL_CODE" : os.getenv("REGIONAL_CODE")
}