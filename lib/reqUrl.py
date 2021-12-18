import urllib.request
import datetime

def getRequestUrl(url, id, secret):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", id)
    req.add_header("X-Naver-Client-Secret", secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None