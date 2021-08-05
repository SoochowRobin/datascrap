import requests
import json
if __name__ == "__main__":
    # post url
    post_url = "https://fanyi.baidu.com/sug"
    data = {
        'kw': 'dog'
    }
    # cover UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    #get json object
    dict_obj = response.json()

    # store in local
    fp = open('./dog.json', 'w', encoding='utf-8')
    json.dump(dict_obj, fp=fp, ensure_ascii=False)

    print("Over!!!")