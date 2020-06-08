import json

def json_read():

    with open('newsafr.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        a = data['rss']
        b = a['channel']
        c = b['items']
        collection = []
        frequency = {}
        for dicts in c:
            str = dicts['description']
            temp = str.split()
            for words in temp:
                if len(words) > 6:
                    count = frequency.get(words, 0)
                    frequency[words] = count + 1
        for word in frequency:
            collection.append(frequency[word])
        collection.sort(reverse=True)
        top_10 = collection[0:10:]
        for i in frequency:
            if frequency[i] in top_10:
                print(f'{i} - {frequency[i]}')

json_read()

print('')

def xml_read():
    import xml.etree.ElementTree as ET

    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    collection = []
    frequency = {}
    xml_items = root.findall('channel/item')
    for item in xml_items:
        temp = item.find('description').text.split()
        for words in temp:
            if len(words) > 6:
                count = frequency.get(words, 0)
                frequency[words] = count + 1
    for word in frequency:
        collection.append(frequency[word])
    collection.sort(reverse=True)
    top_10 = collection[0:10:]
    for i in frequency:
        if frequency[i] in top_10:
            print(f'{i} - {frequency[i]}')

xml_read()

