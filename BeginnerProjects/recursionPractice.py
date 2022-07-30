# Trust the natural recursion


def fac(n):
    """
    To calculate the factorial of n
    """
    if  n ==0:
        return 1

    return n * fac(n-1)



# 1,1,2,3,5,...

def fib(n: int) -> int:
    """
    Gives the nth fib number
    """
    if n == 1 or n==2:
        return 1

    return fib(n-2) + fib(n-1)



    

