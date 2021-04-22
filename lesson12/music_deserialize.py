'''2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. И получить объект: словарь из предыдущего задания.'''

import pickle, json

fname_pickle = 'music.pic'
fname_json = 'music.json'

def deserialize_pickle(fn):
    with open(fn, 'rb') as f:
        print(f'Файл {fn} прочитан')
        return pickle.load(f)

def deserialize_json(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        print(f'Файл {fn} прочитан')
        return json.load(f)

if __name__ == '__main__':
    print(deserialize_pickle(fname_pickle))
    print(deserialize_json(fname_json))
