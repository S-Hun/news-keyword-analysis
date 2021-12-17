import re
import json
import pandas as pd
from collections import Counter
from konlpy.tag import Okt
from collections import Counter

def getData(data_path = '.'):
    fileName = "/웹3.0_naver_news"
    return json.loads(open(data_path + fileName+'.json', 'r', encoding='utf-8').read())

def extractText(data):
    message = ''
    for item in data:
        if 'title' in item.keys():
            message = message + re.sub(r'[^\w]', ' ', item['title']) + ''
        if 'description' in item.keys():
            message = message + re.sub(r'[^\w]', ' ', item['description']) + ''
    return message

def nounTagging():
    nlp = Okt()
    message = extractText(getData())
    return nlp.nouns(message)

def getCV(data_path = '.'):
    count = Counter(nounTagging())
    word_count = dict()
    for tag, counts in count.most_common(100):
        if(len(str(tag))>1):
            word_count[tag] = counts
    
    with open(data_path + '/웹3.0_count.json', 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(word_count, indent = 4, ensure_ascii = False)
        outfile.write(jsonFile)
        print(data_path + '/웹3.0_count.json SAVED')