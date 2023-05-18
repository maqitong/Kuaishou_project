"""
爬虫思路
      数据来源分析
      1.爬什么？(需求分析)
          视频、标题、评论 (数据分析）
      2.去哪爬？(接口分析) url = “https://www.kuaishou.com/graphql”
          触发的接口怎么分析：可以先清空数据包，单独触发接口获取api
          视频一般都是ajax请求。(动态数据)


      爬虫代码实现
      1.发送请求:构造请求头和请求体
      2.数据获取
      3.数据解析
      4.数据存储
"""
import httpx

def click_like(url, headers, json_data):

    # 介绍怎么使用httpx
    with httpx.Client() as client:
        resp = client.post(url=url, headers=headers, json=json_data)
        if resp.json()['data']['visionVideoLike']['result'] == 1:
            print('点击爱心！')

#  with open() as f:

def main():
    url = 'https://www.kuaishou.com/graphql'
    # 爬虫的本性伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
        'cookie': 'kpf=PC_WEB; clientid=3; did=web_1712a745d28adca024fc9d8898cdfa34; userId=3503868975; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB3kTmNn44xPBuSIrUlo8OxJY6l2uPX9sSFqBqIYZKYl_6gZQ9Bcyq7ll5NMMNJ21cqkMImbNOdcg7HvvSf-OuWYqSxGcJZzRHAXrs2CJM8fBzUHgzvhAwm2mhRI_L5Bc2pR6vRoZm25tert5uxv-bBKRm8qaZOF81fdYS4Y_wor-z10dFEntnd3zg-8N6uhVpa7mIKazxSrxFXuwaZKy-eRoSWXnZQFypWC8Fi7687FtZGgfDIiBYpeEHeUUygmh70MQNdjQcwCQGjRXQGnRHd7WdyS_cXigFMAE; kuaishou.server.web_ph=428cd918af568f88e7f86885d9d762bcf3b3; kpn=KUAISHOU_VISION',
    }
    json_data = {
        "operationName": "visionVideoLike",
        "variables": {
            "photoId": "3xg3ysi9yd7fsgy",
            "photoAuthorId": "3xutpw6xj3m9nue",
            "cancel": 0,
            "expTag": "1_i/2002189855480765026_xpcwebbrilliantxxcarefully0"
        },
        "query": "mutation visionVideoLike($photoId: String, $photoAuthorId: String, $cancel: Int, $expTag: String) {\n  visionVideoLike(photoId: $photoId, photoAuthorId: $photoAuthorId, cancel: $cancel, expTag: $expTag) {\n    result\n    __typename\n  }\n}\n"
    }
    click_like(url, headers, json_data)



if __name__ == '__main__':
    main()