from pyxnat import Interface

def get_XNAT(username, password, xnat_cache, xnatUrl='https://xnat.hdni.org/xnat'):
    xnat = Interface(server=xnatUrl, user=username, password=password,
                     cachedir=xnat_cache)
    return xnat
