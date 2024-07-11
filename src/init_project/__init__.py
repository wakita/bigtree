import sys
from pathlib import Path

PROJECT = Path(__file__).parent.parent.parent

if __name__ == '__main__':
    for p in sys.path: print(f' - {p}')