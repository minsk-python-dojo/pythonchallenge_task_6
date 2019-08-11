import os
import unittest

from task import download_zip_file, save_downloaded_file 


class TestDownload(unittest.TestCase):

    def setUp(self):
        self.url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
        self.dest_path = os.path.join(os.path.abspath('data'), 'channel.zip') 
        self.binary_str = b'sdbjfjhdsgjhfjdhsfgjh'

    def test_download_zip_file(self):
        # downolad 
        is_download_succesfull = download_zip_file(self.url, self.dest_path)
        self.assertTrue(is_download_succesfull)

    def test_downloaded_exists(self):
        #check file exists
        download_file_exists = save_downloaded_file(self.dest_path, self.binary_str)
        self.assertTrue(os.path.exists(self.dest_path))
    
    def test_downloaded_content_equals_expected(self):
        save_downloaded_file(self.dest_path, self.binary_str)
        with open(self.dest_path, 'rb') as file:
            content = file.read()
        self.assertEqual(content, self.binary_str)



