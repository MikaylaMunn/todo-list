# To Do App Project

## About
This is a simple todo app undertaken for the purpose of learning the Django framework hands-on without having to attend to front-end matters. The project was completed in two phases:
    Phase 1: Completion of elements that allow the user to keep a list of tasks to do and mark them as complete or update or delete them. It also allows the user to navigate to a notes page in which notes can be created and deleted.
    Phase 2: Completion of elements that allow the users to add and remove tags to any task, so the logics for one-to-many and many-to-many relationships of database data would have to be implemented on the backend.

## Usuage
- To clone a copy of this project using https, run the following command in the command line:<br>
``` git clone https://github.com/MikaylaMunn/todo-list ```
- In the same directory as <your_project_directory_name>/todosite/todosite/settings.py file, create a .env file and, in it, save a secret key that you create. You may generate a key in the terminal like so:<br>
```$ shasum<<<test ```
- A hash will be generated and printed to the terminal, which you can use as the key, or just type a long alphanumberal+symbols, and save it in the .env file, like so:<br>
```SECRET_KEY=<the_hash_you_generated>```
- Create a Python virtual environment and activate it in your local project: (assuming you already have Python installed) <br>
```$ cd <your_project_directory_name>```<br>
```$ python3 -m venv venv```<br>
```$ . venv/bin/activate```

- Install the packages from requirements.txt:  
```$ pip install -r requirements.txt```

- In the <your_project_direcotry_name>/todosite/ directory run the following command to start the server: <br>
```$ cd todosite ``` <br>
```$ python3 manage.py runserver```
