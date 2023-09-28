import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

x = requests.get('https://secure.icicidirect.com/trading/bsetbid/SBICAR')
print(x.status_code)

parser = MyHTMLParser()
parser.feed(x.text)

x.close()