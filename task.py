import io
import os
from typing import List
import zipfile

import requests 

ZIP_URL = 'http://www.pythonchallenge.com/pc/def/channel.zip'
DEST_PATH = os.path.join(os.path.abspath('data'), 'channel.zip')

def save_downloaded_file(dest_path: str, file_content: bytes) -> bool:
    with open(dest_path, 'wb') as file:
        bytes_written = file.write(file_content)
    file_wrote_corectly = len(file_content) == bytes_written
    return file_wrote_corectly 


def download_zip_file(url: str) -> bytes:
    response = requests.get(url)
    return response.content

def get_zip_comments(file_path: str) -> List[str]:
    with zipfile.ZipFile(file_path, 'r') as file:
        info_list = file.infolist()
    comments_list = [info.comment.decode() for info in info_list]
    return comments_list

def main():
    zip_content = download_zip_file(ZIP_URL)
    save_downloaded_file(DEST_PATH, zip_content)
    comments_list = get_zip_comments(DEST_PATH)
    import pprint

    pprint.pprint(comments_list)

if __name__ == '__main__':
    main()    