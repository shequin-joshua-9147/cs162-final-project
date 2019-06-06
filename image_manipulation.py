"""
Manipulate images in specific ways based on commands used on input.

This module is used in order to manipulate images in a number of ways.

All of this is done through the ImageO object. The ImageO object reads in a file and allows for
manipulations to be done on an image and for that image to be output after the manipulation.

All different things this module allows for are:
- make an image only all of its red values
- make an image only all of its green values
- make an image only all of its blue values
- zero out all red values of an image
- zero out all green values of an image
- zero out all blue values of an image
- darken an image by moving all values to be in the lower half of 255
- bright an image by moving all values to be in the upper half of 255
- make image in-to a gray-scaled image
- invert the colors of an image
- block or blur an image, making all pixel of a block the same rgb value

All of these option can be called after importing and creating an ImageO object or from calling
this module from the command line with the proper options.

Joshua Shequin
"""
import argparse
import sys
import numpy as np
from PIL import Image


def common_denominator(number_one, number_two, range_one, range_two):
    """
    Recursion solution to this problem even though it is not the best way of doing it.

    Base case is when the modulo of both numbers and the second range value is zero,
    or if they are the same.

    Parameters
    ----------
    number_one : int
        the first number of the two numbers to find the common denominator between.
    number_two : int
        the second number of the two numbers to find the common denominator between.
    range_one : int
        the lowest integer for a range of values to find the common denominator in.
    range_two : int
        the highest integer for a range of values to find the common denominator in.

    Returns
    ------
    Integer
        the value that the two input have number both have a denominator with, or the lowest int
        in the range given if no denominator was found.

    """
    if number_one % range_two == 0 and number_two % range_two == 0:
        return range_two
    elif range_one == range_two:
        return range_one
    else:
        return common_denominator(number_one, number_two, range_one, range_two-1)


