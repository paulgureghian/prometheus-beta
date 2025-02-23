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
    
    # Complex regex-based strategy
    def advanced_split(s):
        # Regex to split on capital letters while preserving context
        words = []
        i = 0
        while i < len(s):
            # Detect quote sequences
            if s[i] in '"\'':
                quote_end = i
                while quote_end + 1 < len(s) and s[quote_end + 1] in '"\'':
                    quote_end += 1
                quote_segment = s[i:quote_end+1]
                
                # If we're in a quote segment, treat it specially
                if len(words) > 0 and '"' in words[-1]:
                    words[-1] += quote_segment
                else:
                    words.append(quote_segment)
                i = quote_end + 1
                continue
            
            # Handle uppercase sequences
            if s[i].isupper():
                if len(words) > 0 and words[-1].isupper() and len(words[-1]) == 1:
                    words[-1] += s[i]
                else:
                    words.append(s[i])
                i += 1
                continue
            
            # Detect word fragments
            word_fragment = ""
            start_fragment = i
            
            # Accumulate characters in the fragment
            while i < len(s) and (not s[i].isupper() or 
                                  (len(word_fragment) > 0 and word_fragment[-1].islower())):
                # Special handling for punctuation
                if not s[i].isalnum() and s[i] not in '"\'':
                    if word_fragment and word_fragment[-1] != s[i]:
                        break
                
                word_fragment += s[i]
                i += 1
            
            # Punctuation handling
            while i < len(s) and not s[i].isalnum() and s[i] not in '"\'':
                word_fragment += s[i]
                i += 1
            
            if word_fragment:
                words.append(word_fragment)
        
        return words
    
    return advanced_split(text)