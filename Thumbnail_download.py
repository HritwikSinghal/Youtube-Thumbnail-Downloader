# youtube videos thumbnail downloader and resizer and alse cropper (all at once)
# created by Hritwik Singhal on 28-05-2018: 03:20

# i am a newbie to python(and programming), so you can assume that this piece is
# poorly written, poorly commented etc etc
# Also, you can modify functions as per your need.

# you should have a list of ID of videos,separated by new line,
# in a file called 'ids' with no file extension

import os
import re

import requests
from PIL import Image
from bs4 import BeautifulSoup


def download_image(ID, url):
    # insert ID in url of image
    img_url = 'https://img.youtube.com/vi/' + ID + '/maxresdefault.jpg'

    # Naming of images
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = str(soup.title)
    title = re.findall(r'<title>(.*)- YouTube</title>', title)[0].strip()
    name = title + '.jpg'

    # downloading the image
    print("Downloading '{0}'.....".format(title))
    raw_data = requests.get(img_url, stream=True)
    with open(name, "wb") as raw_img:
        for chunk in raw_data.iter_content(chunk_size=2048):
            if chunk:
                raw_img.write(chunk)
    print("Download Successful")

    img = Image.open(name)

    # the image is 1280* 720
    # resizing the image
    img = img.resize((900, 600))

    # Cropping image
    # This crops the middle 500*500 portion of image
    crop_area = (200, 50, 700, 570)
    img = img.crop(crop_area)
    img.save(name)


def start():
    os.chdir(os.getcwd())

    if os.path.isfile('ID.txt'):
        for line in open('ID.txt').read().split("\n"):
            if line.strip().startswith('https://www.youtube.com/'):
                url = line
                video_id = url.strip()[32:43]
                try:
                    download_image(video_id, url)
                except:
                    print("There was some Error")

    else:
        print("Couldn't find 'ID.txt' file.")

        while True:
            url = input("Enter Youtube URL.\n")

            if url.strip().startswith('https://www.youtube.com/'):
                video_id = url.strip()[32:43]
                try:
                    download_image(video_id, url)
                except:
                    print("There was some Error")
            else:
                print("Wrong URL entered. Enter url in this format: 'https://www.youtube.com/watch?v=EOfCEhWq420'")


start()
