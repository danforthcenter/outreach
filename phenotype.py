#!/usr/bin/env python3

############################################################
# Based on code from Andy Lin and Monica Tessman
# Usage: python phenotype.py <NAME>
# Program takes a picture with attached camera and saves to computer
############################################################

import argparse
import json
import paramiko
import os
from subprocess import call


def options():
    """

    :return args: argparse object
    """

    parser = argparse.ArgumentParser(description='Phenotyping image capture and image processing demo.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--conf", help="JSON configuration file.", default="config.json")
    parser.add_argument("-d", "--debug", help="Activate debugging.", action="store_true")
    args = parser.parse_args()

    return args


def main():
    """Function that contains the main part of the code

    :return:
    """

    # Parse command-line flags
    args = options()

    # Read the database connection configuration file
    config = open(args.conf, 'rU')

    # Load the JSON configuration data
    conf = json.load(config)

    # SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(conf['hostname'], username=conf['username'], password=conf['password'])
    sftp = ssh.open_sftp()

    filename = "image.jpg"

    if args.debug:
        filename = "seeds.jpg"
    else:
        # use gphoto2 --auto-detect to check camera is still attached
        call(["gphoto2", "--auto-detect"])

        print(" ")
        print("taking picture")

        # Take a picture
        camera_capture(filename)

    # Copy picture to server
    try:
        sftp.put(filename, os.path.join(conf['path'], filename))
    except IOError as e:
        print("I/O error({0}): {1}. Offending file: {2}".format(e.errno, e.strerror, filename))

    sftp.close()
    ssh.close()


def camera_capture(filename):
    """Function to take a picture with a Nikon Coolpix L830

    This function requires the computer to have gphoto2
    installed and uses the module subprocess to write to
    the command line to take pictures

    :param filename: str
    :return:
    """

    # use gphoto2 --capture-image-and-download --filename filename
    # to take the picture and download it with the given name
    call(["gphoto2", "--capture-image-and-download", "--filename", filename])
    print("Image saved: " + filename)


if __name__ == "__main__":
    main()
