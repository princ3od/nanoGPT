import os
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

current_dir = os.path.dirname(__file__)
input_file_path = os.path.join(current_dir, 'spotify_millsongdata.csv')

if not os.path.exists(input_file_path):
    print("Downloading spotify_millsongdata.csv...")
    data_url = 'https://firebasestorage.googleapis.com/v0/b/gptathome.firebasestorage.app/o/spotify_millsongdata.zip?alt=media&token=5977db04-9847-44dc-94c7-ded1efc4f150'
    with urlopen(data_url) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(current_dir)
    print("Downloaded spotify_millsongdata.csv")
else:
    print("spotify_millsongdata.csv already exists.")