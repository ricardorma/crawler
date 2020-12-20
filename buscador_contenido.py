from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, url_inicial, url_pagina):
        super().__init__()
        self.url_inicial = url_inicial
        self.page_url = url_pagina
        self.urls = set()

    def handle_starttag(self, tag, atributos):
        if tag == 'a':
            for (atributo, valor) in atributos:
                if atributo == 'href':
                    url = parse.urljoin(self.url_inicial, valor)
                    self.urls.add(url)

    def urls_paginas(self):
        return self.urls

    def error(self, mensaje):
        pass
