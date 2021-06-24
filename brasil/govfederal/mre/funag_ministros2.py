from typing import List
from urllib.request import urlopen

import bs4.element
from bs4 import BeautifulSoup

data: List = []  # <- we want the data here.

# Parse the webpage html
bs = BeautifulSoup('''\
<div class="item-page">
   <p><strong>TITLE</strong></p>
   <p><strong>18/05/2016</strong>&nbsp; &nbsp; <a href="/link//paragraphs/bio">Author's name</a>&nbsp;|&nbsp;<a href="/link/paragraphs/speech">Speech</a></p>
   <p><strong>01/01/2011&nbsp; &nbsp;&nbsp;</strong><a href="/link/paragraphs/bio02">Author's name02</a></p>
   <p><strong>28/08/2013&nbsp; &nbsp; </strong><a href="/link/paragraphs/bio03">Author's name03</a>&nbsp;|&nbsp;<a href="/link/paragraphs/speech">Speech</a></p>
   <p><strong>01/01/2011&nbsp; &nbsp;&nbsp;</strong><a href="/link/paragraphs/bio04">Author's name04</a></p>
   <p><strong>01/01/2011&nbsp; &nbsp;&nbsp;</strong><a href="/link/paragraphs/bio05">Author's name05</a></p>
   <p><strong>28/08/2013&nbsp; &nbsp; </strong><a href="/link/paragraphs/bio03">Author's name06</a>&nbsp;|&nbsp;<a href="/link/paragraphs/speech">Speech</a></p>
</div>''', features='html.parser')

# Grab the paragraphs within the `item-page` div, checkout CSS selectors :).
entries = bs.select('div.item-page p')

# Populate the entries with time and links (if they are present)
for entry in entries:
    entry: bs4.element.Tag# https://github.com/il-vladislav/BeautifulSoup4/blob/master/bs4/element.py
    print(entry, type(entry))
    authors =  bs.find('a').text
    # authors =  entry.select('a')
    print(authors)
    time = entry.select_one('strong').get_text()
    print(time)
    if time == 'TITLE':
        continue  # skip this entry

    # Grab a list of the links (may be of size 0-2 depending on the contents).
    links = [link.get('href') for link in entry.select('a')]

    # Populate the array with a document.
    data.append({
        'time': time,
        'author': authors,
        'speech_link': links[0] if len(links) > 0 else '',
        'speech': [],
        'bio_link': links[1] if len(links) > 1 else '',
        'bio': [],
    })

# Collect speeches and bios if present.
for person in data:
    if person['speech_link']:  # empty strings evaluate as False and would be skipped.
        html = urlopen('https://baconipsum.com/api/?type=all-meat&paras=2&start-with-lorem=1&format=html')
        person['speech'] = [para.get_text() for para in BeautifulSoup(html, 'html.parser').select('p')]

    if person['bio_link']:
        html = urlopen('https://baconipsum.com/api/?type=all-meat&paras=2&start-with-lorem=1&format=html')
        person['bio'] = [para.get_text() for para in BeautifulSoup(html, 'html.parser').select('p')]

# print(data)
