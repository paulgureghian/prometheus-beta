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
    
    # Compute all palindromic substrings 
    def compute_palindromes(s):
        """Helper to find all palindromic substrings"""
        pals = set()
        n = len(s)
        # All possible substrings
        for i in range(n):
            # Odd length palindromes
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                pals.add(s[left:right+1])
                left -= 1
                right += 1
            
            # Even length palindromes
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                pals.add(s[left:right+1])
                left -= 1
                right += 1
        
        # Add single characters as palindromes
        pals.update(set(s))
        return sorted(pals)
    
    # Compute all palindromes
    all_pals = compute_palindromes(s)
    
    # Greedy approach for non-overlapping palindromes
    result = []
    used = [False] * len(s)
    
    # Prioritize longer palindromes, then sort lexicographically
    for pal in sorted(all_pals, key=len, reverse=True):
        # Check if this palindrome can be used (non-overlapping)
        pal_indices = [s.index(pal) + i for i in range(len(pal))]
        
        # If no indices used, add palindrome
        if not any(used[idx] for idx in pal_indices):
            result.append(pal)
            # Mark indices as used
            for idx in pal_indices:
                used[idx] = True
    
    # If no palindromes, fall back to single characters
    if not result:
        result = list(s)
    
    return sorted(result)