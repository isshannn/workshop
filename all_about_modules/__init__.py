from . import one
from . import two
from . import three
print("Main module __init__.py file")

__all__ = [
    "one",
    "two",
    "three",
]
if __name__ == "__main__":
    print("Inside the main module")
