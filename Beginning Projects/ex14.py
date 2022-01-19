#! python3
# ex14.py

import dbm, pickle, ex12, os

def sed(pattern, replacement_string, filename_1, filename_2):
    with open(filename_1) as file_obj_1:
        with open(filename_2, 'w') as file_obj_2:
            file_1 = file_obj_1.read()
            file_2 = file_1.replace(pattern, replacement_string)
            file_obj_2.write(file_2)

def store_anagram_set(anagram_dict):
    db = dbm.open('anagrams', 'c')
    for word_tuple, word_list in anagram_dict.items():
        word_tuple = ''.join(word_tuple)
        word_data = ''
        for word in word_list:
            word_data += ' ' + word
        db[word_tuple] = pickle.dumps(word_data)
    db.close()

def read_anagrams(anagram):
    try:
        db = dbm.open('anagrams', 'c')
        anagram = ''.join(tuple(sorted(tuple(anagram))))
        words = pickle.loads(db[anagram])
        db.close()
        return words
    except KeyError:
        print('Anagram not found')

def save_file_anagrams(filename):
    with open(filename) as file_obj:
        file = file_obj.read()
        anagram_dict = ex12.anagrams(file)
        store_anagram_set(anagram_dict)
        
def walk_dir(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk_dir(path)
