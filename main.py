from lib import parsePostData
from lib import preprocess

def main():
    parsePostData.init(data_path='./data')
    preprocess.wordCount(data_path='./data')

if __name__ == "__main__":
    main()