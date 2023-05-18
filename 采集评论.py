import httpx


def main():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42",

    }
    cookies = {
        "kpf": "PC_WEB",
        "clientid": "3",
        "did": "web_1712a745d28adca024fc9d8898cdfa34",
        "userId": "3503868975",
        "kuaishou.server.web_st": "ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB4caYt4tEw2ojmnXNGzkiW2805GqRhTu7_AB9Bvb4bmYRArIJo4kHqATsitJlanB4hPAhL9zkbQgVgEqfMlAt_JDEikmHy-4ErvpXw4GpQEedG9mnloqnUakhtscq70D2t-LMfojtC5NDXQRm1nZZrAkVg0MYEJ-R7d2arHDI1NRCDP7I9VFPRFIyv88pRad-_JwAbozkAArrrc2bNDw8MBoSKS0sDuL1vMmNDXbwL4KX-qDmIiD6ZUyIJsStQA24xCKKFiizh5xzmyqeadt4A9YtLJjclSgFMAE",
        "kuaishou.server.web_ph": "4ccee95088f5dbd238a0adfc7e05d69ce5db",
        "ktrace-context": "1|MS43NjQ1ODM2OTgyODY2OTgyLjE5MTU4NjY0LjE2ODQ0MTg1MTUxMDEuMzk1NDM0|MS43NjQ1ODM2OTgyODY2OTgyLjgzNDE3MTE4LjE2ODQ0MTg1MTUxMDEuMzk1NDM1|0|graphql-server|webservice|false|NA",
        "kpn": "KUAISHOU_VISION"
    }
    url = "https://www.kuaishou.com/graphql"
    json_data = {
        "operationName": "commentListQuery",
        "variables": {
            "photoId": "3xec6d45j94838i",
            "pcursor": ""
        },
        "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      authorLiked\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        authorLiked\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    comment = get_comment(url, headers, cookies, json_data)
    parse_comment(comment)

def get_comment(url, headers, cookies, json_data):

    with httpx.Client() as client:
        response = client.post(url=url, headers=headers, cookies=cookies, json=json_data)
        return response.json()

def parse_comment(comment):
    root_comments = comment['data']['visionCommentList']['rootComments']
    for item in root_comments:
        print(item['content'])


if __name__ == '__main__':
    main()