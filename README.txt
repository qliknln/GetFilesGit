***************Bitbucket utility for Qlik@Qlik only***************
This script is only intended for the Qlik@QlikIT team. All usage
outside this department is not allowed nor supported.
******************************************************************

This is a script that pulls a number of specified folders, and the files
within, from the specified Bitbucket Git to a local folder on disk.
It then iterates the downloaded files, looks for the % character in the
filename and replaces that with an _ (underscore). If the file has the
.profile extension, it will be copied to another folder with the "_renamed" suffix and
renamed to .profile.xml

All parameters:
- Bitbucket URL
- Log in credentials
- The path the local target folder
- List of folders to retrieve from the specified Git.
Are specified in the Repository_data.py.

Prerequisites:
To successfully run this script, you need to have the following runtimes installed:
Python 2.7 (https://www.python.org/downloads/windows/)
Git (https://git-scm.com/downloads)

After installing the Python 2.7 runtime, you also need to install the gitpython
code package (https://github.com/gitpython-developers/GitPython).
To do this, open a command promt as administrator and type the following:
pip install GitPython

To run this script, run the GetGit.bat file as administrator.

To get support and/or guidance, please feel free to contact me at:
niklas.lagesson@qlik.com
or
Skype: niklas_ln
