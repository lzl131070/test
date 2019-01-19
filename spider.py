import requests



if __name__ == '__main__':

    url = 'http://127.0.0.1:8000/'
    for i in range(5):
        res = requests.get(url)
        html = res.text
        print(i)
