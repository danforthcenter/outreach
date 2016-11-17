#!/usr/bin/env python

############################################################
# Based on code from Andy Lin and Monica Tessman
# Usage: python phenotype.py <NAME>
# Program takes a picture with attached camera and saves to computer
############################################################

import argparse
import json
import paramiko
import os
import sys
from subprocess import call


def options():
    """

    :return args: argparse object
    """

    parser = argparse.ArgumentParser(description='Phenotyping image capture and image processing demo.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--conf", help="JSON configuration file.", default="config.json")
    parser.add_argument("-d", "--debug", help="Activate debugging.", action="store_true")
    parser.add_argument("-e", "--exp",
                        help="Experiment. Options = arabidopsis, indigo, cassava, sorghum-seed", default="sorghum-seed")
    args = parser.parse_args()

    if args.exp not in ['arabidopsis', 'indigo', 'cassava', 'sorghum-seed']:
        print("{0} is not a valid experiment\n".format(args.exp))
        sys.exit(1)

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

    filename = args.exp + ".jpg"
    path = "."

    if args.debug:
        path = "sample-data"
    else:
        # use gphoto2 --auto-detect to check camera is still attached
        call(["gphoto2", "--auto-detect"])

        print(" ")
        print("Taking picture")

        # Take a picture
        camera_capture(os.path.join(path, filename))

    # Copy picture to server
    print("Transferring image to server")
    try:
        sftp.put(os.path.join(path, filename), os.path.join(conf['www-path'], filename))
    except IOError as e:
        print("I/O error({0}): {1}. Offending file: {2}".format(e.errno, e.strerror, filename))

    print("Analyzing image")
    cmds = ["export PYTHONPATH=" + conf['plantcv-path']]

    if args.exp == 'indigo':
        opts = ["--image", os.path.join(conf['www-path'], filename), "--outdir", conf["www-path"]]
        cmds.append(os.path.join(conf['git-path'], "indigo-phenotyping.py " + " ".join(map(str, opts))))
    elif args.exp == 'arabidopsis':
        opts = ["--image", os.path.join(conf['www-path'], filename), "--outdir", conf["www-path"]]
        cmds.append(os.path.join(conf['git-path'], "arabidopsis-phenotyping.py " + " ".join(map(str, opts))))
    elif args.exp == 'cassava':
        opts = ["--image", os.path.join(conf['www-path'], filename), "--outdir", conf["www-path"]]
        cmds.append(os.path.join(conf['git-path'], "cassava-phenotyping.py " + " ".join(map(str, opts))))
    elif args.exp == 'sorghum-seed':
        opts = ["--image", os.path.join(conf['www-path'], filename), "--outdir", conf["www-path"],
                "--mask", os.path.join(conf["git-path"], "sample-data/seed-mask.jpg")]
        cmds.append(os.path.join(conf['git-path'], "sorghum-seed-phenotyping.py " + " ".join(map(str, opts))))

    stdin_, stdout_, stderr_ = ssh.exec_command(';'.join(map(str, cmds)))
    stderr_.channel.recv_exit_status()
    lines = stderr_.readlines()
    for line in lines:
        print(line)

    sftp.close()
    ssh.close()
    if args.debug is False:
        os.remove(filename)


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
