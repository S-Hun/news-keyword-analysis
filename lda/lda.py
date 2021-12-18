
import pandas as pd
from konlpy.tag import Okt
import gensim
import glob
import pyLDAvis
import pyLDAvis.gensim_models
# import os
# os.environ["PYTHONIOENCODING"] = "utf-8"

if __name__ == '__main__':

    # csv 파일 읽어들이는 부분
    path = './data'  # use your path
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        print(filename)
        df = pd.read_csv(filename, encoding='utf-8')
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)

    description = df['description']  # df중 description 열만 따로 저장
    descriotion_noun_tk = []
    # 파일 읽어들이기 끝

    # 단어 추출
    okt = Okt()

    for d in description:
        descriotion_noun_tk.append(okt.nouns(d))  # 명사 추출

    descriotion_noun_tk2 = []

    for d in descriotion_noun_tk:
        item = [i for i in d if len(i) > 1]  # 토큰 길이가 1보다 큰거만 추출
        descriotion_noun_tk2.append(item)
    # 단어 추출 끝

    # lda 모델링
    dictionary = gensim.corpora.Dictionary(descriotion_noun_tk2)
    corpus = [dictionary.doc2bow(word) for word in descriotion_noun_tk2]
    # print(corpus)

    k = 3
    lda_model = gensim.models.ldamulticore.LdaMulticore(
        corpus, iterations=12, num_topics=k, id2word=dictionary, passes=1, workers=10)
    print(lda_model.print_topics(num_topics=k, num_words=15))
    # lda 모델링 끝

    # 시각화
    prepared_data = pyLDAvis.gensim_models.prepare(
        lda_model, corpus, dictionary)
    pyLDAvis.save_html(prepared_data, 'lda.html')
