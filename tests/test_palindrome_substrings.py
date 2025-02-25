import pytest
from src.palindrome_substrings import find_non_overlapping_palindromes

def test_basic_palindromes():
    """Test basic palindrome finding"""
    assert find_non_overlapping_palindromes("aabaa") == ["aa", "aba"]
    assert find_non_overlapping_palindromes("abcd") == ["a", "b", "c", "d"]

def test_empty_string():
    """Test empty string input"""
    assert find_non_overlapping_palindromes("") == []

def test_single_character():
    """Test single character input"""
    assert find_non_overlapping_palindromes("a") == ["a"]
    assert find_non_overlapping_palindromes("z") == ["z"]

def test_multiple_palindromes():
    """Test string with multiple non-overlapping palindromes"""
    assert find_non_overlapping_palindromes("racecar") == ["r", "aceca"]
    assert find_non_overlapping_palindromes("madam") == ["ada", "m"]

def test_no_palindromes():
    """Test string with no palindromes longer than single character"""
    assert find_non_overlapping_palindromes("abc") == ["a", "b", "c"]

def test_complex_palindromes():
    """Test more complex palindrome scenarios"""
    assert find_non_overlapping_palindromes("abbaxyzzyx") == ["abba", "xyzzyx"]
    assert find_non_overlapping_palindromes("bananas") == ["an", "aa"]

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert find_non_overlapping_palindromes("aaaa") == ["aa", "aa"]

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        find_non_overlapping_palindromes(123)
    with pytest.raises(TypeError):
        find_non_overlapping_palindromes(None)