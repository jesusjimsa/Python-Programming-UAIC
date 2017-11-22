# Create a script that displays the following system information:
#	- Python version used. If Python 2 is used, Python 2 will also display the "=== Python 2 ==="
# 	  message, and if Python 3 is used, it will display the "Running under Py3" message
# 	  (hint: sys.version_info)
#	- The name of the user who executed the script
#	- The complete script path
#	- The path of the directory where the script is located
#	- Type of operating system
#	- The number of cores
#	- The directories in the PATH process one by one

import sys, os, multiprocessing

# Colors for displaying the answers
GREEN = '\033[32m'
BLUE = '\033[34m'
RED = '\033[31m'
RESET = '\033[0m'

# Python version used
print GREEN + "Python version" + RESET

if sys.version_info.major == 2:
	print BLUE +  "=== Python 2 ===" + RESET
else:
	print "Running under Py3"

# The name of the user who executed the script
print GREEN + "Username" + RESET
print BLUE +  os.getlogin() + RESET

# The complete script path
print GREEN + "Script path" + RESET
print BLUE  + os.path.realpath(__file__) + RESET

# The path of the directory where the script is located
print GREEN + "Path of the directory where the script is located" + RESET
print BLUE + os.path.dirname(os.path.realpath(__file__)) + RESET

#Type of operating system
print GREEN + "Operating system" + RESET

system = sys.platform

if system == "linux2":
	print BLUE + "Linux" + RESET
elif system == "win32":
	print BLUE + "Windows" + RESET
elif system == "darwin":
	print BLUE + "macOS" + RESET
else:
	print RED + "Unknown OS" + RESET

# The number of cores
print GREEN + "Number of cores" + RESET
print BLUE + str(multiprocessing.cpu_count()) + RESET

# The directories in the PATH process one by one
path = os.path.realpath(".")

print GREEN + "These are the directories in " + path + RESET
for a in os.listdir(path):
	if os.path.isdir(os.path.join(path, a)):
		print BLUE + os.path.join(path, a) + RESET