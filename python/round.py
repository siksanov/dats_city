from requests import Session
from requests import get, post
from json import dump
from typing import List, Dict

url = "https://games-test.datsteam.dev"

headers = {"x-auth-token": "209c896d-8bfc-4585-ba18-cf8f22236150"}

# turn = words.get('turn')
# nextTurnSec = words.get('nextTurnSec')
# usesIndexes = words.get('usedIndexes')
# roundEndsAt = words.get('roundEndsAt')
# shuffleLeft = words.get('shuffleLeft')


class Tower:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

        response = get(f'{self.url}/api/words', headers=self.headers).json()
        param = response.copy()
        del param['words'] # {'mapSize': [30, 30, 100], 'turn': 8, 'nextTurnSec': 212, 'usedIndexes': [], 'roundEndsAt': '2025-04-05T07:55:00Z', 'shuffleLeft': 5}
        self.words = {k:v for k, v in enumerate(response.get('words'))}
        for i in param.get('usedIndexes'):
            del self.words[int(i)]
        
        self.load_words = []


    def write_words(self, data, name: str):
        with open(name, 'w') as file:
            file.write(str(data))

    def build(self, done = False, load_words: List[Dict] = None) -> Dict:
        self.done = done

        payload = {
            "done": self.done,
            "words": load_words
        }

        build = post(f'{self.url}/api/build', json=payload, headers=self.headers)

        return build.json()

    def find_crossings(self, id: int):
        word = self.words[id]
        words = self.words.copy()
        del words[id]

        for cross_id, cross_word in words.items():
            for letter_index, letter in enumerate(word):
                try:
                    cross_letter_index = cross_word.index(letter)
                except Exception:
                    continue
                else:
                    
                    return {
                            "id": id,
                            "word": word,
                            "letter": letter,
                            "letter_index": letter_index,
                            "cross_id": cross_id,
                            "cross_word": cross_word,
                            "cross_letter": cross_word[cross_letter_index],
                            "cross_letter_index": cross_letter_index,
                            }


        
        










    











# x = 0
# y = 0
# z = 0

# dir = 2
# id = 1
# pos = [x,y,z]

# words = [
#     {
#     "dir": dir,
#     "id": id,
#     "pos": [x,y,z]
#     }
# ]

# payload = {
#     "done": False,
#     "words": words
# }


# # build = session.get(f'{url}/api/build', json=payload, headers=headers).json()

# words = get(f'{url}/api/words', headers=headers).json()

# print(words)

# wrd_dict = {k:v for k, v in enumerate(words.get('words'))}

# usedIndexes = words['usedIndexes']

# for k, v in wrd_dict.items()[1:]:
#     n = 0
#     if n < 2:
#         for letter in v:
#             for i, j in wrd_dict.items()[k+1:]:
#                 try:
#                     wrd = j.index(letter)
#                 except Exception as err:
#                     pass
#                 else:
#                     dir = 3
#                     id = i
#                     x = wrd
#                     words.append(
#                         { 
#                             "dir": dir,
#                             "id": id,
#                             "pos": [x,y,z]
#                         }
#                     )
#                     n += 1

#     if n == 2:
        
#         word_one = wrd_dict[words[-2]["id"]]
#         word_two = wrd_dict[words[-1]["id"]]

#         word_max = word_one
#         word_min = word_two

#         index_letter_one = words[-2]["pos"][0]
#         index_letter_two = words[-1]["pos"][0]

#         if len(word_two) > len(word_max):
#             word_max = word_two
#             word_min = word_one

#         dict_max_min = {}

#         for i in range(len(word_max)):
#             try:
#                 dict_max_min[word_max[i]] = word_min[i]
#             except Exception as err:
#                 dict_max_min[word_max[i]] = ''
        
#         for i, j in wrd_dict.items()[k+1:]:

#             for ki, vj in dict_max_min:
#                 if j[index_letter_one] == ki and j[index_letter_two] == vj:
#                     dir = 2
#                     id = i
#                     y = i
#                     words.append(
#                         { 
#                             "dir": dir,
#                             "id": id,
#                             "pos": [x,y,z]
#                         }
#                     )
#                     n += 1

# print(words)