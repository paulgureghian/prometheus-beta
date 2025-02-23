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
    
    # Custom state machine for complex parsing
    def parse_words(s):
        words = []
        i = 0
        while i < len(s):
            # Quotation handling
            if s[i] in '"\'':
                quote_end = i
                while quote_end + 1 < len(s) and s[quote_end + 1] in '"\'':
                    quote_end += 1
                quote_segment = s[i:quote_end+1]
                
                # Attach to previous word or create new
                if words and ('"' in words[-1] or "'" in words[-1]):
                    words[-1] += quote_segment
                else:
                    words.append(quote_segment)
                
                i = quote_end + 1
                continue
            
            # Capital letter and word boundary detection
            current_word = s[i]
            next_boundary = i + 1
            
            # Look ahead for word boundaries
            while next_boundary < len(s):
                # Detect word split conditions
                is_break = (
                    (s[next_boundary].isupper() and not s[next_boundary-1].isupper()) or
                    (not s[next_boundary].isalnum() and s[next_boundary] not in '"\'')
                )
                
                if is_break:
                    break
                
                current_word += s[next_boundary]
                next_boundary += 1
            
            # Handle uppercase sequences
            if current_word.isupper() and len(current_word) > 1:
                words.extend(list(current_word))
            else:
                words.append(current_word)
            
            i = next_boundary
        
        return words
    
    return parse_words(text)