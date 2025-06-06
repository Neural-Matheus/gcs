"""Basic arithmetic operations."""

from typing import Union

Number = Union[int, float]

def sum_numbers(a: Number, b: Number) -> Number:
    """Return the sum of *a* and *b*.

    Args:
        a (Number): First addend.
        b (Number): Second addend.

    Returns:
        Number: The arithmetic sum of the two numbers.
    """
    return a + b
