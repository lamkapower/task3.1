import json
import collections

def json_read():
    with open('newsafr.json' , encoding='utf-8') as fi:
        data = json.load(fi)
        descript_list = []
        for content in data['rss']['channel']['items']:
            descript_list.append(content['description'].split())
    return descript_list



def sortByLength(inputStr):
    return len(inputStr)

def listmerge(json_read):
    merged_list=[]
    for lst in json_read:
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
    for word in listmerge(json_read()):
        cnt[word] += 1
    print(cnt.most_common(10))

top_ten()