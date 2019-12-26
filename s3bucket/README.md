

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/
```

2. Check into the cloned repository
```
$ cd s3report
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

4. Configure AWS CLI
```
$ aws configure
```

5. Create a bucket on AWS Dashboard and update it on the `app.py` file on line 10.

6. Run the application
```
$ python app.py
```

7. Navigate to http://localhost:5000/
