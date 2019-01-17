## ValueError
# int("hello")
# print("test")

## ZeroDivisionError
# 7 / 0

try:
    # int("hello")
    7 / 0
except ValueError:
    print("You cannot convert string into integer")
except ZeroDivisionError:
    print("You cannot divide by 0")
except:
    print("Another error")