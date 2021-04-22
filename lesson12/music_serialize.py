import json, pickle

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
    {'name': 'Шапито', 'year': 2014}]}

fname_pickle = 'music.pic'
fname_json = 'music.json'

def serialize_pickle(fn, obj):
    with open(fn, 'wb') as f:
        print(f'Файл {fn} создан')
        pickle.dump(obj, f)
        return pickle.dumps(obj)

def serialize_json(fn, obj):
    with open(fn, 'w', encoding='utf-8') as f:
        print(f'Файл {fn} создан')
        json.dump(obj, f)
        return json.dumps(obj)

if __name__ == '__main__':
    print(serialize_pickle(fname_pickle, my_favourite_group))
    print(serialize_json(fname_json, my_favourite_group))
