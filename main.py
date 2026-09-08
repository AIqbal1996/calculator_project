"""
Demonstration program for the calculator_tools package.

This module imports functions from different modules
and demonstrates their functionality.
"""

from calculator_tools.arithmetic import (
    add,
    subtract,
    multiply,
    divide,
)

from calculator_tools.statistics import (
    calculate_percentage,
    calculate_average,
)

from calculator_tools.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    convert_units,
)

from calculator_tools.exceptions import InvalidOperationError


def main():
    """
    Run demonstrations of all calculator_tools functionality.
    """

    print("=" * 60)
    print("CALCULATOR TOOLS PACKAGE DEMONSTRATION")
    print("=" * 60)

    # ---------------------------------------------------------
    # 1. BASIC ARITHMETIC
    # ---------------------------------------------------------

    print("\n1. BASIC ARITHMETIC")
    print("-" * 60)

    result = add(10, 5)
    print(f"10 + 5 = {result}")

    result = subtract(10, 5)
    print(f"10 - 5 = {result}")

    result = multiply(10, 5)
    print(f"10 * 5 = {result}")

    result = divide(10, 5)
    print(f"10 / 5 = {result}")

    # ---------------------------------------------------------
    # 2. PERCENTAGE
    # ---------------------------------------------------------

    print("\n2. PERCENTAGE CALCULATION")
    print("-" * 60)

    result = calculate_percentage(25, 100)
    print(f"25 is {result}% of 100")

    result = calculate_percentage(50, 200)
    print(f"50 is {result}% of 200")

    # ---------------------------------------------------------
    # 3. AVERAGE
    # ---------------------------------------------------------

    print("\n3. AVERAGE CALCULATION")
    print("-" * 60)

    numbers = [10, 20, 30, 40, 50]

    result = calculate_average(numbers)

    print(f"Numbers: {numbers}")
    print(f"Average: {result}")

    # ---------------------------------------------------------
    # 4. TEMPERATURE CONVERSION
    # ---------------------------------------------------------

    print("\n4. TEMPERATURE CONVERSION")
    print("-" * 60)

    result = celsius_to_fahrenheit(0)
    print(f"0°C = {result}°F")

    result = celsius_to_fahrenheit(100)
    print(f"100°C = {result}°F")

    result = fahrenheit_to_celsius(32)
    print(f"32°F = {result}°C")

    result = fahrenheit_to_celsius(212)
    print(f"212°F = {result}°C")

    # ---------------------------------------------------------
    # 5. UNIT CONVERSION
    # ---------------------------------------------------------

    print("\n5. UNIT CONVERSION")
    print("-" * 60)

    result = convert_units(
        1,
        "kilometer",
        "meter"
    )

    print(f"1 kilometer = {result} meters")

    result = convert_units(
        100,
        "centimeter",
        "meter"
    )

    print(f"100 centimeters = {result} meters")

    result = convert_units(
        1,
        "mile",
        "kilometer"
    )

    print(f"1 mile = {result} kilometers")

    result = convert_units(
        12,
        "inch",
        "foot"
    )

    print(f"12 inches = {result} feet")

    # ---------------------------------------------------------
    # 6. ERROR HANDLING
    # ---------------------------------------------------------

    print("\n6. ERROR HANDLING")
    print("-" * 60)

    # Division by zero
    try:
        divide(10, 0)

    except InvalidOperationError as error:
        print(f"Division error handled: {error}")

    # Invalid data type
    try:
        add("10", 20)

    except InvalidOperationError as error:
        print(f"Data type error handled: {error}")

    # Percentage with zero
    try:
        calculate_percentage(10, 0)

    except InvalidOperationError as error:
        print(f"Percentage error handled: {error}")

    # Empty average
    try:
        calculate_average([])

    except InvalidOperationError as error:
        print(f"Average error handled: {error}")

    # Unsupported unit
    try:
        convert_units(
            10,
            "meter",
            "banana"
        )

    except InvalidOperationError as error:
        print(f"Unit conversion error handled: {error}")

    # Invalid temperature input
    try:
        celsius_to_fahrenheit("hot")

    except InvalidOperationError as error:
        print(f"Temperature error handled: {error}")

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()