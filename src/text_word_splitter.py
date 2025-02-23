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
    
    # Complex regex pattern for splitting
    words = []
    current_word = ""
    i = 0
    
    while i < len(text):
        char = text[i]
        
        # Handle quotation marks without breaking words
        if char in '"\'':
            quote_start = i
            while i + 1 < len(text) and text[i+1] in '"\'':
                i += 1
            quote_end = i
            quote_part = text[quote_start:quote_end+1]
            
            if current_word:
                current_word += quote_part
            else:
                current_word = quote_part
            
            i += 1
            continue
        
        # Splitting logic for capital letters and punctuation
        if char.isupper() and current_word and not current_word[-1].isupper():
            # Start of a new word when capital letter follows a lowercase
            words.append(current_word)
            current_word = char
        elif not char.isalnum() and char not in '"\'':
            # Punctuation mark
            if current_word:
                words.append(current_word)
                current_word = char
            else:
                current_word = char
        elif char.isupper():
            # Handle sequences of capital letters
            if current_word and current_word.isupper():
                current_word += char
            else:
                if current_word:
                    words.append(current_word)
                current_word = char
        else:
            current_word += char
        
        i += 1
    
    # Append the last word
    if current_word:
        words.append(current_word)
    
    return words