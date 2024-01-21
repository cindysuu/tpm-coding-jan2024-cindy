"""
file: type_token_ratio.py
---
Defines a feature that outputs the word type-token ratio.
"""

from features.word_count import *
  
"""
function: get_word_TTR
@param text: The message for which we are calculating the word type-token ratio.
Recall that the type-token ratio is equal to (# of unique words) / (# of total words).
The output of this function should be a number (specifically, a float).
Example: “Please, oh please can I go to the ball?” → 8 / 9 → 0.889
"""

def get_word_TTR(text):
    total_words = count_words(text)
    
    words = text.split()
    unique_words = len(set(words))

    if total_words == 0:
        return 0.0
    else:
        word_TTR = unique_words / total_words
        return float(word_TTR)
        # For less digits in the TTR float
        # return round(word_TTR, 3)