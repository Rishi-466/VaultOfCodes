def convert_temperature(value: float, unit: str) -> float:
    """
    Converts temperature between Celsius and Fahrenheit.

    Parameters:
        value (float): The input temperature to convert.
        unit (str): The unit of the input temperature ('C' or 'F').

    Returns:
        float: The converted temperature, rounded to 2 decimal places.

    Raises:
        ValueError: If the unit is not 'C' or 'F'.
    """
    unit = unit.upper().strip()

    if unit == 'C':
        # Celsius to Fahrenheit
        result = (value * 9 / 5) + 32
    elif unit == 'F':
        # Fahrenheit to Celsius
        result = (value - 32) * 5 / 9
    else:
        raise ValueError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

    return round(result, 2)

# Example usage
if __name__ == "__main__":
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of temperature (C/F): ")
        converted = convert_temperature(temp, unit)
        new_unit = 'Fahrenheit' if unit.upper().strip() == 'C' else 'Celsius'
        print(f"Converted Temperature: {converted}° {new_unit}")
    except ValueError as e:
        print(f"Error: {e}")
