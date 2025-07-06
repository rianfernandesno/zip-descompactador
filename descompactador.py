from pathlib import  Path
from zipfile import ZipFile


home = Path.home() / "Downloads"

zipados = home / "zipados"
destino = home / "descompactados"

zipados.mkdir(exist_ok=True)
destino.mkdir(exist_ok=True)

arquivos = zipados.iterdir()

for arquivo in arquivos:
    if arquivo.is_file() and arquivo.suffix == ".zip" :
        try:
            destino_pasta = Path(destino / arquivo.stem)
            destino_pasta.mkdir(exist_ok=True)
            with ZipFile(arquivo, 'r') as zip:
                zip.extractall(destino_pasta)
        except:
            continue