"""
Manipulate images in specific ways based on commands used on input.

This module is used in order to manipulate images in a number of ways and also to do some
preliminary detection within images for things like numbers on a blank background etc.

Functions of this module:

Joshua Shequin
"""
from PIL import Image
import numpy as np
import argparse
import sys


def lowest_common_denominator(number_one, number_two):
    # TODO
    # recursion solution to this problem even though it is not the best way of doing it.
    if number_one == number_two:
        return number_one


class ImageO:
    """

    """
    def __init__(self, input_file):
        try:
            self.infile = np.array(Image.open(input_file))  # read in the file and store as a
            # numpy array.
        except FileNotFoundError:
            # if that file did not exist then we warn the user and close the program.
            print("Check your infile parameter, I can't find the file you put in!")
            sys.exit()

    def cr(self, output_file):
        """
        Clear all red in our image

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """
        for row in self.infile:
            for column in row:
                column[0] = 0

        Image.fromarray(self.infile, "RGB").save(output_file)

    def cg(self, output_file):
        """
        Clear all green in our image

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """
        for row in self.infile:
            for column in row:
                column[1] = 0

        Image.fromarray(self.infile, "RGB").save(output_file)

    def cb(self, output_file):
        """
        Clear all blue in our image

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """
        for row in self.infile:
            for column in row:
                column[2] = 0

        Image.fromarray(self.infile, "RGB").save(output_file)

    def ro(self, output_file):
        """
        Clears all green and all blue of our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """
        for row in self.infile:
            for column in row:
                column[1] = 0
                column[2] = 0

        Image.fromarray(self.infile, "RGB").save(output_file)

    def go(self, output_file):
        """
        Clears all red and all blue of our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """
        for row in self.infile:
            for column in row:
                column[0] = 0
                column[2] = 0

        Image.fromarray(self.infile, "RGB").save(output_file)

    def bo(self, output_file):
        """
        Clears all red and all green of our image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """
        for row in self.infile:
            for column in row:
                column[0] = 0
                column[1] = 0

        Image.fromarray(self.infile, "RGB").save(output_file)

    def lh(self, output_file):
        """
        Scales all shades to be only in the lower 127 of color ints.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """

        for row in self.infile:
            for column in row:
                column[0] = column[0]/2
                column[1] = column[1]/2
                column[2] = column[2]/2

        Image.fromarray(self.infile, "RGB").save(output_file)

    def uh(self, output_file):
        """
        Scales all shades to be only in the upper 127 of color ints.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """

        for row in self.infile:
            for column in row:
                column[0] = column[0]/2 + 127
                column[1] = column[1]/2 + 127
                column[2] = column[2]/2 + 127

        Image.fromarray(self.infile, "RGB").save(output_file)

    def gs(self, output_file):
        """
        Converts the image to a grey-scale image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """

        for row in self.infile:
            for column in row:
                new_value = (column[0]*(1/3)) + (column[1]*(1/3)) +\
                                                  (column[2]*(1/3))
                column[0] = new_value
                column[1] = new_value
                column[2] = new_value

        Image.fromarray(self.infile, "RGB").save(output_file)

    def ic(self, output_file):
        """
        Inverts all rgb values of the image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """

        for row in self.infile:
            for column in row:
                column[0] = 255 - column[0]
                column[1] = 255 - column[1]
                column[2] = 255 - column[2]

        Image.fromarray(self.infile, "RGB").save(output_file)

    def bi(self, output_file):
        """
        Inverts all rgb values of the image.

        Parameter
        ---------
        output_file : string
            the name of the file we want to output to.
        Return
        ------
        None
        """
        number_of_blocks = 100
        block_height = len(self.infile)//number_of_blocks
        block_width = len(self.infile[0])//number_of_blocks
        for block_row in range(number_of_blocks):
            for block in range(number_of_blocks):
                block_reds = []
                block_greens = []
                block_blues = []
                for row in range((block_row * block_height), (block_row * block_height) + block_height):
                    for column in range((block * block_width), (block * block_width) + block_width):
                        block_reds.append(self.infile[row][column][0])
                        block_greens.append(self.infile[row][column][1])
                        block_blues.append(self.infile[row][column][2])
                avg_of_red = sum(block_reds) // len(block_reds)
                avg_of_green = sum(block_greens) // len(block_greens)
                avg_of_blue = sum(block_blues) // len(block_blues)
                for row in range((block_row * block_height), (block_row * block_height) + block_height):
                    for column in range((block * block_width), (block * block_width) + block_width):
                        self.infile[row][column][0] = avg_of_red
                        self.infile[row][column][1] = avg_of_green
                        self.infile[row][column][2] = avg_of_blue
            print(f"Finished block number: {block*block_row+1} out of {number_of_blocks * number_of_blocks}")
        Image.fromarray(self.infile, "RGB").save(output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manipulate an Image.')
    parser.add_argument('Infile', metavar='I', type=str,
                        help='The file to have the operation performed on it.')
    parser.add_argument('Outfile', metavar='O', type=str,
                        help="The name of the outfile from the script.")
    parser.add_argument("Operation", metavar="o", type=str,
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

    args = parser.parse_args()
    operation_options = ["cr", "cg", "cb", "ro", "go", "bo", "lh", "uh", "gs", "ic", "bi"]

    if args.Operation not in operation_options:
        print("Not a valid operation, please use the argument -h for extra help.")
        sys.exit()

    image_operable = ImageO(args.Infile)

    if args.Operation == "cr":
        image_operable.cr(args.Outfile)
    elif args.Operation == "cg":
        image_operable.cg(args.Outfile)
    elif args.Operation == "cb":
        image_operable.cb(args.Outfile)
    elif args.Operation == "ro":
        image_operable.ro(args.Outfile)
    elif args.Operation == "go":
        image_operable.go(args.Outfile)
    elif args.Operation == "bo":
        image_operable.bo(args.Outfile)
    elif args.Operation == "lh":
        image_operable.lh(args.Outfile)
    elif args.Operation == "uh":
        image_operable.uh(args.Outfile)
    elif args.Operation == "gs":
        image_operable.gs(args.Outfile)
    elif args.Operation == "ic":
        image_operable.ic(args.Outfile)
    elif args.Operation == "bi":
        image_operable.bi(args.Outfile)
