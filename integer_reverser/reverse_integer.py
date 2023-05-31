#!/usr/bin/env python3

def reverser(x):
    '''
    Takes in an integer and return the digits in reverse order (can be negative)

    Args: 
        x (int): an integer input

    Returns:
        a string of the digits of x in reverse
    '''

    x = str(x)

    if x[0] == "-":
        return("-" + x[:0:-1])
    return(x[::-1])

def main():
    print(reverser(12345))
    print(reverser(-5124))

if __name__ == '__main__':
    main()

