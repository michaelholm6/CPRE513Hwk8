This readme assumes the following:

You're running this script on Ubuntu.

You're able to compile java programs using the command line tool "javac program.java"

You're able to run compiled java programs using the command line tool "java program [args]"

You have venv, Python, and pip installed.

If you're not running on Ubuntu, or some Linux based operating system, I don't think this program will work. 

If you're not able to compile java programs using the command line, 
run the command "sudo apt-get install openjdk-8-jdk"

If you're not able to run compiled java programs using the command line, 
run the command "sudo apt-get install openjdk-8-jre"

If you don't have python, install it using the command "sudo apt update" then "sudo apt install python3"

If you don't have pip, install it using the command "sudo apt update" then "sudo apt install python3-pip"

If you don't have venv, install it using the command "python --version" to check your version of python,
then run "sudo apt install python<version>-venv", replacing <version> with the first two version of numbers of
your python. For example, if you have python 3.10.12, replace <version> with 3.10 

Once this is all setup, find the requirements.txt file in the same folder as this file.

Run the command "python -m venv <environment_name>" replacing <environment_name> with any name.

Run the command "source <environment_name>/bin/activate" to activate the environment.

Run the command "pip install -r <path/to/requirements.txt>"

Now, you must have two source code files you are planning to debug with this script. For this assignment, these source code files are file1v1.java and file1v2.java.
Because these two source code files have a public class named file1v1 declared in them, you must rename file1v2.java to file1v1.java, and store it in some
seperate directory from the original file1v1.java.

Next, both of the file1v1.java source code files must have any package declarations at line 1 deleted, and those changes saved.

Finally, run the script using the command "python3 <path/to/CPRE_513_HWK_8.py>"

Follow the terminal prompts that this script creates.

