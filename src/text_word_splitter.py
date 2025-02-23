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
    
    # Regex pattern to split on capital letters and punctuation (except quotes)
    pattern = r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|(?<=[a-zA-Z])(?=[^\w\s"\']+)'
    
    # Special handling to preserve punctuation with words
    words = re.split(pattern, text)
    
    # Further process words to handle punctuation and capital letter sequences
    processed_words = []
    i = 0
    while i < len(words):
        current_word = words[i]
        
        # Handle sequences of capital letters
        if current_word.isupper() and len(current_word) > 1:
            processed_words.extend(list(current_word))
            i += 1
            continue
        
        # Look ahead to include adjacent punctuation
        while i + 1 < len(words) and re.match(r'^[^\w\s"\']+$', words[i+1]):
            current_word += words[i+1]
            i += 1
        
        processed_words.append(current_word)
        i += 1
    
    return processed_words