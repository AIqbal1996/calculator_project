"""
Statistical calculation functions for calculator_tools.

This module provides functions for:
    - Percentage calculation
    - Average calculation
"""

from .exceptions import InvalidOperationError


def _validate_number(value, name="value"):
    """
    Validate that a value is an integer or float.

    Parameters
    ----------
    value : int or float
        Value to validate.
    name : str
        Name of the value used in error messages.

    Raises
    ------
    InvalidOperationError
        If the value is not an integer or float.
    """

    if isinstance(value, bool):
        raise InvalidOperationError(
            f"{name} cannot be a boolean."
        )

    if not isinstance(value, (int, float)):
        raise InvalidOperationError(
            f"{name} must be an integer or float. "
            f"Received: {value!r}"
        )


def calculate_percentage(part, whole):
    """
    Calculate what percentage 'part' is of 'whole'.

    Formula:
        (part / whole) * 100

    Parameters
    ----------
    part : int or float
        The part value.
    whole : int or float
        The total value.

    Returns
    -------
    float
        Percentage value.

    Raises
    ------
    InvalidOperationError
        If values are invalid or whole is zero.

    Examples
    --------
    calculate_percentage(25, 100) -> 25.0
    calculate_percentage(50, 200) -> 25.0
    """

    _validate_number(part, "part")
    _validate_number(whole, "whole")

    if whole == 0:
        raise InvalidOperationError(
            "Cannot calculate percentage when whole is zero."
        )

    return (part / whole) * 100


def calculate_average(values):
    """
    Calculate the arithmetic average of a collection of numbers.

    Formula:
        sum(values) / number_of_values

    Parameters
    ----------
    values : list, tuple, or other iterable
        Collection of numeric values.

    Returns
    -------
    float
        Average value.

    Raises
    ------
    InvalidOperationError
        If values is not a valid collection of numbers
        or if the collection is empty.

    Examples
    --------
    calculate_average([10, 20, 30]) -> 20.0
    calculate_average([5, 10]) -> 7.5
    """

    if isinstance(values, (str, bytes)):
        raise InvalidOperationError(
            "Values must be a collection of numbers, "
            "not a string."
        )

    try:
        values = list(values)
    except TypeError:
        raise InvalidOperationError(
            "Values must be an iterable collection of numbers."
        )

    if len(values) == 0:
        raise InvalidOperationError(
            "Cannot calculate the average of an empty collection."
        )

    for index, value in enumerate(values):
        _validate_number(
            value,
            f"values[{index}]"
        )

    return sum(values) / len(values)