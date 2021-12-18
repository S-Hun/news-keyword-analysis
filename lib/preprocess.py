import re
import json
import pandas as pd
from collections import Counter
from konlpy.tag import _okt

import os
import configparser

def getData(srcText, data_path):
    fileName = srcText + "_naver_news"
    return json.loads(open(data_path + '/' + fileName+'.json', 'r', encoding='utf-8').read())

def extractText(data):
    message = ''
    for item in data:
        if 'title' in item.keys():
            message = message + re.sub(r'[^\w]', ' ', item['title']) + ''
        if 'description' in item.keys():
            message = message + re.sub(r'[^\w]', ' ', item['description']) + ''
    return message

def nounTagging(message):
    nlp = Okt()
    return nlp.nouns(message)

def getConfig(config_path):
    if config_path == None:
        config_path = '.\\config.ini'
    print(os.getcwd())
    if os.path.isfile(config_path) != True:
        print("ERR: \"%s\" config file is missing." % (config_path))
        return None
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')

    for section in config.sections():
        for key in config[section]:
            if config[section][key] == '':
                print("ERR: config \"%s\" value is blank." % (key))
                return None
                
    return config

def wordCount(data_path = '.', config_path = None):
    config = getConfig(config_path)
    if config == None:
        return
    for srcText in config['API']['search_words'].split():
        message = extractText(getData(srcText, data_path))
        count = Counter(nounTagging(message))
        word_count = dict()
        for tag, counts in count.most_common(100):
            if(len(str(tag))>1):
                word_count[tag] = counts
        
        with open(data_path + '/' + srcText + '_count.json', 'w', encoding='utf8') as outfile:
            jsonFile = json.dumps(word_count, indent = 4, ensure_ascii = False)
            outfile.write(jsonFile)
            print(data_path + '/' + srcText + '_count.json SAVED')