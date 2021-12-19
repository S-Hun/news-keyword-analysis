from lib import parsePostData
from lib import preprocess
from lda import lda

def main():
    path = './data'
    parsePostData.init(data_path=path)
    preprocess.wordCount(data_path=path)
    lda.init(data_path=path, K=[3])


if __name__ == "__main__":
    main()
