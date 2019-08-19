import io
from dataclasses import dataclass
import os
from typing import List, Dict
import zipfile
import pprint

import requests 

ZIP_URL = 'http://www.pythonchallenge.com/pc/def/channel.zip'
DEST_DIR_PATH = os.path.abspath('data')
DEST_PATH = os.path.join(DEST_DIR_PATH, 'channel.zip')
START_FILE_NAME = 90052

@dataclass
class ZippedFile:
    name: str
    comment: str
    next_name: str

def save_downloaded_file(dest_path: str, file_content: bytes) -> bool:
    with open(dest_path, 'wb') as file:
        bytes_written = file.write(file_content)
    file_wrote_corectly = len(file_content) == bytes_written
    return file_wrote_corectly 


def download_zip_file(url: str) -> bytes:
    response = requests.get(url)
    return response.content

def get_zip_comments(file_path: str) -> Dict[str, str]:
    with zipfile.ZipFile(file_path, 'r') as file:
        info_list = file.infolist()

    comments: dict = {info.filename.split('.')[0] : info.comment.decode()  for info in info_list}
    return comments

def extract_files(file_path: str, dest_path: str):
    zipfile.ZipFile(file_path).extractall(dest_path)

def get_next_name(file_content: str) -> str:
    next_name = file_content.split()[-1]
    return next_name

def ordered_comment_generator(next_name: str) -> ZippedFile:
    try:
        int(next_name)
    except ValueError:
        yield None
    with open(os.path.join(DEST_DIR_PATH, f'{next_name}.txt'), 'r') as file:
        content = file.read()
    zipped_file_obj = ZippedFile(name = next_name, comment = None, next_name = get_next_name(content))
    yield zipped_file_obj

def main():
    zip_content = download_zip_file(ZIP_URL)
    save_downloaded_file(DEST_PATH, zip_content)
    extract_files(DEST_PATH, DEST_DIR_PATH)
    comments: dict = get_zip_comments(DEST_PATH)
    current_link = START_FILE_NAME
    final_comment = ''
    while True:
        zipped_file_obj = next(ordered_comment_generator(current_link))
        if not zipped_file_obj:
            break
        zipped_file_obj.comment = comments.get(zipped_file_obj.name)
        if zipped_file_obj.comment:
            final_comment += zipped_file_obj.comment
        print(zipped_file_obj)
        current_link = zipped_file_obj.next_name
    print(final_comment)
    # pprint.pprint(comments)

if __name__ == '__main__':
    main()    