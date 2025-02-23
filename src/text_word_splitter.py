import re

def split_text_to_words(text):
    """
    Split a text string into words based on specific rules.
    
    Rules:
    1. Words are separated by capital letters or punctuation (excluding quotes)
    2. Punctuation marks are included with the word they end
    3. Sequences of capital letters are treated as separate words
    4. Quotation marks do not break words
    
    Args:
        text (str): Input text string without spaces
    
    Returns:
        list: A list of words split according to the specified rules
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        return []
    
    words = []
    current_word = text[0]
    
    for char in text[1:]:
        if char.isupper() and not current_word[-1].isupper():
            # Split on capital letter transition from lowercase
            words.append(current_word)
            current_word = char
        elif not char.isalnum() and char not in '"\'':
            # Punctuation handling
            if current_word and current_word[-1].isupper() and len(current_word) == 1:
                # Extended uppercase sequence
                current_word += char
            else:
                # Start a new punctuation-based word
                if current_word:
                    words.append(current_word)
                current_word = char
        elif char.isupper() and current_word.isupper() and len(current_word) == 1:
            # Continue uppercase sequence
            current_word += char
        else:
            current_word += char
    
    # Append final word
    if current_word:
        words.append(current_word)
    
    return words