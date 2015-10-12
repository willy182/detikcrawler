__author__ = 'willy-182'

import requests
from bs4 import BeautifulSoup

urlRequest = 'http://www.detik.com/'

response = requests.get(urlRequest)

if response.status_code == 200:
    jumlah_size_img = 0

    soup = BeautifulSoup(response.text, 'html.parser')
    for i in soup.find_all('img'):
        url_img = i.get('src')
        if url_img.startswith('http://') or url_img.startswith('https://'):
            image = url_img
        elif url_img.startswith('//') :
            image = 'http:%s' % url_img
        else:
            image = urlRequest+url_img

        jumlah_tag_img = len(soup.find_all('img'))

        try:
            r = requests.get(image)
            im = r.headers['Content-Length']
            jumlah_size_img += int(im)
        except Exception as e:
            print "gagal dapetin image"

    print "Total Images = (%d)" % jumlah_tag_img
    print "Total size = (%d)" % jumlah_size_img
else:
    print "gagal konek"