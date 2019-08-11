import zipfile 
import requests 
import io


def download_zip_file(url: str, dest_path: str) -> bool:
    response = requests.get(url)
    with open(dest_path, 'wb') as file:
        file.write(response.content)
    return True
