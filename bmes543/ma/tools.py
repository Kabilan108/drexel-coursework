# Author: Tony Kabilan Okeke <mailto: tko35@drexel.edu>
# Date:   04.17.2022

# Imports
import tempfile as temp
import os, pickle, GEOparse

def tempdir(dirname: str):
    """
    Create path to a temporary directory
    @param dirname
        name of temporary directory
    @return
        path to temporary directory
    """

    name = os.path.join(temp.gettempdir().replace("\\","/"), dirname)
    if not os.path.isdir(name): os.mkdir(name)
    return name

def geodlparse(acc: str):
    """
    Download, parse and cache data from GEO
    @param acc
        A GEO accession
    @return
        a GSE or GPL object
    """

    # Path to temporary directory
    geodir = tempdir('GEO')

    # Download files
    try:
        # Specify file names
        names = [f'{acc}.txt', f'{acc}_family.soft.gz']
        geofile = os.path.join(geodir, names[0 if acc[:3] == 'GPL' else 1])
        cachefile = os.path.join(geodir, f"{acc}.pkl")

        if os.path.isfile(cachefile):
            # Load data if it has already been cached
            try:
                print('Loading cached data...')
                with open(cachefile, 'rb') as cache:
                    geodata =  pickle.load(cache)
                return geodata
            except Exception as e:
                print(f"ERROR: Loading cached file failed.\n{e}")
        else:
            if os.path.isfile(geofile):
                # If data has already been downloaded, parse it and cache results
                print('Already downloaded. Parsing...')
                geodata = GEOparse.get_GEO(filepath=geofile, silent=True)
            else:
                # Download and parse data
                print('Downloading and parsing...')
                geodata = GEOparse.get_GEO(acc, destdir=geodir, silent=True)
            # Cache data
            with open(cachefile, 'wb') as cache:
                pickle.dump(geodata, file=cache)
            return geodata
    except Exception as e:
        print(f"ERROR: Enter a valid GEO Accension\n{e}")