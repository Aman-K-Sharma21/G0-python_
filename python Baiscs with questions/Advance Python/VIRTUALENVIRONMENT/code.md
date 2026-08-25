#install virtual environment
pip install virtualenv

#creating a virtual environment
virtualenv <name of the virtual Environment>

#allowing script execution , use this command in the terminal

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

#to install modules
pip install <name of the module>

#to get the requirement file, run this code inside virtual environment
pip freeze > requirements.txt

#to install all the modules inside requirement.txt , we use this command
pip install -r .\requirements.txt

#if i want that my new virtual environment already contain all the packages that my system interpreter does, we use that command

virtualenv --system-site-packages <name of the virtual environment>

