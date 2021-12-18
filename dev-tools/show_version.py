import pandas as pd
import urllib.request
import json
import re
import konlpy

def main():
    print("pandas=="+pd.__version__)
    print("urllib.requset=="+urllib.request.__version__)
    print("json=="+json.__version__)
    print("re=="+re.__version__)
    print("konlpy=="+konlpy.__version__)

if __name__ == "__main__":
    main()