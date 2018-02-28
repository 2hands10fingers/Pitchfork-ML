import sqlite3
import nltk.corpus
import nltk
import numpy
import csv
import os
import pickle

from nltk.tokenize import word_tokenize, sent_tokenize
from pathlib import Path

FILENAMES = ['review_text', 'sentences_tokenized', 'sentences_words_tokenized', 'words_tagged1', 'words_tagged2']

# --- function junction

# Load from pickle file
def load(filestring):

    filepath = filestring + '.pkl'

    if Path(filepath).is_file():
        print(f'Loading {filepath}...')
        with open(filepath, 'rb') as f:
            pickle_list = pickle.load(f)
        print(f'{filepath} loaded.\n')
        return pickle_list

    else:
        print(f'No pickle file found at {filepath}!\n')
        return False

# Dump list into pickle file
def dump(filestring, this_list):

    filepath = filestring + '.pkl'
    print(f'Writing {filepath}...') 

    if Path(filepath).is_file():
        print(f'Removing previous version of {filepath}...')
        os.remove(filepath)
        
    with open(filepath, 'wb') as f:
        pickle.dump(this_list, f)

    f.close()

    print(f'Wrote {filepath}.\n')

def looper(loop):
	for i in loop: print(i)

database = 'database.sqlite'
folder = '' #designate where your DB is *IMPORTANT*

filepath = f'/{folder}/{database}'
conn = sqlite3.connect(filepath)

print('Connection Established!')

# ---- Querying of datbase to pull reviews. 
#-------- Change the table variable to get a new table(i.e., 'reviews', 'content', 'artists', 'years', 'genres', 'labels')

table = "content"
cursor = conn.cursor()
reviews = cursor.execute("SELECT * FROM '{}';".format(table))

review_list = load(FILENAMES[0])
if not review_list:
    review_list = [i[1] for i in reviews] #Reviews split up in list
    dump(FILENAMES[0], review_text)

sent_list = load(FILENAMES[1])
if not sent_list:
    #Reviews split up into 2D list of sentences
    sent_list = [sent_tokenize(str(i)) for i in review_text]
    dump(FILENAMES[1], sent_list)

words_list = load(FILENAMES[2])
if not words_list:
    # Reviews' sentences split up into 2D list of words
    words_list = [ word_tokenize(str(i)) for i in sent_tokenized]
    dump(FILENAMES[2], words_list)

'''
Had to split this into two loads/dumps due to MemoryError. May require
more splitting of lists in same fashion for slower machines.
'''
tagged1 = load(FILENAMES[3])
tagged2 = load(FILENAMES[4])
if not tagged1:
    # Reviews' words tagged (https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk)
    # tagged is a 2D list of tuples, tuples are split by word and tag
    tagged1 = [nltk.pos_tag(i) for i in words_list]
    dump(FILENAMES[3], tagged1[:int(len(tagged1)/2)])
    dump(FILENAMES[4], tagged1[int(len(tagged1)/2):])
else:
    # Tack on back half of list to first half
    tagged1.extend(tagged2)

#print(len(tagged1)) # Just checking that this is 18393 (this should be length for all lists)

#looper(tagged)
