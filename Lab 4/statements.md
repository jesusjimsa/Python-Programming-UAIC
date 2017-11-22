# Lab 4

1. Write a python program to receive two numbers from the command line (a and b) and display:  
a) a - b  
b) a + b  
c) a / b  
d) a * b  

2. Write a script which takes as parameter from the command line a path and displays the first 4096 bytes if the path leads to a file, it's entries if the path is a directory and an error message if the path is not a valid one.

3. Write a function that receives a filename as a parameter and writes the data from the os.environ in the file, each line containing an entry in this dictionary, in the form of the key [tab] value.

4. Write a function that receives as a parameter a path that represents a directory on the system, recursively browses the file structure and directories that it contains and displays in the console all the paths it has travelled. You are NOT allowed to use os.walk.

5. Write a script that receives 2 parameters from the console representing a path to a directory on the system and a file name. The script will recursively navigate to the file structure and directories in the given directory as a parameter using os.walk and write in the file given as a parameter all sites path you travelled and it's type (FILE, DIRECTORY, UNKNOWN), separated by |. Each path will be written on one line.

6. Write a script that receives 3 parameters from the console. The first one will be a path to a file, the second a path to a directory and the third will be the size of a buffer. Script will copy the given file as a parameter into the given directory as a parameter, using a buffer of the third parameter size, in bytes.

7. Create your own module in which to implement at least 3 functions. Use these functions in a script.

8. Write a script that takes the following arguments: path, tree_depth, filesize, filecount, dircount and create a directory structure deep depth as follows: starting from the root path will be created dircount filecount directories and files containing filesize bytes (only the "a" character for example) and this process will be repeated recursively for each created directory until the desired depth is reached (in directories at the maximum depth, no other directories will be created)  
For example, if we run the script like this: ```python3 create_dummy_tree.py test 2 1024 3 3``` the following structure will be created in the current directory:  
```
    test
    test / dir0
    test / dir0 / file1 (size 1024)
    test / dir0 / file2 (size 1024)
    test / dir0 / file3 (size 1024)

    test / dir1
    test / dir1 / file1 (size 1024)
    test / dir1 / file2 (size 1024)
    test / dir1 / file3 (size 1024)

    test / dir2
    test / dir2 / file1 (size 1024)
    test / dir2 / file2 (size 1024)
    test / dir2 / file3 (size 1024)

    test / file0 (size 1024)
    test / file1 (size 1024)
    test / file2 (size 1024)
```

9. Create a script that displays the following system information:  
- Python version used. If Python 2 is used, Python 2 will also display the "=== Python 2 ===" message, and if Python 3 is used, it will display the "Running under Py3" message (hint: sys.version_info)
- The name of the user who executed the script
- The complete script path
- The path of the directory where the script is located
- Type of operating system
- The number of cores
- The directories in the PATH process one by one

10. Write a search_by_content function that receives two target string and to_search as a parameter and returns a list of files containing to_search. The files are searched as follows: if the target is a file, it is searched only in that file and if it is a directory it will search recursively for all the files in that directory. If the target is neither a file nor a directory, it will drop a ValueError exception with an appropriate message.

11. Write a get_file_info function that receives as a parameter a string representing the path to a file and returns a dictionary with the following fields:
```Python
full_path = # absolute path to the file
file_size = # file size in bytes
file_extension = # file extension (if it has) or ""
can_read = True / False # if you can read from file
can_write = True / False # if you can write to file
```