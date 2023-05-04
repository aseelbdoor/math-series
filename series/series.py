def fibonacci(n):
    '''
    This function calculate the Fibonacci for integer
    parameter n : int,
    return int
    '''
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n):
    '''
    This function calculate the Lucas for integer
    parameter n : int,
    return int
    '''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


def sum_series(n, a=0, b=1):
    '''
    This function calculate the sumation series for integer
    parameter n / a / b : int,
    return int
    '''
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-1, a, b)+sum_series(n-2, a, b)
