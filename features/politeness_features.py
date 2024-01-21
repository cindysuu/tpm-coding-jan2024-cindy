"""
file: politeness_features.py
---
Defines a feature that calls the PolitenessStrategies from ConvoKit
and returns them as 21 columns (for each message).

Link to Politness Documentation: https://convokit.cornell.edu/documentation/politenessStrategies.html
Link to ConvoKit GitHub examples: https://github.com/CornellNLP/ConvoKit/tree/master/examples/politeness-strategies

You should follow the samples to create the appropriate imports, process the data, and call the function.
"""


"""
function: get_politeness_strategies
(Chat-level function)

This gets the politeness annotations of each message, with some fields 
including HASHEDGE, Factuality, Deference, Gratitude, Apologizing, etc.
"""

import convokit
import spacy

def get_politeness_strategies(text):
    politeness_model = convokit.PolitenessStrategies()
    spacy_nlp = spacy.load('en_core_web_sm', disable=['ner'])
    utterance = politeness_model.transform_utterance(text, spacy_nlp=spacy_nlp)
    politeness_strategies = utterance.meta['politeness_strategies']
    return politeness_strategies
