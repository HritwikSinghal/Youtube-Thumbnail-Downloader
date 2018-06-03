# youtube videos thumbnail downloader and resizer and alse cropper (all at once)
# created by Hritwik Singhal on 28-05-2018: 03:20

# i am a newbie to python(and programming), so you can assume that this piece is
# poorly written, poorly commented etc etc
# Also, you can modify functions as per your need.

import urllib
from PIL import Image


# you should have a list of ID of videos,separated by new line,
# in a file called 'ids' with no file extension
def download_image(ids):
    ID_list = []
    for x in open(ids).read().split():
        y = x.strip()
        ID_list.append(y[32:43])

    # take ID of video
    for one_ID in ID_list:
        ID = one_ID

        # insert ID in url of image
        url = 'https://img.youtube.com/vi/' + ID + '/maxresdefault.jpg'

        # Naming of images
        name = ID + '.jpg'

        # downloading the image
        urllib.urlretrieve(url, name)

        img_open = Image.open(name)

        # the image is 1280* 720
        # resizing the image
        resize_img = img_open.resize((900, 600))

        # Cropping image
        # This crops the middle 500*500 portion of image
        crop_area = (200, 50, 700, 570)
        cropped_img = resize_img.crop(crop_area)
        cropped_img.save(name)


download_image('ID.txt')

