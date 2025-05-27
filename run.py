import subprocess

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
subprocess.run(['py', 'main.py'])
