import bs4
import io
import PIL
import requests

url = 'https://www.flaticon.com/search?word={}'
name = input('Input: ')
url.format(name)

r = requests.get(url.format(name))
b = bs4.BeautifulSoup(r.text, 'lxnl')
images = b.find_all('img')
imgl = images[0][data-thumb]
req = requests.get(imgl)
img = Image.open(BytesIO(req.content))
img.show()
