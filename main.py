from lib import parsePostData
from lib import preprocess
from lda import lda


def main():
    path = './data'
    parsePostData.init(data_path=path)
    preprocess.wordCount(data_path=path)
    lda.createLDA(data_path=path)


if __name__ == "__main__":
    main()
