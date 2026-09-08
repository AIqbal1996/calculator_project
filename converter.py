"""
Conversion functions for the calculator_tools package.

This module provides:
    - Celsius to Fahrenheit
    - Fahrenheit to Celsius
    - Simple length-unit conversion
"""

from .exceptions import InvalidOperationError


def _validate_number(value, name="value"):
    """
    Validate that a value is an integer or float.

    Raises
    ------
    InvalidOperationError
        If value is not numeric.
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


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Formula:
        Fahrenheit = (Celsius * 9/5) + 32

    Example
    -------
    celsius_to_fahrenheit(0) -> 32.0
    """

    _validate_number(celsius, "celsius")

    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Formula:
        Celsius = (Fahrenheit - 32) * 5/9

    Example
    -------
    fahrenheit_to_celsius(32) -> 0.0
    """

    _validate_number(fahrenheit, "fahrenheit")

    return (fahrenheit - 32) * 5 / 9


# Conversion factors relative to meters.
_LENGTH_FACTORS = {
    "meter": 1.0,
    "meters": 1.0,
    "m": 1.0,

    "kilometer": 1000.0,
    "kilometers": 1000.0,
    "km": 1000.0,

    "centimeter": 0.01,
    "centimeters": 0.01,
    "cm": 0.01,

    "millimeter": 0.001,
    "millimeters": 0.001,
    "mm": 0.001,

    "mile": 1609.344,
    "miles": 1609.344,
    "mi": 1609.344,

    "yard": 0.9144,
    "yards": 0.9144,
    "yd": 0.9144,

    "foot": 0.3048,
    "feet": 0.3048,
    "ft": 0.3048,

    "inch": 0.0254,
    "inches": 0.0254,
    "in": 0.0254,
}


def convert_units(value, from_unit, to_unit):
    """
    Convert a length value from one supported unit to another.

    Parameters
    ----------
    value : int or float
        Numeric value to convert.

    from_unit : str
        Unit to convert from.

    to_unit : str
        Unit to convert to.

    Returns
    -------
    float
        Converted value.

    Raises
    ------
    InvalidOperationError
        If value is invalid, units are invalid,
        or units are unsupported.

    Examples
    --------
    convert_units(1, "kilometer", "meter")
        -> 1000.0

    convert_units(100, "cm", "meter")
        -> 1.0
    """

    _validate_number(value, "value")

    if not isinstance(from_unit, str):
        raise InvalidOperationError(
            "from_unit must be a string."
        )

    if not isinstance(to_unit, str):
        raise InvalidOperationError(
            "to_unit must be a string."
        )

    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in _LENGTH_FACTORS:
        raise InvalidOperationError(
            f"Unsupported source unit: {from_unit!r}"
        )

    if to_unit not in _LENGTH_FACTORS:
        raise InvalidOperationError(
            f"Unsupported target unit: {to_unit!r}"
        )

    # Convert the original value into meters.
    value_in_meters = value * _LENGTH_FACTORS[from_unit]

    # Convert meters into the target unit.
    converted_value = (
        value_in_meters / _LENGTH_FACTORS[to_unit]
    )

    return converted_value