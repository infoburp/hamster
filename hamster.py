import urllib, os, sys
from sgmllib import SGMLParser
class urllist(SGMLParser):
        def reset(self):
                SGMLParser.reset(self)
                self.urls = []
        def start_a(self, attrs):
                href = [v for k, v in attrs if k=='href']
                if href:
                        self.urls.extend(href)
usock = urllib.urlopen(str(sys.argv[0]))
parser = urllist()
parser.feed(usock.read())
usock.close()
parser.close()
for url in parser.urls:
  try:
    urllib.urlretrieve(url,str(url))
    print(url)
  except urllib.error as err:
    print(str(url) + " " + err.code)
