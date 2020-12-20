import threading
from queue import Queue
from spider import Spider
from Dominio import *
from Archivo import *

NOMBRE_PROYECTO = 'esi'
PAGINA_INICIAL = 'http://webpub.esi.uclm.es/spa'
NOMBRE_DOMINIO = obtener_dominio(PAGINA_INICIAL)
ARCHIVO_COLA = NOMBRE_PROYECTO + '/queue.txt'
ARCHIVO_INDEXADAS = NOMBRE_PROYECTO + '/crawled.txt'
NUMERO_HILOS = 8
queue = Queue()
Spider(NOMBRE_PROYECTO, PAGINA_INICIAL, NOMBRE_DOMINIO)

def crear_spiders():
    for _ in range(NUMERO_HILOS):
        t = threading.Thread(target=objetivo)
        t.daemon = False
        t.start()

def objetivo():
    while True:
        url = queue.get()
        Spider.indexar_pagina(threading.current_thread().name, url)
        queue.task_done()

def crear_hilos():
    for link in archivo_a_lista(ARCHIVO_COLA):
        queue.put(link)
    queue.join()
    obtener_urls()

def obtener_urls():
    links_cola = archivo_a_lista(ARCHIVO_COLA)
    if len(links_cola) > 0:
        print(str(len(links_cola)) + ' urls en la cola')
        crear_hilos()

crear_spiders()
obtener_urls()


