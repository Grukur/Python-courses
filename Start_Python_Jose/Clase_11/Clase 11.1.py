from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1') # para buscar un unico objeto
    print(h1_tag.string)


def find_list_items():
    list_item = simple_soup.find_all('li')
    print(list_item)
    for i in range(len(list_item)):
        list2 = next(iter(list_item[i])).string # # para buscar un unico objeto
        print(list2)

    list_content = [e.string for e in list_item]
    print(list_content)


def find_paragraph():
    paragraph = simple_soup.find('p', {"class": 'subtitle'})
    print(paragraph.string)


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)


find_list_items()
find_title()
find_paragraph()
find_other_paragraph()







