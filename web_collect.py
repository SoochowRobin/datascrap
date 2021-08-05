# the task is to write code get user input and get the result searched by google
# and then store the text in local machine
import requests
if __name__ == "__main__":
    url = "https://www/google.com/search?"
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'
    }
    # get input parameter
    kw = input("enter what you want search")
    param = {
        'query': kw
    }
    # get response object
    response = requests.get(url=url, params=param, headers=headers,verify=False)

    #use response object to get content of page
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, " has successfully saved!")

