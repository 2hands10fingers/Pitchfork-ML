import sqlite3
import statistics
import re

database = 'database.sqlite'
folder = 'Volumes/TonoDrive'
filepath = f'/{folder}/{database}'
conn = sqlite3.connect(filepath)

print('Connection Established!')

cursor = conn.cursor()
reviews = cursor.execute("SELECT * FROM 'reviews';")


def artist_analysis():
    artists = cursor.execute("SELECT * FROM 'artists';")
    artist_list = []
    for i in artists: artist_list.append(i[1])

    print(len(set(artist_list)), "artists")

def review_score_analysis():
    scores = []
    reviews = cursor.execute("SELECT * FROM 'reviews';")

    for i in reviews:
        scores.append(i[4])

    print(scores)
    mean = statistics.mean(scores)

    print(mean)



def reviews_counter_analysis():
    reviews = cursor.execute("SELECT * FROM 'reviews';")
    ten = []
    ninenine = []
    nineeight = []
    nineseven = []
    ninesix = []
    ninefive = []
    ninefour = []
    ninethree = []
    ninetwo = []
    nineone = []
    nine = []
    zero = []

    for i in reviews:
        y = ("ARTIST: ", i[2], "ALBUM: ", i[1])
        if i[4] == 10.0: ten.append(y)
        if i[4] == 9.9: ninenine.append(y)
        if i[4] == 9.8: nineeight.append(y)
        if i[4] == 9.7: nineseven.append(y)
        if i[4] == 9.6: ninesix.append(y)
        if i[4] == 9.5: ninefive.append(y)
        if i[4] == 9.4: ninefour.append(y)
        if i[4] == 9.3: ninethree.append(y)
        if i[4] == 9.2: ninetwo.append(y)
        if i[4] == 9.1: nineone.append(y)
        if i[4] == 9.0: nine.append(y)
        if i[4] == 0.0: zero.append(y)


    print('0\n')
    print(len(zero))
    for i in zero: print(i)
    print('10\n')
    print(len(ten))
    for i in ten: print(i)
    print('9.9\n')
    print(len(ninenine))
    for i in ninenine: print(i)
    print('9.8\n')
    print(len(nineeight))
    for i in nineeight: print(i)
    print(len(nineseven))
    print('9.7\n')
    for i in nineseven: print(i)
    print(len(ninesix))
    print('9.6\n')
    for i in ninesix: print(i)
    print(len(ninefive))
    print('9.5\n')
    for i in ninefive: print(i)
    print(len(ninefour))
    print('9.4\n')
    for i in ninefour: print(i)
    print(len(ninethree))
    print('9.3\n')
    for i in ninethree: print(i)
    print(len(ninetwo))
    print('9.2\n')
    for i in ninetwo: print(i)
    print(len(nineone))
    print('9.1\n')
    for i in nineone: print(i)
    print(len(nine))
    print('9.0\n')
    for i in nine: print(i)

def content_analysis():
    content = cursor.execute("SELECT * FROM 'content';")
    array = []
    newarray = []
    sets = []
    final = []
    final_final = []
    for i in content:
        array.append(i[1])

    for i in array:
        x = i.split()
        newarray.append(x)

    for i in newarray: sets.append(i)
    for i in sets: final.append(i)

    flat_list = [item.lower() for sublist in final for item in sublist]


    for i in set(flat_list):
        address = re.sub(r'([^\s\w]|_)+', '', i)
        final_final.append(address)

    # print(final_final)
    print("\n\nUNIQUE WORDS:", len(final_final))
