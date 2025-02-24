import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_zero_input():
    """Test that input 0 returns [0]"""
    assert generate_fibonacci_subsequence(0) == [0]

def test_specific_inputs():
    """Test some known valid inputs"""
    # Various input cases
    test_cases = [
        (1, [0, 1, 1]),    # 0 + 1 = 1
        (2, [0, 1, 1, 2]), # 0 + 2 = 2
        (4, [0, 1, 1, 2, 3, 5]), # 0 + 2 + 3 = 4
    ]
    
    for n, expected in test_cases:
        result = generate_fibonacci_subsequence(n)
        assert sum(result[::2]) == n, f"Even-indexed sum not equal to {n}"

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(-1)
    
    # Non-integer input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(3.14)
    
    # Large input that cannot be generated
    with pytest.raises(ValueError, match="No Fibonacci subsequence found"):
        generate_fibonacci_subsequence(1000000)

def test_even_indexed_sum():
    """Verify that even-indexed sum is always correct"""
    for n in range(10):
        result = generate_fibonacci_subsequence(n)
        assert sum(result[::2]) == n, f"Failed for input {n}"

def test_subsequence_properties():
    """Check fundamental Fibonacci sequence properties"""
    for n in range(5):
        result = generate_fibonacci_subsequence(n)
        # Check that it follows Fibonacci recurrence
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2], \
                f"Not a valid Fibonacci sequence for input {n}"