#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is a power program


def main():
    # this function calculates the number with an exponent of 2
    counter = 0
    sum_number = 1
    # input
    number_as_string = input("Enter a positive integer: ")
    # process & output
    print("")
    try:
        number_as_int = int(number_as_string)
        number_as_int = number_as_int + 1
        if number_as_int < 0:
            print("That is not a positive integer.")
        else:
            for counter in range(number_as_int):
                sum_number = counter**2
                print("{0}² = {1} ".format(counter, sum_number))
    except Exception:
        print("That is not a integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
