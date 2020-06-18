import requests

def translate_text(num):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    api_key = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
    list = []
    new_list = []
    if num == 'DE':
        name = 'DE.txt'
        name_1 = 'de_1.txt'
        lang = 'de-ru'
    elif num == 'FR':
        name = 'FR.txt'
        name_1 = 'fr_1.txt'
        lang = 'fr-ru'
    elif num == 'ES':
        name = 'ES.txt'
        name_1 = 'es_1.txt'
        lang = 'es-ru'
    with open(name, 'r', encoding= 'utf-8') as fr:
        for line in fr:
            line = line.strip()
            list.append(line)
    params = {
        'key': api_key,
        'text': list,
        'lang': lang
    }
    response = requests.post(url, params= params)
    new_list.append(response.json()['text'])
    with open(name_1, 'w', encoding= 'utf-8') as fw:
        for data in new_list:
            for elements in data:
                fw.write(elements)

translate_text('ES')
