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
        # Quotation mark preservation
        if char in '"\'':
            current_word += char
            continue
        
        # Uppercase sequence handling
        if char.isupper() and not current_word[-1].isupper():
            words.append(current_word)
            current_word = char
        elif char.isupper() and current_word.isupper() and len(current_word) == 1:
            current_word += char
        elif not char.isalnum() and char not in '"\'':
            # Punctuation handling
            if current_word[-1].isupper() and len(current_word) == 1:
                # Extend uppercase sequence
                current_word += char
            else:
                # Punctuation breaks the word, but preserves pattern
                words.append(current_word)
                current_word = char
        else:
            current_word += char
    
    # Append the last word
    words.append(current_word)
    
    # Special case for uppercase sequences
    processed_words = []
    for word in words:
        if word.isupper() and len(word) > 1:
            processed_words.extend(list(word))
        else:
            processed_words.append(word)
    
    return processed_words