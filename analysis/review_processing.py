import sqlite3
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk.corpus
import nltk
import numpy
import csv

# --- function junction
def write_csv(filestring, this_list):
    with open(filestring + '.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for item in this_list:
            f.write(item)

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


review_text = [i[1] for i in reviews] #Reviews split up in list
write_csv('review_text', review_text)


sent_tokenized = [sent_tokenize(str(i)) for i in review_text] #Reviews split up into sentences
# write_csv('sentences_tokenized', sent_tokenized) # Not super sure why these won't work...


review_words = [ word_tokenize(str(i)) for i in sent_tokenized] # Reviews' sentences split up into words
# write_csv('sentences_words_tokenized', review_words)


# Reviews' words tagged (https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk)
tagged = [nltk.pos_tag(i) for i in review_words ] 
# write_csv('words_tagged', tagged)


looper(tagged)
