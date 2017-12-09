import http.client
import json
# import scraper

# **********************************************
# *** Update or verify the following values. ***
# **********************************************
def getTags(text):
    # Replace the accessKey string value with your valid access key.
    accessKey = '8565315a2d7443418390b0324344c4fd'
    uri = "westcentralus.api.cognitive.microsoft.com"
    path = "/text/analytics/v2.0/keyPhrases"
    print(text)
    # documents = scraper.getList("https://en.wikipedia.org/wiki/India")
    # documents = { "documents": [
    #     { "id": "1", "text": "This is a document written in English." },
    #     { "id": "2", "text": "Este es un document escrito en Español." },
    #     { "id": "3", "text": "这是一个用中文写的文件" }
    # ]}
    documents = { "documents": [ { "id": "1", "text": str(text) } ]}
    print(documents)
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = http.client.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return json.loads(response.read())

if __name__ == "__main__":
    print(getTags(input("enter>")))