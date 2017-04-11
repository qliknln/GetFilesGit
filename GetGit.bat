@echo ********Get files from Bitbucket git***********

@echo Running this script, will replace all files and folder located in the
@echo folder specified as 'repo_dir' in 'Repository_data.py'
@echo off

SET /p UserInput= Do you wish to continue [y/n]
if "%UserInput%" == "y" (
@echo Downloading...
python Get_files.py
)
