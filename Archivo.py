import os

def crear_directorio_proyecto(directorio):
    if not os.path.exists(directorio):
        print('Creando el directorio: ' + directorio)
        os.makedirs(directorio)

def crear_archivos_datos(nombre_proyecto, base_url):
    queue = nombre_proyecto + '/queue.txt'
    crawled = nombre_proyecto + '/crawled.txt'
    if not os.path.isfile(queue):
        escribir_archivo(queue, base_url)
    if not os.path.isfile(crawled):
        escribir_archivo(crawled, '')

def escribir_archivo(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def anadir_al_fichero(path, data):

    with open(path, 'a') as file:
        file.write(data + '\n')

def archivo_a_lista(nombre_archivo):
    lista = set()
    with open(nombre_archivo, 'rt') as f:
        for line in f:

            lista.add(line.replace('\n', ''))
    return lista

def lista_a_archivo(links, nombre_archivo):
    for link in sorted(links):
        anadir_al_fichero(nombre_archivo, link)




