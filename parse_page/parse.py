import bs4 as bs
import glob
import os
import shutil
import sys

#htmls = glob.glob('*.html')
if len(sys.argv) != 2:
    print('usage: python3 parse.py page.html')
    exit(1)

htmls = [sys.argv[1]]

for html in htmls:
    path = html.replace('.html','')
    os.mkdir(path)
    soup = bs.BeautifulSoup(open(html), 'html.parser')
    imgs = soup.findAll('img', {'height':'200', 'width':'200'})
    for img in imgs:
        alt = img['alt']
        names = alt.split(', ')
        name = names[1] + '_' + names[0]

        file = path + '/' + name + '.jpeg'
        print(file)

        src = img['src']
        shutil.copy(src, file)

print(len(imgs))
