import os
import sys

# Directories
SCRIPT_FILE_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DATA_DIR = os.path.join(SCRIPT_FILE_DIR, "internal")

# Filenames
TOKEN_FILE = "token.json"
INPUT_FILE = "input.csv"

# Full paths
TOKEN_PATH = os.path.join(DATA_DIR, TOKEN_FILE)
INPUT_PATH = os.path.abspath(SCRIPT_FILE_DIR, INPUT_FILE)
