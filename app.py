"""Basic math utilities."""

from typing import Union

def soma(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Return the sum of *a* and *b*."""
    return a + b


if __name__ == "__main__":
    # Quick manual test
    print(soma(2, 3))
