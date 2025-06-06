"""Unit tests for arithmetic operations."""

import pytest

from app import sum_numbers


def test_sum_numbers() -> None:
    """Check if the sum of 2 and 3 equals 5."""
    assert sum_numbers(2, 3) == 5
