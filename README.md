# Netflix-Clone-Django
Netflix Clone in Django

You(Admin) can upload your movies based on age and movie_choices.

Users can register, login and watch their movies based on their choices and profiles.


## Installation
Set up your virtualenvironment.
Use the package manager pip to install the requirements.
```bash
pip install requirements.txt
```

## Usage
```python
python manage.py makemigrations
python manage.py migrate
```

Create an admin:
```python
python manage.py createsuperuser
```
Enter the credentails to create an admin


Run the project in localhost:
```python
python manage.py runserver
```

## Description
This Django App has two apps installed.

### 1.users

User Model, user authorization and authentication are all handled in this app.

AbstractUser model is used for user Model. So you will login using email of the user.

#### Urls
```
http://127.0.0.1:8000/auth/login
http://127.0.0.1:8000/auth/sign-up
```

### 2.base

This app handels the user profile and their choices. 
Plus this app also handels the users to watch their movies.

Movie, Profile, Video models are created in the models.py

#### Urls
Home page:
```
http://127.0.0.1:8000/
```

To show the list of the profiles created by the user:
```
http://127.0.0.1:8000/profile-list/
```

To create a profile:
```
http://127.0.0.1:8000/profile/create/
```


To show the list of the movies:
```
http://127.0.0.1:8000/watch/user_profile_id
```


To Show the details of the movie:
```
http://127.0.0.1:8000/movie/detail/movie_id
```

To watch the specified movie:
```
http://127.0.0.1:8000/movie/play/movie_id
```


You can also use the admin panel to upload movies, create users and their profiles.
