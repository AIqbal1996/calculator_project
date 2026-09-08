"""
calculator_tools

A reusable Python package providing arithmetic,
statistics, temperature conversion, and unit conversion.
"""

from .arithmetic import (
    add,
    subtract,
    multiply,
    divide,
)

from .statistics import (
    calculate_percentage,
    calculate_average,
)

from .converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    convert_units,
)

from .exceptions import InvalidOperationError


__version__ = "1.0.0"


__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "calculate_percentage",
    "calculate_average",
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "convert_units",
    "InvalidOperationError",
]