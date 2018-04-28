from collections import Counter
import sqlite3
import re
import statistics
from nltk import sent_tokenize, pos_tag
from json import dump, load


database = 'database.sqlite'
folder = 'Volumes/TonoDrive'
filepath = f'/{folder}/{database}'
conn = sqlite3.connect(filepath)

print('Connection Established!')

cursor = conn.cursor()
content = cursor.execute("SELECT * FROM 'content';")

# ---- BREAKING UP REVIEWS INTO SENTENCES
print("Breaking up reviews in sentences...")
reviews = []
review_sentences_list = []
for review in content:
    reviews_parsed = []
    reviews_parsed.append(sent_tokenize(review[1]))
    for i in reviews_parsed:

        stored_parsed_review = {
            "length": len(i),
            "review_sentences": i,
        }

        reviews.append(stored_parsed_review)

review_sent_lengths = [i["reviews"] for i in reviews]

print('Saving to reviews_parsed.json.\n')
with open('reviews_parsed.json', 'w') as file:
    dump(reviews, file)


# ---- WORD TOKENIZATION
print('Parsing sentences for words. This will take a while.')

review_sent_word_length = []
review_sentences_list = []
print("Opening...")
with open('reviews_parsed.json', 'rb') as reviews:
    # reviews_sent_lengths = [i["length"] for i in load(reviews)]
    for review in load(reviews):
        review_sentences = review["review_sentences"]

        # print(review_sentences)

        for review_sentence in review_sentences:
            punctuations = ['(', ')', '?', ':', ';', ',',
                            '.', '!', '/', '"', "'"
                                                        ]
            other_filter = ['”', "’", '“', '’re', '’s', '’ve', '', '’t']

            keep_hyphenations_and_quotes = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*",
                                                  str(review_sentence))
            remove_punctuation = [''.join(x for x in par if x not in punctuations) for par in keep_hyphenations_and_quotes]
            clear_empty_strings = list(filter(None, remove_punctuation))
            clear_spec_chars_contracts = list(filter(lambda x: x not in other_filter, clear_empty_strings))
            review_sentences_list.append(clear_spec_chars_contracts)
            review_sent_word_length.append(len(clear_spec_chars_contracts))

print('Saving to reviews_sentences_words.json\n')
with open('reviews_sentences_words.json', 'w') as outfile:
    dump(review_sentences_list, outfile)

#
# # ---- BREAKING UP INTO PARTS OF SPEECH
# # --- SECTION 1

pos_list = []
with open('reviews_sentences_words.json', 'r') as reviews_file:
    the_data = load(reviews_file)
    print("Grabbing the data and turning it into parts of speech.")
    for sentence in the_data:
        x = pos_tag(sentence)
        pos_list.append(x)

print('Saving all the data to parts_of_speech_review_sentences.json')
with open('parts_of_speech_review_sentences.json', 'w') as outfile:
    dump(pos_list, outfile)

# --- SECTION 2
# ---- Determinging the average number of POS!

parts_of_speech = []
with open('parts_of_speech_review_sentences.json', 'r') as pos:
    pos_data = load(pos)

    for sentence in pos_data:
        pos_sent_list = [part_of_speech[1] for part_of_speech in sentence]
        count_parts_speech_per_sentence = Counter(pos_sent_list)
        parts_of_speech.append(count_parts_speech_per_sentence)


total = sum(map(Counter, parts_of_speech), Counter())
N = float(len(parts_of_speech))
average_pos_per_sentence = {k: v/N for k, v in total.items()}

print(f"Word average per sentence: {statistics.mean(review_sent_word_length)}")
print(f"Word standard deviation per sentence: {statistics.stdev(review_sent_word_length)}")
# print(f"Sentence average length: {statistics.mean(reviews_sent_lengths)}")
# print(f"Sentence standard deviation: {statistics.stdev(reviews_sent_lengths)}")
print(f"Which means 11-45 words for 13-33 sentences")
print('Which means anywhere from 143 - 1,485 words per review')
print(average_pos_per_sentence)

'''
Word average per sentence: 28.03303836579362
Word standard deviation per sentence: 17.183635667578145
Sentence average length: 23.543848203120753
Sentence standard deviation: 10.147592013072698

Which means 11-45 words for 13-33 sentences
Which means anywhere from 143 - 1,485 words per review

{'SYM': 0.0013462897363304253, ':': 0.14264667168542544, 
'NN': 4.368463105195339, 
'RB': 1.5308884588561849, 
'VBD': 0.5519372254885208, 
'DT': 2.897746638894149, 
'NNP': 2.781598551641642, 
'JJ': 2.6825873702781715, 
'IN': 3.5272767999408834, 
'CC': 1.1208058340761404, 
'NNS': 1.6067840994637934, 
'TO': 0.5763367063702828, 
'WRB': 0.12574761801395706, 
'VBG': 0.6693207587254816, 
'VB': 0.7046083289842555, 
'PRP$': 0.5719745428849857, 
'PRP': 0.814507599724738, 
'VBP': 0.5706328716383169, 
'VBN': 0.457687706966068, 
'VBZ': 0.9713399624054941, 
'WDT': 0.19611492649673704, 
'JJS': 0.0986647946388572, 
'RBR': 0.08869347545965518, 
'CD': 0.30735355923905766, 
'RP': 0.14605973554528198, 
'FW': 0.005653031345689332, 
'PDT': 0.02695812415423908, 
'EX': 0.034705640561423605, 
'WP': 0.09130523136323959, 
'MD': 0.17987169835720324, 
'NNPS': 0.033624913980630056, 
'JJR': 0.09864632068021116, 
'RBS': 0.03713034763371682, 
'$': 0.00100913999104013, 
"''": 6.0040365599641606e-05, 
'WP$': 0.009266999505821607, 
'UH': 0.0031220990111813633, 
'POS': 0.00037178841775162687, 
'LS': 4.849414144586437e-05, 
'#': 7.851432424568518e-05, 
')': 4.387565178435348e-05, 
'(': 1.847395864604357e-05}
'''
