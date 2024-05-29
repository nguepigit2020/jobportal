# jobportal
## Below are the steps you need to follow before being able to execute the code.
* Setup a virtual environment

     ``python -m venv my_env`` if you have already ``virtualenv`` installed

     ``source my_env/bin/activate`` to activate the virtual environment


* Move to ``jobportal`` folder and run the requirement to install all dependencies
    
   ``pip install -r requirement.txt``

* Setup the Mysql database

   * Create a user nguepi which full privilege 
  
     ``CREATE USER 'nguepi'@'localhost' IDENTIFIED BY 'Ng123';``
  
      ``GRANT ALL PRIVILEGES ON jobportal.* TO 'nguepi'@'localhost';``
  
      ``FLUSH PRIVILEGES;``

   * Log in to MySQL using ``sudo mysql -u nguepi -p Ng123``
   * Create a table ``jobportal`` using ``CREATE DATABASE jobportal;
`` 
* Make migrations

   ``python manage.py makemigrations``

   ``python manage.py migrate``
* Now you can run the api and start performing some request

  ``python manage.py runserver``
* After this step, you will be able to use the three ulrs below to perform GET, POST, PUT and DELETE the item:

   ``"jobseekers": "http://127.0.0.1:8000/api/jobseekers/",``

  ``"adminusers": "http://127.0.0.1:8000/api/adminusers/",``

   `` "jobs": "http://127.0.0.1:8000/api/jobs/"``
### Example: to get all jobs which,
  
 Make a get request which this url ``http://127.0.0.1:8000/api/jobs/``

### Example: to update the job which id 3,

 Make a put request which this url ``http://127.0.0.1:8000/api/jobs/3/``

### Example: to get the job which id 3,

  Make a get request which this url ``http://127.0.0.1:8000/api/jobs/3/``

### Example: to delete the job which id 3,

 Make a delete request which this url ``http://127.0.0.1:8000/api/jobs/3/``
