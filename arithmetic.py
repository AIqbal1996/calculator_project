"""
Arithmetic operations for the calculator_tools package.

This module provides functions for:
    - Addition
    - Subtraction
    - Multiplication
    - Division
"""

from .exceptions import InvalidOperationError


def _validate_numbers(a, b):
    """
    Validate that both values are numbers.

    Parameters
    ----------
    a : int or float
        First value.
    b : int or float
        Second value.

    Raises
    ------
    InvalidOperationError
        If either value is not an integer or float.
    """

    if isinstance(a, bool) or isinstance(b, bool):
        raise InvalidOperationError(
            "Boolean values are not valid numbers."
        )

    if not isinstance(a, (int, float)):
        raise InvalidOperationError(
            f"Invalid value for a: {a!r}. "
            "Expected an integer or float."
        )

    if not isinstance(b, (int, float)):
        raise InvalidOperationError(
            f"Invalid value for b: {b!r}. "
            "Expected an integer or float."
        )


def add(a, b):
    """
    Add two numbers.

    Example
    -------
    add(10, 5) -> 15
    """

    _validate_numbers(a, b)

    return a + b


def subtract(a, b):
    """
    Subtract b from a.

    Example
    -------
    subtract(10, 5) -> 5
    """

    _validate_numbers(a, b)

    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Example
    -------
    multiply(10, 5) -> 50
    """

    _validate_numbers(a, b)

    return a * b


def divide(a, b):
    """
    Divide a by b.

    Parameters
    ----------
    a : int or float
        Numerator.
    b : int or float
        Denominator.

    Raises
    ------
    InvalidOperationError
        If b is zero.

    Example
    -------
    divide(10, 2) -> 5.0
    """

    _validate_numbers(a, b)

    if b == 0:
        raise InvalidOperationError(
            "Division by zero is not allowed."
        )

    return a / b