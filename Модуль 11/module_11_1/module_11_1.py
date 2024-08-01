import os
import requests
import numpy as np
from PIL import Image
from threading import Thread


class InvertPictures(Thread):
    def __init__(self, number, url):
        super().__init__()
        self.url = url
        self.number = number

    def run(self):
        self.download_picture('original')
        self.grayscale_picture('grayscale')
        self.invert_picture('invert')

    def download_picture(self, folder):
        os.makedirs(folder, exist_ok=True)
        response = requests.get(self.url)
        with open(f'{folder}/{self.number}.jpg', 'wb') as out:
            out.write(response.content)

    def grayscale_picture(self, folder):
        os.makedirs(folder, exist_ok=True)
        img = Image.open(f'original/{self.number}.jpg')
        img = img.convert("L")
        img.save(f'{folder}/{self.number}.png')

    def invert_picture(self, folder):
        os.makedirs(folder, exist_ok=True)
        img = Image.open(f'grayscale/{self.number}.png')
        matrix = np.asarray(img)
        img = Image.fromarray(255 - matrix)
        img.save(f'{folder}/{self.number}.png')


urls = ['https://sun9-11.userapi.com/impg/fkvmiN9f2FV9OAXpN96XRSbYhPa2zWVxdsvk5w/TSti7CZOJhk.jpg?size=1280x768&quality=95&sign=05b1c05e324dce1babf09015ca9ef564&type=album,'
        'https://sun9-22.userapi.com/impg/HfN3s-PYxe_HCkCVH8U5cjX9U5Ioos_q-5Ta0g/3bXSvEWLGDE.jpg?size=1280x791&quality=95&sign=8db2522d133bd945f82380e75b1e535f&type=album',
        'https://sun9-7.userapi.com/impg/9CpDLYrgndYngvvoR88mPQXOtUp9tn1XfOeEmg/t_-2WTqznyI.jpg?size=848x1280&quality=95&sign=9d5e7111d94576e0c3ba0c445cf1d713&type=album',
        'https://sun9-35.userapi.com/impg/RseEFkFh2LcFqFLSUTDMlfToMPkrVjCuhT5kAg/g-SelbARrio.jpg?size=805x1280&quality=95&sign=d3853ce4f9f07ab1a62fa08bd14c4da6&type=album',
        'https://sun4-22.userapi.com/impg/72vwnhKKSabrEUKaqQCJA-NRZaH_Cc_qhiGedg/IPDHH4_f_RE.jpg?size=503x696&quality=95&sign=9da4797046e91b419fad33996e0eb43c&type=album',
        'https://sun9-5.userapi.com/impg/mghEY94J5ajNRpxcwTa2_LlgoLKrhZrU5ZOfwQ/HLU5SfT56lA.jpg?size=1179x860&quality=95&sign=6b93d85a20f37fcb10d0edeae8f23063&type=album']

threads = []
for i, e in enumerate(urls):
    t = InvertPictures(number=i+1, url=e)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