class ImageO:
    """
    Object that handles images, allowing for a number of manipulations.

    Image object that takes an input file as the input and reads that input file and turns that
    image in to an array. From that array the object allows for a number of manipulations to be
    done to the image. Every manipulation also by default outputs the file.
    """

    def __init__(self, input_file):
        """
        Initialize the object by taking an input_file and loading the image to an array.

        Parameter
        ---------
        input_file : string
            string of the file location to be read, relative or full path.
        """
        try:
            self.infile = np.array(Image.open(input_file))  # read in the file and store as a
            # numpy array.
        except FileNotFoundError:
            # if that file did not exist then we warn the user and close the program.
            print("Check your infile parameter, I can't find the file you put in!")
            sys.exit()

    def clear_red(self, output_file, returnable=False):
        """
        Clear all red in our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[0] = 0

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def clear_green(self, output_file, returnable=False):
        """
        Clear all green in our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[1] = 0

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def clear_blue(self, output_file, returnable=False):
        """
        Clear all blue in our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[2] = 0

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def red_only(self, output_file, returnable=False):
        """
        Clear all green and all blue of our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[1] = 0
                column[2] = 0

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def green_only(self, output_file, returnable=False):
        """
        Clear all red and all blue of our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[0] = 0
                column[2] = 0

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def blue_only(self, output_file, returnable=False):
        """
        Clear all red and all green of our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[0] = 0
                column[1] = 0

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def lower_half(self, output_file, returnable=False):
        """
        Scale all shades to be only in the lower 127 of color ints.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[0] = column[0]/2
                column[1] = column[1]/2
                column[2] = column[2]/2

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def upper_half(self, output_file, returnable=True):
        """
        Scale all shades to be only in the upper 127 of color ints.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[0] = column[0]/2 + 128
                column[1] = column[1]/2 + 128
                column[2] = column[2]/2 + 128

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def gray_scale(self, output_file, returnable=False):
        """
        Convert the image to a grey-scale image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                # to transform a pixel to its gray-scale form we find the average of the three
                # colors.
                new_value = (column[0]*(1/3)) + (column[1]*(1/3)) +\
                                                  (column[2]*(1/3))
                column[0] = new_value
                column[1] = new_value
                column[2] = new_value

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def invert_color(self, output_file, returnable=False):
        """
        Invert all rgb values of the image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        for row in self.infile:
            for column in row:
                column[0] = 255 - column[0]
                column[1] = 255 - column[1]
                column[2] = 255 - column[2]

        if returnable:
            return self.infile

        Image.fromarray(self.infile, "RGB").save(output_file)
        return None

    def block_image(self, output_file, returnable=False):
        """
        Blurs or blocks an image, assigning a block size for an image making all pixels the same.

        Calls the common_denominator function to find a common denominator within a range of two
        numbers for two numbers. This will be used to determine the block width and height.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        numpy array
            Return the numpy array of the image if returnable=True
        """
        number_of_blocks = common_denominator(len(self.infile), len(self.infile[0]), 2, 100)
        block_height = len(self.infile)//number_of_blocks
        block_width = int(len(self.infile[0])//number_of_blocks)
        for block_row in range(number_of_blocks):
            for block in range(number_of_blocks):
                block_reds = []  # stores all red values in a block
                block_greens = []  # stores all green values in a block
                block_blues = []  # stores all blue values in a block
                for row in range((block_row * block_height),
                                 (block_row * block_height) + block_height):
                    for column in range((block * block_width),
                                        (block * block_width) + block_width):
                        # go through every pixel in the block and store the rgb values in their
                        # respective lists.
                        block_reds.append(self.infile[row][column][0])
                        block_greens.append(self.infile[row][column][1])
                        block_blues.append(self.infile[row][column][2])
                # find the average of the values in our rgb lists
                avg_of_red = sum(block_reds) // len(block_reds)
                avg_of_green = sum(block_greens) // len(block_greens)
                avg_of_blue = sum(block_blues) // len(block_blues)
                for row in range((block_row * block_height),
                                 (block_row * block_height) + block_height):
                    for column in range((block * block_width),
                                        (block * block_width) + block_width):
                        # go through every pixel in the block and change its rgb values
                        self.infile[row][column][0] = avg_of_red
                        self.infile[row][column][1] = avg_of_green
                        self.infile[row][column][2] = avg_of_blue

        if returnable:
            return self.infile
        Image.fromarray(self.infile, "RGB").save(output_file)
        return None


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Manipulate an Image.')
    PARSER.add_argument('Infile', metavar='I', type=str,
                        help='The file to have the operation performed on it.')
    PARSER.add_argument('Outfile', metavar='O', type=str,
                        help="The name of the outfile from the script.")
    PARSER.add_argument("Operation", metavar="o", type=str,
                        help='Which operation would you like performed? Options:'
                             ' cr - clear all red;'
                             ' cg - clear all green;'
                             ' cb - clear all blue;'
                             ' ro - make the image only shades of red;'
                             ' go - make the image only shades of green;'
                             ' bo - make the image only shades of blue;'
                             ' lh - make colors all be in lower half;'
                             ' uh - make colors all be in upper half;'
                             ' gs - make the image gray-scale;'
                             ' ic - invert the colors of the image;'
                             ' bi - block the image in to same color cubes of pixels')

    ARGS = PARSER.parse_args()

    if ARGS.Operation not in ["cr", "cg", "cb", "ro", "go", "bo", "lh", "uh", "gs", "ic", "bi"]:
        print("Not a valid operation, please use the argument -h for extra help.")
        sys.exit()

    if ARGS.Operation == "cr":
        ImageO(ARGS.Infile).clear_red(ARGS.Outfile)
    elif ARGS.Operation == "cg":
        ImageO(ARGS.Infile).clear_green(ARGS.Outfile)
    elif ARGS.Operation == "cb":
        ImageO(ARGS.Infile).clear_blue(ARGS.Outfile)
    elif ARGS.Operation == "ro":
        ImageO(ARGS.Infile).red_only(ARGS.Outfile)
    elif ARGS.Operation == "go":
        ImageO(ARGS.Infile).green_only(ARGS.Outfile)
    elif ARGS.Operation == "bo":
        ImageO(ARGS.Infile).blue_only(ARGS.Outfile)
    elif ARGS.Operation == "lh":
        ImageO(ARGS.Infile).lower_half(ARGS.Outfile)
    elif ARGS.Operation == "uh":
        ImageO(ARGS.Infile).upper_half(ARGS.Outfile)
    elif ARGS.Operation == "gs":
        ImageO(ARGS.Infile).gray_scale(ARGS.Outfile)
    elif ARGS.Operation == "ic":
        ImageO(ARGS.Infile).invert_color(ARGS.Outfile)
    elif ARGS.Operation == "bi":
        ImageO(ARGS.Infile).block_image(ARGS.Outfile)
