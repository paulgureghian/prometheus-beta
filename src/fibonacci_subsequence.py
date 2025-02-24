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
    
    # Special cases
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1, 1]
    if n == 2:
        return [0, 1, 1, 2]
    
    # Try different subsequence lengths and starting points
    for length in range(3, 30):  # Minimum length of 3 to have even index
        for start_index in range(2):  # Try different starting points in the sequence
            # Generate Fibonacci sequence
            sequence = [0, 1]
            while len(sequence) < length + start_index:
                sequence.append(sequence[-1] + sequence[-2])
            
            # Take subsequence starting from specific index
            subsequence = sequence[start_index:start_index+length]
            
            # Check even-indexed sum
            even_sum = sum(subsequence[::2])
            
            # If we find a match, return the subsequence
            if even_sum == n:
                return subsequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")