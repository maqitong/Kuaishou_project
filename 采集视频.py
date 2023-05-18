import os.path

import httpx


def get_json(url, headers, cookies, json_data):
    try:
        with httpx.Client() as client:
            resp = client.post(url=url, headers=headers, cookies=cookies, json=json_data, timeout=4)
            return resp.json()
    except:
        return None

def parse_json(json_dic):
    # 短视频标题 作者id 作者名字 短视频id 短视频url
    result_list = []
    for item in json_dic['data']['brilliantTypeData']['feeds']:
        caption = item['photo']['caption']
        author_id = item['author']['id']
        name = item['author']['name']
        photo_id = item['photo']['id']
        photo_url = item['photo']['photoUrl']
        resp_dict = {"caption": caption,
                     "author_id": author_id,
                     "name": name,
                     "photo_id": photo_id,
                     "photo_url": photo_url,
                     }
        result_list.append(resp_dict)

    return result_list


# 下载视频
def download_photo(feeds, headers):
    # 请求下载地址url获取二进制数据
    for feed in feeds:
        with httpx.Client() as client:
            resp = client.get(url=feed['photo_url'], headers=headers)
            save_photo(resp.content, feed['photo_id'])

        return None


def save_photo(data, filename):
    if not os.path.exists('./视频'):
        os.mkdir('./视频')

    with open('./视频/' + filename + '.mp4', mode='wb')as f:
        f.write(data)


def main():
    url = 'https://www.kuaishou.com/graphql'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',

    }
    cookies = {
        "kpf": "PC_WEB",
        "clientid": "3",
        "did": "web_1712a745d28adca024fc9d8898cdfa34",
        "userId": "3503868975",
        "kpn": "KUAISHOU_VISION",
        "kuaishou.server.web_st": "ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB4caYt4tEw2ojmnXNGzkiW2805GqRhTu7_AB9Bvb4bmYRArIJo4kHqATsitJlanB4hPAhL9zkbQgVgEqfMlAt_JDEikmHy-4ErvpXw4GpQEedG9mnloqnUakhtscq70D2t-LMfojtC5NDXQRm1nZZrAkVg0MYEJ-R7d2arHDI1NRCDP7I9VFPRFIyv88pRad-_JwAbozkAArrrc2bNDw8MBoSKS0sDuL1vMmNDXbwL4KX-qDmIiD6ZUyIJsStQA24xCKKFiizh5xzmyqeadt4A9YtLJjclSgFMAE",
        "kuaishou.server.web_ph": "4ccee95088f5dbd238a0adfc7e05d69ce5db"
    }

    json_data = {
        "operationName": "brilliantTypeDataQuery",
        "variables": {
            "hotChannelId": "00",
            "page": "brilliant",
            "pcursor": "1"
        },
        "query": "fragment photoContent on PhotoEntity {\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  __typename\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantTypeDataQuery($pcursor: String, $hotChannelId: String, $page: String, $webPageArea: String) {\n  brilliantTypeData(pcursor: $pcursor, hotChannelId: $hotChannelId, page: $page, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"
    }
    json_dic = get_json(url, headers, cookies, json_data)
    if json_dic:
        feeds = parse_json(json_dic)
        if feeds:
            download_photo(feeds,headers)

if __name__ == '__main__':
    main()