#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module converts fahrenheit to celsius."""

import decimal
decimal.getcontext().prec = 5

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')

def fahrenheit_to_celsius(degrees):
    """This function converts fahrenheit to celsius.

    Args:
        degrees (decimal): The degrees in Fahrenheit to be converted to celsius.

    Returns:
        decimal: Degrees in Celsius.

    Examples:

        >>>fahrenheit_to_celsius(212)
        Decimal('100')
    """
    celsius = ((decimal.Decimal(degrees) - 32)*5)/9
    return celsius

def celsius_to_kelvin(degrees):
    """This function converts celsius to kelvin.

    Args:
        degrees (decimal): The degrees in celsius to be converted to kelvin.

    Returns:
        decimal: Degrees in Kelvin.

    Examples:

        >>> celsius_to_kelvin(100)
        Decimal('373.15')
    """
    kelvin = ABSOLUTE_DIFFERENCE + decimal.Decimal(degrees)
    return kelvin

def fahrenheit_to_kelvin(degrees):
    """This function converts  fahrenheit to celsius to kelvin.

    Args:
        degrees (decimal): The degrees in fahrenheit to be converted to kelvin.

    Returns:
        decimal: Degrees in Kelvin.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """
    kelvin = celsius_to_kelvin(fahrenheit_to_celsius(degrees))
    return kelvin