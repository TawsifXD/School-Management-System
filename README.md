# School Management System
A school management project in Django would involve creating a web application that helps manage various aspects of a school, such as student enrollment, class schedules, teacher assignments, and grades.


# Installation 
1. go to the project folder
2. create `.env` for project

**command to create envarment for project**
``` 
python -m venv env
```

3. then just active `.env` 

**command to active envarmant**
``` 
cd env/scripts/activate
```

4. Install requirements packege

**command to install requirements packege**
``` 
pip install -r requirements.txt
```

5. Then just Migrate the project

**command to migrate**
```
python manage.py migrate
```
6. create a superuser
**command to create a superuser**
```
python manage.py createsuperuser
```

7. Then run the project 
```
python manage.py runserver
```


# Admin Login
When you run migrate, a superuser is created.
```
username: admin
password: admin123
```
# Roadmap
To build a fully fledged open source school management.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
[MIT](https://github.com/TawsifXD/School-Management-System/blob/master/LICENSE).
