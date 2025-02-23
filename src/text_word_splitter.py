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
    
    def split_complex_word(word):
        result = []
        current = word[0]
        
        for char in word[1:]:
            if char.isupper() and not current[-1].isupper():
                result.append(current)
                current = char
            else:
                current += char
        
        result.append(current)
        return result
    
    def process_text(s):
        words = []
        i = 0
        
        while i < len(s):
            char = s[i]
            
            # Quotation mark handling
            if char in '"\'':
                quote_end = i
                while quote_end + 1 < len(s) and s[quote_end + 1] in '"\'':
                    quote_end += 1
                quote_segment = s[i:quote_end+1]
                
                if words and '"' in words[-1]:
                    words[-1] += quote_segment
                else:
                    words.append(quote_segment)
                
                i = quote_end + 1
                continue
            
            # Detect word or word fragment
            if char.isalpha():
                # Complex word collection
                fragment = char
                next_index = i + 1
                
                while next_index < len(s):
                    next_char = s[next_index]
                    
                    # Break conditions
                    if next_char.isupper() and not fragment[-1].isupper():
                        break
                    if not next_char.isalnum() and next_char not in '"\'':
                        break
                    
                    fragment += next_char
                    next_index += 1
                
                # Handle uppercase sequences and split words
                if fragment.isupper() and len(fragment) > 1:
                    words.extend(list(fragment))
                else:
                    words.extend(split_complex_word(fragment))
                
                i = next_index
                continue
            
            # Punctuation handling
            if not char.isalnum() and char not in '"\'':
                words.append(char)
                i += 1
                continue
            
            i += 1
        
        return words
    
    return process_text(text)