# Introduction to Linux

In this session we will learn to work with command-line Linux. For detailed information about the Bioinformatics Core Facility, see [here](https://github.com/danforthcenter/bioinformatics/wiki). 

# Outline
1. Connecting to a remote server
2. Basic file operations
3. A brief overview of using the cluster

# Connecting to a remote server

To connect to the Danforth Center Bioinformatics cluster we will use Secure Shell (SSH). The three pieces of information you need to connect are the hostname of the server, your username, and your password. In a terminal program the command will take the form: 

```
ssh <username>@<hostname>
```

For programs like PuTTY, you will enter this information into a form to connect.

Once connected, try changing your password:

```
passwd
```

You should be prompted with the following:

```
Changing password for user <username>.
(current) LDAP Password:
New password:
Retype new password:
```

# Basic Linux operations

## Basic Linux shell commands

**pwd** - print the current working directory path

**ls** - list the files and directories in the current working directory

**cd** - change directories directly to *home*

**cd** ***dir*** - change directories from the current working directory to *dir*

**touch** ***file*** - create the empty file *file*

**rm** ***file*** - remove the file *file*

**mkdir** ***dir*** - make the directory *dir*

**rmdir** ***dir*** - remove the directory *dir* (has to be empty)

**cp** ***file1*** ***file2*** - create a copy of *file1* called *file2*

**cp -r** ***dir1*** ***dir2*** - create a copy of *dir1* and its contents called *dir2*

**mv** ***file1*** ***file2*** - move/rename *file1* to *file2*

**head** ***file*** - print the first 10 lines of *file* to *stdout*

**tail** ***file*** - print the last 10 lines of *file* to *stdout*

**less** ***file*** - opens *file* using a paging viewer

**htop** - display the current running processes (task manager/activity monitor). It is a modern version of **top** which should be available if **htop** is not.

**df -h** - display disk usage with human-readable units

**gzip** ***file*** - compress *file*

**gunzip** ***file.gz*** - decompress *file.gz*

**tar zcf** ***archive.tar.gz*** ***dir*** - create a compressed archive of *dir* (or a set of files)

**tar zxf** ***archive.tar.gz*** - decompress and extract the contents of *archive.tar.gz*

**Ctrl+C** - stop the current command

**exit** - log out of the current session



