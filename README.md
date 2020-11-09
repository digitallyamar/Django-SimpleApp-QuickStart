# Django-SimpleApp-QuickStart

NOTE: This repo uses class based view and renders html using a HTML template file.

## Features

- Simple Todo App with corresponding model.
- Supports Editing of Model data using Admin panel.
- Support for created_by field with default set to current_user in case left empty.

## How this repo was created in the beginning?

Step 1: Create a directory to hold our Django project.

    mkdir Django-SimpleApp-QuickStart
    cd Django-SimpleApp-QuickStart

Step 2: Create Python3 virtual enironment and activate it.

    python3 -m venv venv
    source venv/bin/activate

Step 3: Install Django in using pip in the venv.

    pip install Django
    pip install django-crum

Step 4: Create Django project in the current directory.

    django-admin startproject SimpleProject .

    [Notice the period (.) at the end of the command above. Need it to create project in the current directory itself]

Step 5: Create a simple app

    django-admin startapp app

    With this, you should have a dir structure that looks like this:
    > tree -L 1
    >   .
        ├── app
        ├── manage.py
        ├── SimpleProject
        └── venv

Step 6: But for Django project to know the existence of this app, we need to update entry in settings.py of the SimpleProject folder.

    Make an entry of our app in the INSTALLED_APPS list as shown below:

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

Step 7: Next, create and apply migrations to our project using the command:

    python3 manage.py makemigrations

    python3 manage.py migrate

    A this point in time, create a superuser(admin) for Django using command:

    python3 manage.py createsuperuser

Step 8: We can now run our Django server using the command:

    python3 manage.py runserver

    If you now visit the link [127.0.0.1:8000](127.0.0.1:8000), you should be greeted with Django Welcome Page!

    You can also login to the Admin panel by visiting the link [[127.0.0.1:8000/admin](127.0.0.1:8000/admin/) and using the superuser credentials created earlier.


## Where to go from here?

As you can see, even though we included our Django app, nothing much happened there. This repo is still working just like our other repo "Django-Simple-QuickStart" that has no app in it. 

#### So what went wrong?

Well the thing is, we need to do a lot of things from here to get our app working. It needs to get its own DB model, its own view and its own url set as well. Until that is done, we cant make much use of our app files.

But since they are specific to the type of app we are creating, it will be heavily customized froom Step 9 onwards.


Step 9: Let us assume that our app is a todo app. 
        So, we need to create two fields in our app to accept to strings of data per task.

        1. Title of the todo task
        2. Description of the task

        Let us then create a model for our app in the app folder's models.py
        We will also create a view for our app using the views.py file
        We will need to create a HTML template file as part of this view creation.
            - Created under templates/app directory.
        
        Finally, we will bind the view to home page url using urlpatterns list update.

            - To do this, create a urls.py file in our app folder and add appropriate details there.
            - Update urls.py file in our project folder to point to the above app folder's urls.py file.

Step 10: Once these are in place, we can create migration files using the command:

        python3 manage.py makemigrations

Step 11: Now, let us apply the migrations thus created using the command:

        python3 manage.py migrate

Step 12: With these in place, let us now run the server again:
        python3 manage.py runserver

        And now if we visit the url [127.0.0.1:8000](127.0.0.1:8000) you should see webpage rendered using template html file.
