# TaskTimeTracker
This is an web application which is used to track your productivity based on the amount of time you have devoted to a specific task. The application lets users create their own accounts and add tasks that should be completed or are currently being worked on. Users are allowed to start working on multiple tasks at once and record the amount of time that they have spent on a specific activity. The application supports FaceID login and regular password and username logins. In order to login with FaceID ensure that you have a working web camera.

## Getting Started
To ensure that the program runs properly please ensure that you follow the steps for installing the dependencies

### Installing C++ compiler and CMake tools
[Download](https://visualstudio.microsoft.com/downloads/) and install visual studio. After installation ensure that you select to install **Desktop Development with C++** in the workloads section.

### Install Python 
[Download](https://www.python.org/downloads/) and install the newest version of Python (**Must be 64 bit**)

### Install dependencies
In your virtual environment install the dependecies. You can do so by running the command ```pip install -r requirements.txt``` (make sure PIP and Python are added to your systems environment variables)

## Running the Application
In order to locally run the application you can open your terminal and navigate to the directory contaning all of the code (this directory should include the ```manage.py``` file). In your terminal run the command ```python manage.py runserver```. The output should look like this: 

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 02, 2020 - 23:12:42
Django version 3.0.7, using settings 'TasksApp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

In your web browser copy and paste the text after ```Starting development server at``` (in this case the text is ```http://127.0.0.1:8000/```). You can choose to run your local server off of a different port by adding a command line argument after the runserver command (```python manage.py runserver PORT_NUMBER```)


## Authors
[**Alexei Ivanov**](https://github.com/aivan6842) - Back End <br/>
[**Nicholas Sturk**](https://github.com/nicholasturk) - Front End

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
