from dotenv import load_dotenv
load_dotenv()
import os

auth = {
    "API_KEY" : os.getenv("NEARMAP_KEY", None),
    "BASE_URL": os.getenv("NEARMAP_BASE_URL", "https://api.nearmap.com/")
}