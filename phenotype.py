#!/usr/bin/env python3

############################################################
# Based on code from Andy Lin and Monica Tessman
# Usage: python phenotype.py <NAME>
# Program takes a picture with attached camera and saves to computer
############################################################

import json
import paramiko
from subprocess import call


def main():
    """Function that contains the main part of the code

    :return:
    """

    # Read the database connection configuration file
    config = open("config.json", 'rU')
    # Load the JSON configuration data
    conf = json.load(config)

    # SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(conf['hostname'], username=conf['username'], password=conf['password'])
    sftp = ssh.open_sftp()

    # use gphoto2 --auto-detect to check camera is still attached
    call(["gphoto2", "--auto-detect"])

    print(" ")
    print("taking picture")

    filename = "image.jpg"

    # Take a picture
    camera_capture(filename)

    # Copy picture to server
    try:
        sftp.put(conf['path'], filename)
    except IOError as e:
        print("I/O error({0}): {1}. Offending file: {2}".format(e.errno, e.strerror, conf['path']))


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
