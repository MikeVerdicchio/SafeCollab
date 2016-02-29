# Mike Verdicchio, mpv3ms
# CS 3240, Lab 1
# January 25, 2016
# lab1_fact.py

def factorial1(n):
    if n < 0:
        raise ValueError("You cannot take the factorial of a negative number!")
        return

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial1(n-1)

def factorial2(n):
    oxf = []
    for i in range(0, n):
        oxf.append(factorial1(i))
    return oxf


def test_fact1():
    print("Test case 1: n=0 & n=1")
    assert factorial1(0) == 1, "factorial1(0) != 1"
    assert factorial1(1) == 1, "factorial1(0) != 1"
    print()

    print("Test case 2: n=5")
    assert factorial1(5) == 120, "factorial1(5) != 120"
    print()

    print("Test case 3: n is a negative number")
    try:
        factorial1(-1)
    except ValueError:
        print("You cannot take the factorial of a negative number!")

if __name__ == "__main__":
    test_fact1()
    print("Jisu")
