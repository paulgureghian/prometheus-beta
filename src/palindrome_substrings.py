def find_non_overlapping_palindromes(s: str) -> list[str]:
    """
    Find and return all non-overlapping palindromic substrings of an input string,
    sorted in lexicographic order.

    Args:
        s (str): Input string to find palindromic substrings in.

    Returns:
        list[str]: A list of unique non-overlapping palindromic substrings,
                   sorted lexicographically.

    Examples:
        >>> find_non_overlapping_palindromes("aabaa")
        ['aa', 'aba']
        >>> find_non_overlapping_palindromes("abcd")
        ['a', 'b', 'c', 'd']
    """
    # Input validation
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty list
    if not s:
        return []
    
    # Find all palindromes 
    palindromes = []
    n = len(s)
    
    # Greedy approach to find non-overlapping palindromes
    used = [False] * n
    
    # Find all palindromes and track used indices
    for length in range(len(s), 0, -1):
        for start in range(n - length + 1):
            # Skip if current characters are already used
            if any(used[i] for i in range(start, start + length)):
                continue
            
            # Check if substring is a palindrome
            substring = s[start:start+length]
            if _is_palindrome(substring):
                # Mark characters as used
                for i in range(start, start + length):
                    used[i] = True
                palindromes.append(substring)
    
    # If no palindromes found, return single characters
    if not palindromes:
        palindromes = list(s)
    
    # Sort lexicographically and remove duplicates
    return sorted(set(palindromes))

def _is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.

    Args:
        s (str): String to check

    Returns:
        bool: True if string is a palindrome, False otherwise
    """
    return s == s[::-1] and len(s) > 0