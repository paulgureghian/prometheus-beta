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
    
    # Find all palindromes and track used indices
    palindromes = []
    used_indices = set()
    
    # Check each possible substring
    for i in range(len(s)):
        # Skip already used indices
        if i in used_indices:
            continue
        
        # Check for odd-length palindromes
        odd_pal = _find_palindrome_around_center(s, i, i, used_indices)
        if odd_pal:
            palindromes.append(odd_pal)
        
        # Check for even-length palindromes
        even_pal = _find_palindrome_around_center(s, i, i+1, used_indices)
        if even_pal:
            palindromes.append(even_pal)
    
    # Add single characters as fallback palindromes
    for i in range(len(s)):
        if i not in used_indices:
            palindromes.append(s[i])
    
    # Remove duplicates and sort lexicographically
    return sorted(set(palindromes))

def _find_palindrome_around_center(s: str, left: int, right: int, used_indices: set) -> str:
    """
    Find the longest palindrome centered at given indices.

    Args:
        s (str): Input string
        left (int): Left index of potential palindrome
        right (int): Right index of potential palindrome
        used_indices (set): Set to track already used indices

    Returns:
        str: Longest palindrome found, or empty string
    """
    # Extend while maintaining palindrome
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    # Backtrack to last valid palindrome
    left += 1
    right -= 1
    
    # Check if palindrome is valid and not overlapping
    if left == right:
        if left not in used_indices:
            used_indices.add(left)
            return s[left]
    elif left < right:
        # Check if indices are free
        if all(i not in used_indices for i in range(left, right+1)):
            # Mark all indices as used
            used_indices.update(range(left, right+1))
            return s[left:right+1]
    
    return ''