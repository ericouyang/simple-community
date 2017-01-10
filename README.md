Simple Community
==============

Development Setup
-----

1. Install `virtualenv` (Python package manager) globally

  `pip install virtualenv`

2. Create a new virtualenv named `simple_community` in a convenient location on your machine outside of the `simple-community` project folder

  `virtualenv simple_community`

3. Navigate into the created `simple_community` folder and activate the virtualenv

  `source bin/activate`

4. Move the `simple-community` project root folder inside the `simple_community` virtualenv folder

5. Navigate into `simple_community` project folder

6. Install Python dependencies via pip:

  `pip install -r requirements.txt`

7. Migrate the development sqlite database

  `./manage.py migrate`

8. Run the development server on port 8000

  `./manage.py runserver`

9. Navigate in your browser to `http://localhost:8000`

On Windows, start by following the instructions for [installing Python, PIP, Setuptools, and Django](https://docs.djangoproject.com/en/dev/howto/windows/).

1. Install Python (recommended version 2.7 or higher) or check which version of Python you have:

  `python --version`

2. Install Setuptools. Please uninstall previous versions first. If you have Powershell, you can install Setuptools with the following command in Powershell (run with administrative privileges):

  `(Invoke-WebRequest https://bootstrap.pypa.io/ez_setup.py).Content | python -`

   or you can download [ez_setup.py](https://bootstrap.pypa.io/ez_setup.py) and run the script. Verify that you've installed Setuptools by checking your Python Scripts directory (generally at C:/PythonXX/Scripts). Add this folder and its parent (by default, at C:/PythonXX) to your PATH if they aren't there already.

3. If your Python version is 3.4 or higher, you already have PIP installed. For other versions of Python, run this in a command prompt:

  `easy_install pip`

4. Install Django 1.7 by running the following command:

  `pip install django`

   Verify the Django version with the following command:

  `django-admin --version`

5. Install SQLite. Download the precompiled binaries for Windows [here](http://www.sqlite.org/download.html). Extract the ZIP file into a directory and move/rename that directory to C:/sqlite. Verify that SQLite is installed with the `sqlite3` command in a command prompt.

6. Continue from step 1 of the instructions for Mac OS.
