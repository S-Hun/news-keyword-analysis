import reqUrl
import configparser
import urllib.request
import datetime
import json
import pandas as pd

#[CODE 1]
def getNaverSearch(node, srcText, start, display, config):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % \
        (urllib.parse.quote(srcText), start, display)
    url = base + node + parameters
    responseDecode = reqUrl.getRequestUrl(url, config) #[CODE 1]

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)

#[CODE 2]
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    jsonResult.append({'cnt':cnt, 'title':title, 'description': description, 'org_link':org_link, 'link': org_link, 'pDate':pDate})
    return

#[CODE 0]
def saveData(data_path, config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    node = config['API']['Node']
    srcText = config['API']['SearchWord']
    cnt = 0
    jsonResult = []
    jsonResponse = getNaverSearch(node, srcText, 1, 100, config) #[CODE 2]
    total = jsonResponse['total']
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt) #[CODE 3]
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100, config) #[CODE 2]
    print('전체 검색 : %d 건' %total)
    print("가져온 데이터 : %d 건" %(cnt))

    with open(data_path + '%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)
        outfile.write(jsonFile)
        print(data_path + '%s_naver_%s.json SAVED' % (srcText, node))

    csvDataFrame = pd.DataFrame(jsonResult)
    csvDataFrame.to_csv(data_path + '/%s_naver_%s.csv'%(srcText, node))
    print(data_path + '/%s_naver_%s.csv SAVED' % (srcText, node))