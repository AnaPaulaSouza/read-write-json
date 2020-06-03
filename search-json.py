from search-json import *

def read_write_json():

    with open('/home/ana/Downloads/events_navigation.jpg', 'rb') as file:
        data = [json.loads(i) for i in file.readlines()]

    for i in data:
        v = i.get('page_type')
        with open(v, 'a+') as fwrite:
            json.dump(i, fwrite, sort_keys=False, indent=4, ensure_ascii=False)


if __name__ == '_main_':
    read_write_json()