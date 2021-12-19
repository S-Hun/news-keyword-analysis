import pandas as pd
from konlpy.tag import Okt
import json
import gensim
import glob
import pyLDAvis
import pyLDAvis.gensim_models

def getFiles(data_path):
    all_files = glob.glob(data_path + "/*.csv")
    li = []
    for filename in all_files:
        print(filename)
        df = pd.read_csv(filename, encoding='utf-8')
        li.append(df)
    return li

def convTokens(df, columns):
    data = df[columns[0]]
    if len(columns) > 1:
        for column in columns[1:]:
            temp = [i + j for i, j in zip(data, df[column])]
            data = temp
    data_noun_tk = []

    okt = Okt()

    for d in data:
        data_noun_tk.append(okt.nouns(d))

    data_noun_tk2 = []

    for d in data_noun_tk:
        item = [i for i in d if len(i) > 1]
        data_noun_tk2.append(item)
    
    return data_noun_tk2

def createLDA(tokens, k):
    dictionary = gensim.corpora.Dictionary(tokens)
    corpus = [dictionary.doc2bow(word) for word in tokens]

    lda_model = gensim.models.ldamulticore.LdaMulticore(
        corpus, iterations=12, num_topics=k, id2word=dictionary, passes=1, workers=10)
    with open('LDA_K%s.json' % (k), 'w', encoding='utf8') as outfile:
                jsonFile = json.dumps(
                    lda_model.print_topics(num_topics=k, num_words=15), indent=4, ensure_ascii=False)
                outfile.write(jsonFile)
                print('LDA_K%s.json' % (k))

    prepared_data = pyLDAvis.gensim_models.prepare(
        lda_model, corpus, dictionary)
    pyLDAvis.save_html(prepared_data, 'LDA_K%s.html' % (k))
    print("LDA_K%s.html created." % (k))

def init(data_path='.', K=[3]):
    df = pd.concat(getFiles(data_path), axis=0, ignore_index=True)
    tokens = convTokens(df, ['title', 'description'])
    for k in K:
        createLDA(tokens, k)

