from requests import Session

url = "https://games-test.datsteam.dev"


headers = {"x-auth-token": "209c896d-8bfc-4585-ba18-cf8f22236150"}

session = Session()

x = 0
y = 0
z = 0


dir = 2
id = 1
pos = [x,y,z]

words = [
    {
    "dir": dir,
    "id": id,
    "pos": [x,y,z]
    }
]

payload = {
    "done": False,
    "words": words
}


# build = session.get(f'{url}/api/build', json=payload, headers=headers).json()

words = session.get(f'{url}/api/words', headers=headers).json()

print(words)

wrd_dict = {k:v for k, v in enumerate(words.get('words'))}

usedIndexes = words['usedIndexes']

for k, v in wrd_dict.items()[1:]:
    n = 0
    if n < 2:
        for letter in v:
            for i, j in wrd_dict.items()[k+1:]:
                try:
                    wrd = j.index(letter)
                except Exception as err:
                    pass
                else:
                    dir = 3
                    id = i
                    x = wrd
                    words.append(
                        { 
                            "dir": dir,
                            "id": id,
                            "pos": [x,y,z]
                        }
                    )
                    n += 1

    if n == 2:
        
        word_one = wrd_dict[words[-2]["id"]]
        word_two = wrd_dict[words[-1]["id"]]

        word_max = word_one
        word_min = word_two

        index_letter_one = words[-2]["pos"][0]
        index_letter_two = words[-1]["pos"][0]

        if len(word_two) > len(word_max):
            word_max = word_two
            word_min = word_one

        dict_max_min = {}

        for i in range(len(word_max)):
            try:
                dict_max_min[word_max[i]] = word_min[i]
            except Exception as err:
                dict_max_min[word_max[i]] = ''
        
        for i, j in wrd_dict.items()[k+1:]:

            for ki, vj in dict_max_min:
                if j[index_letter_one] == ki and j[index_letter_two] == vj:
                    dir = 2
                    id = i
                    y = i
                    words.append(
                        { 
                            "dir": dir,
                            "id": id,
                            "pos": [x,y,z]
                        }
                    )
                    n += 1

print(words)