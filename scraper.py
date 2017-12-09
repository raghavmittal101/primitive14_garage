from urllib import request
from bs4 import BeautifulSoup
import json

def getList(url):
    url_1 = url
    page = request.urlopen(url_1)
    soup = BeautifulSoup(page, "html.parser")
    ls = soup.find_all('p')
    dict = {"documents" : []}
    for i in range(len(ls)):
        ls[i] = {"id": str(i), "text" : ls[i].get_text()}
        dict["documents"].append(ls[i])
    return dict

if __name__ == "__main__":
    url = input("enter url")
    print(getList(url))