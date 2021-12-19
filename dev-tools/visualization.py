from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import json
import glob

def vis1():
    jsonFilesPath = glob.glob('./data/*_count.json')
    jsonFiles = []
    for jsonFilePath in jsonFilesPath:
        with open(jsonFilePath, 'r', encoding='utf-8') as infile:
            jsonFiles.append(json.load(infile))
    plt.figure(figsize=(10,8))
    count = Counter()
    for i, jsonFile in enumerate(jsonFiles):
        count += Counter(jsonFile)
        word_count = dict(itertools.islice(jsonFile.items(), 20))
        sorted_Keys = sorted(word_count, key = word_count.get, reverse = True)
        sorted_Values = sorted(word_count.values(), reverse = True)
        plt.subplot(4, 1, i+1)
        plt.title(jsonFilesPath[i].replace('./data\\','').replace('_count.json',''))
        plt.bar(range(len(word_count)), sorted_Values, align='center', color='C'+str(i))
        plt.xticks(range(len(word_count)), list(sorted_Keys), rotation='60')
    
    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.9, top=0.9, wspace=0.2, hspace=0.7)
    plt.savefig('./data/count_vis.png')
    stopwords = set(STOPWORDS)
    wc = WordCloud(font_path="C:/Windows/Fonts/NGULIM.TTF", background_color='ivory', stopwords=stopwords, width=800, height=600)
    cloud = wc.generate_from_frequencies(dict(count))
    cloud.to_file("./data/count_wordcloud.jpg")


def font_settings():
    from matplotlib import font_manager, rc
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)

if __name__ == "__main__":
    font_settings()
    vis1()