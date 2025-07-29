def fibonacci_dp(n: int) -> int:
    """
    Calculates the nth Fibonacci number using bottom-up dynamic programming (tabulation).
    
    This function avoids recursion and builds the Fibonacci sequence
    from the base cases up to the desired value. It uses a list to
    store intermediate results (memoization table).

    Parameters:
        n (int): The index of the Fibonacci number to compute (0-based).

    """
    
    # Edge case: the 0th Fibonacci number is 0
    if n == 0:
        return 0

    # Create a list to store Fibonacci values from 0 to n
    dp_mem = [0] * (n + 1)
    
    # Base cases
    dp_mem[1] = 1

    # Fill dp_mem from 2 to n using the recurrence relation:
    # F(n) = F(n-1) + F(n-2)
    for i in range(2, n + 1):
        dp_mem[i] = dp_mem[i - 1] + dp_mem[i - 2]

    return dp_mem[n]



# print(fibonacci_dp(1))
# print(fibonacci_dp(5))
# print(fibonacci_dp(10))