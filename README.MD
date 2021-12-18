# News-keyword-analysis

- Get news title & description and analyze based-on keyword.

# How To

1. Make **Naver API search client account".
Check this [LINK](https://developers.naver.com/docs/search/blog/).

2. Config setting.
- client_id : your naver search API application Client ID<sup>[tip1](#config_tip1)</sup>.
- client_secret : your naver search API application Client Secret.
- node : project data is organized with naver news. you can organize data with another node. check [tip2](#config_tip2). after you change node, you must edit method getNaverSearch function in **parsePostData.py**.
- search_texts : set this with keyword what you want to analyze.

3. In root directory run below command.

```
python main.py
```

\* tip

<a name="config_tip1">1</a> Click Client ID in https://developers.naver.com/apps/

<a name="config_tip2">2</a> https://developers.naver.com/docs/serviceapi/search/blog/blog.md

# Framework