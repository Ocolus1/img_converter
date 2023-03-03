from rembg import remove
from PIL import Image

import os
import string
from random import choices


APPS_DIR = "img_converter/removebg"


class Remove:
    """ This class removes the background image of a picture"""
    def __init__(self, img, format=None):
        self.format = format
        self.img = img


    def generate_name(self):
        """ This function generates a random name for the image"""
        characters = string.digits + string.ascii_letters
        char = "".join(choices(characters, k=10))
        name = self.img.name.split(".")[0] + char + "." + self.format
        return name

    def removeBackgroundImage(self):
        """ This function removes the background image of a picture"""

        # calls the generate_name function to get a random name
        name = self.generate_name()

        # sets the output path of the file
        output_path = f"{APPS_DIR}/download/{name}"

        input = Image.open(self.img)
        output = remove(input)

        # saves the image to the output path
        output.save(output_path)

        return output_path

