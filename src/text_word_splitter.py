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
    
    def extract_words(s):
        words = []
        start = 0
        
        while start < len(s):
            # Quote handling
            if s[start] in '"\'':
                quote_end = start
                while quote_end + 1 < len(s) and s[quote_end + 1] in '"\'':
                    quote_end += 1
                quote_segment = s[start:quote_end+1]
                
                if len(words) and '"' in words[-1]:
                    words[-1] += quote_segment
                else:
                    words.append(quote_segment)
                
                start = quote_end + 1
                continue
            
            # Regular parsing
            end = start + 1
            
            # Collect word fragment
            while end < len(s):
                # Uppercase transition detection
                if s[end].isupper() and not s[end-1].isupper():
                    break
                
                # Punctuation detection (excluding quotes)
                if not s[end].isalnum() and s[end] not in '"\'':
                    break
                
                end += 1
            
            word_fragment = s[start:end]
            
            # Uppercase sequence handling
            if word_fragment.isupper() and len(word_fragment) > 1:
                words.extend(list(word_fragment))
            else:
                words.append(word_fragment)
            
            start = end
        
        # Special punctuation and quotation handling
        final_words = []
        for word in words:
            # Handle punctuation words
            if not word[0].isalnum() and word[0] not in '"\'':
                if final_words and (
                    not final_words[-1][0].isalnum() or 
                    '"' in final_words[-1]
                ):
                    final_words[-1] += word
                else:
                    final_words.append(word)
            else:
                final_words.append(word)
        
        return final_words
    
    return extract_words(text)