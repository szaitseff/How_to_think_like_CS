#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     17.01.2018
# Copyright:   (c) admin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno    # Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """Run the suite of tests for the functions defined below in the file"""
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday") == "Thursday"))
    test(day_num("Halloween") == None)

    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)

    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)

    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)

    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)

    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)

    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)

    test(is_even(8) == True)
    test(is_even(25) == False)
    test(is_even(0) == True)
    test(is_even(-10) == True)

    test(is_odd(0) == False)
    test(is_odd(25) == True)
    test(is_odd(-5) == True)
    test(is_odd(10) == False)

    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))

    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

    test(f2c(212) == 100)           # Boiling point of water
    test(f2c(32) == 0)              # Freezing point of water
    test(f2c(-40) == -40)           # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)

    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)

    test(mysum([1, 2, 3, 4]) == 10)
    test(mysum([1.25, 2.5, 1.75]) == 5.5)
    test(mysum([1, -2, 3]) == 2)
    test(mysum([]) == 0)
    test(mysum(range(11)) == 55)    # 11 is not included in the list

    test(sum_to(4) == 10)
    test(sum_to(1000) == 500500)



def absolute_value(x):
    """ The function returns the absolute value of a number.
    """
    if x < 0:
        return -x
    return x


def turn_clockwise(x):
    """ The four compass points can be abbreviated by single-letter strings
        as “N”, “E”, “S”, and “W”. Write a function turn_clockwise that
        takes one of these four compass points as its parameter, and returns
        the next compass point in the clockwise direction. For all other cases
        the function should return the value None.
    """
    if x == "N":
        return "E"
    if x == "E":
        return "S"
    if x == "S":
        return "W"
    if x == "W":
        return "N"
    return None


def day_name(x):
    """ Write a function day_name that converts an integer number 0 to 6
        into the name of a day. Assume day 0 is “Sunday”. Once again,
        return None if the arguments to the function are not valid.
    """
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday",
            "Friday","Saturday"]
    if x < 0 or x > 6:
        return None
    return days[x]


def day_num(day):
    """ Write the inverse function day_num, which is given a day name
        and returns its number.
    """
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday",
            "Friday","Saturday"]
    for i in [0,1,2,3,4,5,6]:
        if days[i] == day:
            return i
    return None


def day_add(day, delta):
    """ Write a function that helps answer questions like “Today is Wednesday.
        I leave on holiday in 19 days time. What day will that be?”
        So the function must take a day name and a delta argument — the number
        of days to add — and should return the resulting day name.
    Hint: use 'day_name' and 'day_num' functions to help you write this one."""

    a = (day_num(day) + delta) % 7    # day number to leave on holiday
    b = day_name(a)                   # day name to leave on holiday
    return b


def days_in_month(month):
    """ Write a function 'days_in_month' which takes the name of a month,
        and returns the number of days in the month. Ignore leap years.
    """
    months = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]
    nod = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days in a month
    for i in range(12):
        if months[i] == month:
            return nod[i]
    return None


def to_secs(h, m, s):
    """ Write a function to_secs that converts hours, minutes and seconds
        to a total number of seconds."""
    whole_mins = h * 60 + m
    total_secs = whole_mins * 60 + s
    return int(total_secs)


def hours_in(s):
    """ Write a function thar returns the whole integer number of hours
        represented by a total number of seconds. """
    whole_hrs = s // 3600
    return whole_hrs


def minutes_in(s):
    """ Write a function that returns the whole integer number of left over
    minutes in a total number of seconds, once the hours have been taken out.
    """
    a = s // 60             # number of whole minutes
    b = (s // 3600) * 60    # number of minutes in the whole hours
    left_minutes = a - b
    return left_minutes


def seconds_in(s):
    """ Write a function that returns the left over seconds represented
        by a total number of seconds."""
    c = (s // 60) * 60       # number of seconds in the whole minutes
    left_seconds = s - c
    return left_seconds


def compare(a, b):
    """ Write a compare function that returns 1 if a > b, 0 if a == b,
        and -1 if a < b """
    if a > b:
        return 1
    elif a == b:
        return 0
    return -1


def hypotenuse(x, y):
    """ Write a function called hypotenuse that returns the length
    of the hypotenuse of a right triangle given the lengths of the two legs
    as parameters.
    """
    h = (x**2 + y**2)**0.5  # squared hypothenuse = sum of squared legs
    return h


def slope(x1, y1, x2, y2):
    """ Write a function slope(x1, y1, x2, y2) that returns the slope
    of the line through the points (x1, y1) and (x2, y2).
    """
    dx = x2 - x1       # find differences in coordinates
    dy = y2 - y1
    s = dy / dx        # find slope
    return s


def intercept(x1, y1, x2, y2):
    """ Use a call to slope in a new function named intercept(x1, y1, x2, y2)
    that returns the y-intercept of the line through the points (x1, y1)
    and (x2, y2). """
    y0 = y2 - slope(x1, y1, x2, y2) * x2     # note that x0 = 0
    return y0


def is_even(n):
    """ Write a function called is_even(n) that takes an integer as an argument
    and returns True if the argument is an even number and False if it is odd.
    """
    if n % 2 == 0:
        return True
    return False


def is_odd(n):
    """ Now write the function is_odd(n) that returns True when n is odd
    and False otherwise. Finally, modify it so that it uses a call to
    is_even to determine if its argument is an odd integer, and ensure
    that its test still pass.
    """
    if not is_even(n):
        return True
    return False


def is_factor(f, n):
    """ Write a function is_factor(f, n) that passes relevant tests
    in the tests section of the file.
    """
    if n % f == 0:
        return True
    return False


def is_multiple(m, n):
    """ Write is_multiple to satisfy the unit tests above.
    Can you find a way to use is_factor in your definition of is_multiple?
    """
    if is_factor(n, m):
        return True
    return False


def f2c(t):
    """ Write the function f2c(t) designed to return the integer value
    of the nearest degree Celsius for given temperature in Fahrenheit.
    """
    tc = (t - 32) / 1.8   # Fahrenheit to Celsius conversion formula
    return round(tc)


def c2f(t):
    """ Now do the opposite: write the function c2f, which converts
    Celsius to Fahrenheit.
    """
    tf = 32 + t * 1.8
    return round(tf)


def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total


def sum_to(n):
    """ Return the sum of 1+2+3...n """
    ss = 0
    for v in range(n+1):
        ss = ss + v
    return ss


test_suite()   # Here is the call to run the tests
