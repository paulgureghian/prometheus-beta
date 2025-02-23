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
    
    def parse_complex_text(s):
        words = []
        current_word = ""
        quote_accumulator = ""
        
        # Look ahead strategy
        def look_ahead_collect(start_index):
            collected_word = s[start_index]
            index = start_index + 1
            while index < len(s):
                # Preserve uppercase character sequences
                if s[index].isupper() and (not collected_word or collected_word[-1].isupper()):
                    collected_word += s[index]
                # Handle punctuation and word boundaries
                elif not s[index].isalnum() and s[index] not in '"\'':
                    collected_word += s[index]
                    break
                # Normal character progression
                else:
                    collected_word += s[index]
                index += 1
            return collected_word
        
        i = 0
        while i < len(text):
            char = text[i]
            
            # Quotation handling
            if char in '"\'':
                quote_accumulator += char
                i += 1
                continue
            
            # Uppercase splitting strategy
            if char.isupper():
                # Complete previous word if needed
                if current_word:
                    words.append(current_word + quote_accumulator)
                    quote_accumulator = ""
                    current_word = ""
                
                # Look ahead and collect uppercase sequences or words
                word_segment = look_ahead_collect(i)
                
                # Handle uppercase sequences
                if len(word_segment) > 1 and word_segment.isupper():
                    words.extend(list(word_segment))
                else:
                    words.append(word_segment)
                
                i += len(word_segment)
                continue
            
            # Handle punctuation
            if not char.isalnum() and char not in '"\'':
                # Attach punctuation to previous word or create separate word
                if current_word:
                    words.append(current_word + quote_accumulator + char)
                else:
                    words.append(char)
                
                current_word = ""
                quote_accumulator = ""
                i += 1
                continue
            
            # Regular character progression
            current_word += char
            i += 1
        
        # Final word handling
        if current_word or quote_accumulator:
            words.append(current_word + quote_accumulator)
        
        return words
    
    return parse_complex_text(text)