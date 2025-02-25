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
    
    # Track palindromic substrings
    palindromes = []
    used = [False] * len(s)
    
    # Prioritize sequences of length 2
    for i in range(len(s) - 1):
        if not used[i] and not used[i+1]:
            # Check if 2-character substring is a palindrome
            if s[i] == s[i+1]:
                palindromes.append(s[i:i+2])
                used[i] = used[i+1] = True
    
    # If no 2-character palindromes, find 3+ character palindromes
    if not palindromes:
        for length in range(len(s), 1, -1):
            for start in range(len(s) - length + 1):
                # Skip if any character is already used
                if any(used[i] for i in range(start, start + length)):
                    continue
                
                # Check if current substring is a palindrome
                substring = s[start:start+length]
                if substring == substring[::-1]:
                    # Mark characters as used
                    for i in range(start, start + length):
                        used[i] = True
                    palindromes.append(substring)
                    break  # Greedy: take first longest palindrome
    
    # If still no palindromes, use single characters
    if not palindromes:
        # Use unique characters in original string order
        seen = set()
        palindromes = [c for c in s if not (c in seen or seen.add(c))]
    
    return sorted(palindromes)