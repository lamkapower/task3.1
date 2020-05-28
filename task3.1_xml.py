import xml.etree.ElementTree as ET
import collections


def xml_read():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    xml_items = root.findall('channel/item/description')
    descript_list = []
    for xmli in xml_items:
        descript_list.append(xmli.text.split())
    return descript_list

def sortByLength(inputStr):
    return len(inputStr)

def listmerge(xml_read):
    merged_list=[]
    for lst in xml_read:
        merged_list.extend(lst)
    top_words = []
    for num , value in enumerate(merged_list):
        if len(value) > 6:
            top_words.append(merged_list[num])
    top_words.sort(key=sortByLength , reverse=True)
    top_words = map(lambda x:x.lower(), top_words)
    return top_words

def top_ten():
    cnt = collections.Counter()
    for word in listmerge(xml_read()):
        cnt[word] += 1
    print(cnt.most_common(10))

top_ten()