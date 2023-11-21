from . import  ek
from . import first

print("ONE module __init__.py file")
if __name__ == "__main__":
    print("ONE the main module")

__all__ = [
    "ek",
    "first"
]
