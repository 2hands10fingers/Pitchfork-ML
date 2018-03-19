"""
This is where we will process that parts of speech per sentence and identify the trends.
"""
from json import load, dump
import nltk



# --- SECTION 1

pos_list = []
with open('reviews_sentences.json', 'r') as reviews_file:
    the_data = load(reviews_file)
    print("Grabbing the data and turning it into parts of speech.")
    for sentence in the_data:
        x = nltk.pos_tag(sentence)
        pos_list.append(x)


print('Saving all the data to parts_of_speech_review_sentences.json')
with open('parts_of_speech_review_sentences.json', 'w') as outfile:
    dump(pos_list, outfile)


'''
Use uncomment the below code (SECTION 2) and comment out SECTION 1 when the top section is ready
'''


# --- SECTION 2

# with open('parts_of_speech_review_sentences.json', 'r') as pos:
#     pos_data = load(pos)
#     for sentence in pos_data:
#         pos_sent_list = [part_of_speech[1] for part_of_speech in sentence]
# 
#         print(pos_sent_list)
