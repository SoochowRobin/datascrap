# basic practice with request module. use get method to scrap google, and then store text on local machine
import requests

if __name__ == "__main__":
    # step1: speficify url
    url = "https://www.google.com"
    # step2: use requests.get method
    response = requests.get(url=url)
    # get response object
    text = response.text
    # store text in local machine
    with open('./google.html', 'w', encoding='utf-8') as fp:
        fp.write(text)
    print('over!')