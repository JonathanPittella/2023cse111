def deposit(amount):
    # In order for this program to work correctly and
    # for the bank records to be correct, we must not
    # allow someone to deposit a zero or negative amount.
    assert amount > 0
#different types of asserts ===
"""    
    assert temperature < 0

    assert len(given_name) > 0

    assert balance == 0

    assert school_year != "senior"
"""

#Exemple of test Pytest

def test_min():
    assert min(7, -3, 0, 2) == -3

"""
In the previous function, the assert statement will 
cause the computer to first call the min function and 
pass 7, −3, 0, and 2 as arguments to the min function. 
The min function will find the minimum value of its 
parameters and return that minimum value. Then the assert 
statement will compare the returned minimum value to −3. 
If the returned value is not −3, the assert statement 
will raise an exception which will cause pytest to print 
an error message.
"""

# Example 4

    # The variables e and f can be any floating-
    # point numbers from any calculation.
e = 7.135
f = 7.128

if abs(e - f) < 0.01:
    print(f"{e} and {f} are close enough so")
    print("we'll consider them to be equal.")
else:
    print(f"{e} and {f} are not close and")
    print("therefor not equal.")

#Bad exemple
    #def approx(expected_value, rel=None, abs=None, nan_ok=False):

#Good exemple
#    def test_function():
#        assert actual_value == approx(expected_value)

# Example 5

#    def test_sqrt():
#        assert math.sqrt(5) == approx(2.24, rel=0.01)
"""
Notice the rel named argument in line 4 of the previous 
example. The rel named argument causes approx to compute 
the tolerance relative to the expected value. This means 
that the assert statement in the previous example causes 
the computer to verify that the actual value returned 
from math.sqrt(5) is within 1% (0.01) of 2.24. When a 
programmer uses the rel named argument, the approx 
function uses code similar to example 6 to determine 
if the actual and expected values are equal.
"""

# Example 6

# Example 7

#def test_sqrt():
#    assert math.sqrt(5) == approx(2.24, abs=0.01)

    # Compute the tolerance.
#    tolerance = expected_value * rel

    # Use the tolerance to determine if the actual
    # and expected values are close enough to be
    # considered equal.
#    if abs(actual_value - expected_value) < tolerance:
#        return True
#    else:
#        return False


# weather.py

def cels_from_fahr(fahr):
    """Convert a temperature in Fahrenheit to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return cels

# test_weather.
#from weather import cels_from_fahr
from pytest import approx
from pytest import main

def test_cels_from_fahr():
    """Test the cels_from_fahr function by calling it and
    comparing the values it returns to the expected values.
    Notice this test function uses pytest.approx to compare
    floating-point numbers.
    """
    assert cels_from_fahr(-25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
main(["-v", "--tb=line", "-rN", __file__])