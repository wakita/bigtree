import sys
from pathlib import Path

PROJECT = Path(__file__).parent.parent.parent
if str(PROJECT/'src') not in sys.path:
    sys.path.insert(0, str(PROJECT/'src'))

if __name__ == '__main__':
    for p in sys.path: print(p)