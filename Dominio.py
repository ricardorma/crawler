from urllib.parse import urlparse

def obtener_dominio(url):
    try:
        resultado = obtener_subdominio(url).split('.')
        return resultado[-2] + '.' + resultado[-1]
    except:
        return ''

def obtener_subdominio(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

