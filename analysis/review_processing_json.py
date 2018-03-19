# import nltk
# import re
# from nltk.tokenize import word_tokenize, sent_tokenize

import sqlite3
import statistics
import re
from nltk import sent_tokenize
import json

database = 'database.sqlite'
folder = '' # Wherever you're extracting your DB from. *IMPORTANT*
filepath = f'/{folder}/{database}'
conn = sqlite3.connect(filepath)

print('Connection Established!')

cursor = conn.cursor()
content = cursor.execute("SELECT * FROM 'content';")


reviews = []


for review in content:
    reviews_parsed = []
    reviews_parsed.append(sent_tokenize(review[1]))
    for i in reviews_parsed:

        stored_parsed_review = {
            "length": len(i),
            "review_sentences": i,
        }

        reviews.append(stored_parsed_review)

print('Parsing sentences for words. This will take a while.')

reviews_sent_lengths = [ i["length"] for i in reviews ]
review_sent_word_length = []
review_sentences_list = []

for i in reviews:
    review_sentences = (i['review_sentences'])

    for review_sentence in review_sentences:
        punctuations = ['(', ')', '?', ':', ';', ',',
                        '.', '!', '/', '"', "'"
                        ]
        other_filter = ['”', "’", '“', '’re', '’s', '’ve', '']

        keep_hyphenations_and_quotes = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*",
                                                  str(review_sentence))
        remove_punctuation = [''.join(x for x in par if x not in punctuations) for par in keep_hyphenations_and_quotes]
        clear_empty_strings = list(filter(None, remove_punctuation))
        clear_spec_chars_contracts = list(filter(lambda x: x not in other_filter, clear_empty_strings))

        print(clear_spec_chars_contracts)
        review_sentences_list.append(clear_spec_chars_contracts)
        review_sent_word_length.append(len(clear_spec_chars_contracts))

print('Saving to reviews_parsed.json.\n')
with open ('reviews_parsed.json', 'w') as file:
    json.dump(reviews, file)

print('Saving to reviews_sentences.json\n')
with open ('reviews_sentences.json', 'w') as outfile:
    json.dump(review_sentences_list, outfile)


'''
CURRENT STATS:
Word average per sentence: 28.03303836579362
Word standard deviation per sentence: 17.183635667578145
Sentence average length: 23.543848203120753
Sentence standard deviation: 10.147592013072698

Which means 11-45 words for 13-33 sentences
Which means anywhere from 143 - 1,485 words per review

'''


print(f"Word average per sentence: {statistics.mean(review_sent_word_length)}")
print(f"Word standard deviation per sentence: {statistics.stdev(review_sent_word_length)}")
print(f"Sentence average length: {statistics.mean(reviews_sent_lengths)}")
print(f"Sentence standard deviation: {statistics.stdev(reviews_sent_lengths)}")
print(f"Which means 11-45 words for 13-33 sentences")
print('Which means anywhere from 143 - 1,485 words per review')
