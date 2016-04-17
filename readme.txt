1) Installation

You need to have Python 3 (3.4 or later) installed on your PC, 
also you need Python utilities "pip" and "virtualenv".

To launch the django app, you need:
1. cd to a directory of your choice (eg: cd ~/prj)
2. git clone https://github.com/igrik6556/MiloSolutions_tasks.git
3. virtualenv milo-tasks --no-site-packages
   a) cd milo-tasks/bin/
   b) . activate
   c) cd ../../
4. cd MiloSolutions_tasks/dj_task
5. pip3 install -r requirements.txt
6. python3 manage.py runserver
7. open http://localhost:8000/ in your browser
   Notes: Django app comes with a preinstalled database. 
   If you want clear the database, follow these steps:
   	1. rm db.sqlite3
   	2. python3 manage.py migrate
   	A new database will be created then.

To launch a Python app, you need to follow Django app instructions up to the point 3 (including). 
Then:
...
4. cd MiloSolutions_tasks/python_task
5. python3 py_task.py
   Notes: to change input date, need change date in file date.txt

2) Release Notes

1. Created "py_task" script to solve a task for Python test.
2. Created project "dj_task" to solve a task for Django test.
   - Created code to add, remove, edit and view single user.
   - Solved additional task that allows to export CSV-file in excel-format.
   - Tests not designed.
