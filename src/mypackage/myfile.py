def factorial(n):
    """
    my great function that computes the factorial of an iteger
    :param n: (int) non negative integer argument of factorial
    :return: (int) factorial (n)
    """
    if type(n) is not int or n < 0:
        raise ValueError('n must be a positive integer')
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def addition(x, y):
    return x+y