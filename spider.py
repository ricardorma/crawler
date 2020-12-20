from urllib.request import urlopen
from buscador_contenido import LinkFinder
from Dominio import *
from Archivo import *

class Spider:

    NOMBRE_PROYECTO = ''
    URL_INICIAL = ''
    NOMBRE_DOMINIO = ''
    ACHIVO_COLA = ''
    ARCHIVO_INDEXADAS = ''
    cola = set()
    indexado = set()

    def __init__(self, nombre_proyecto, url_inicial, nombre_dominio):
        Spider.NOMBRE_PROYECTO = nombre_proyecto
        Spider.URL_INICIAL = url_inicial
        Spider.NOMBRE_DOMINIO = nombre_dominio
        Spider.ACHIVO_COLA = Spider.NOMBRE_PROYECTO + '/queue.txt'
        Spider.ARCHIVO_INDEXADAS = Spider.NOMBRE_PROYECTO + '/crawled.txt'
        self.crear_ficheros_iniciales()
        self.indexar_pagina('Primera araña', Spider.URL_INICIAL)

    @staticmethod
    def crear_ficheros_iniciales():
        crear_directorio_proyecto(Spider.NOMBRE_PROYECTO)
        crear_archivos_datos(Spider.NOMBRE_PROYECTO, Spider.URL_INICIAL)
        Spider.cola = archivo_a_lista(Spider.ACHIVO_COLA)
        Spider.indexado = archivo_a_lista(Spider.ARCHIVO_INDEXADAS)

    @staticmethod
    def indexar_pagina(nombre_hilo, url_pagina):
        if url_pagina not in Spider.indexado:
            print(nombre_hilo + ' esta indexando ' + url_pagina)
            print('La posicion de la cola ' + str(len(Spider.cola))
                  + ' | Se indexa  ' + str(len(Spider.indexado)))
            Spider.anadir_urls_a_cola(Spider.traducir_urls(url_pagina))
            Spider.cola.remove(url_pagina)
            Spider.indexado.add(url_pagina)
            Spider.actualizar_archivos()

    @staticmethod
    def traducir_urls(url_pagina):
        cadena_html = ''
        try:
            respuesta = urlopen(url_pagina)
            if 'text/html' in respuesta.getheader('Content-Type'):
                bytes_devueltos = respuesta.read()
                cadena_html = bytes_devueltos.decode("utf-8")
            buscador = LinkFinder(Spider.URL_INICIAL, url_pagina)
            buscador.feed(cadena_html)
        except Exception as e:
            print(str(e))
            return set()
        return buscador.urls_paginas()

    @staticmethod
    def anadir_urls_a_cola(urls):
        for url in urls:

            if (url in Spider.cola) or (url in Spider.indexado):
                continue

            if Spider.NOMBRE_DOMINIO != obtener_dominio(url):
                continue
            Spider.cola.add(url)

    @staticmethod
    def actualizar_archivos():
        lista_a_archivo(Spider.cola, Spider.ACHIVO_COLA)
        lista_a_archivo(Spider.indexado, Spider.ARCHIVO_INDEXADAS)


