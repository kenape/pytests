def fizzBuzz(valuePassed):
    if isMultiple(valuePassed, 3) and isMultiple(valuePassed, 5):
        return "FizzBuzz"
    elif isMultiple(valuePassed, 3):
        return "Fizz"
    elif isMultiple(valuePassed, 5):
        return "Buzz"
    else:
        return str(valuePassed)


def isMultiple(value, modulus):
    return value % modulus == 0


def checkFizzBuzz(value, expectedRetVal):
    returned = fizzBuzz(value)
    assert returned == expectedRetVal


def test_returns1WhenPassed1():
    checkFizzBuzz(1, "1")


def test_returns2WhenPassed2():
    checkFizzBuzz(2, "2")


def test_returnsFizzWhenPassed3():
    checkFizzBuzz(3, "Fizz")


def test_returnsBuzzWhenPassed5():
    checkFizzBuzz(5, "Buzz")


def test_returnsFizzWhenPassed6():
    checkFizzBuzz(6, "Fizz")


def test_returnsBuzzWhenPassed10():
    checkFizzBuzz(10, "Buzz")


def test_returnsFizzBuzzWhenPassed15():
    checkFizzBuzz(15, "FizzBuzz")
