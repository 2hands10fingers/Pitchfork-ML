"""
This is where we will process that parts of speech per sentence and identify the trends.
"""

from json import load
import nltk

with open('reviews_sentences.json', 'r') as reviews_file:
    the_data = load(reviews_file)

    for sentence in the_data: print(nltk.pos_tag(sentence))
