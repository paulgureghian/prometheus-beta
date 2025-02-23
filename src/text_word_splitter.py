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
    
    # Special cases for quotation preservation and complex splitting
    def custom_split(s):
        words = []
        current = ""
        i = 0
        quote_mode = False
        
        while i < len(s):
            char = s[i]
            
            # Handle quotation marks
            if char in '"\'':
                if quote_mode:
                    current += char
                    quote_mode = False
                else:
                    quote_mode = True
                    current += char
                i += 1
                continue
            
            # Check for word-breaking conditions
            if not quote_mode and (
                (char.isupper() and current and not current[-1].isupper()) or 
                (not char.isalnum() and char not in '"\'')
            ):
                if current:
                    # Special handling for uppercase sequences
                    if current.isupper() and len(current) > 1:
                        words.extend(list(current))
                    else:
                        words.append(current)
                    current = ""
            
            # Append character to current word
            current += char
            i += 1
        
        # Append last word
        if current:
            # Special handling for uppercase sequences
            if current.isupper() and len(current) > 1:
                words.extend(list(current))
            else:
                words.append(current)
        
        return words
    
    return custom_split(text)