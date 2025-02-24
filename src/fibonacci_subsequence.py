def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers in the subsequence.
    
    Returns:
        list: A Fibonacci subsequence satisfying the condition.
    
    Raises:
        ValueError: If no valid subsequence can be found.
    """
    # Handle invalid input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if n == 0:
        return [0]
    
    # Try different subsequence lengths
    for length in range(2, 20):  # Reasonable upper limit
        # Generate initial Fibonacci sequence
        sequence = [0, 1]
        while len(sequence) < length:
            sequence.append(sequence[-1] + sequence[-2])
        
        # Check even-indexed sum
        even_sum = sum(sequence[::2])
        
        # If we find a match, return the subsequence
        if even_sum == n:
            return sequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")