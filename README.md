# example-flask

## Github Action Build Status
![Deploy Python To IBM CF](https://github.com/Learn-And-Earn/example-flask/workflows/Upload%20Python%20Package/badge.svg)

REST API written in Python Flask & DB2

## Pre-requisites
  - Download & install [Python 3.6](https://www.python.org/downloads/)
  - Download & install [Pipenv](https://docs.pipenv.org/)
   ```cmd
    python -m pip install -U pip 
    pip3 install pipenv
   ```

## Installation

  ```cmd
  # Clone the repository 
  # Change into the directory
  cd example-flask
  # Install all required dependencies with
  pipenv install --deploy --skip-lock
  # Activate the project virtual environment
  pipenv shell
  # Create an local .env file and replace with the relevant values
  copy .env.sample .env
  ```
  You can also set the enviroment variables explicity (OPTIONAL)
  
  ```cmd
  set Build_ENV=development
  set PORT=9000
  ```
## vscode setup
  - Install python from vscode extensions market place (ctrl+shift+x) [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - Open the command palette in visual studio (ctrl+shift+P) type ```>Python: Select Interpreter``` 
  - Choose the python interpreter of virtual env ```('example-flask': pipenv)```
  - Once that is done check the .vscode folder settings.json if the ```python.pythonPath``` points to your virtual env.
  - To debug the applictaion open Run (ctrl+shift+D) and click on the play button besided Run with Python: Flask selected in the drop down.
  
## Running the application

  **Start the app in virtual env shell**
  ```cmd
  python run.py
  ```

## Usage

**Blue-Prints Specifications**
  - GET: /                    - app
  - GET: /api/v1/model/       - controller 
  - GET: /api/v1/model/id     - controller 
  - POST: /api/v1/model/id    - controller 
  - PUT: /api/v1/model/id     - controller
  -DELETE: /api/v1/model/id   - controller

**Example**
curl http://localhost:{APP_PORT}/api/v1/model/

## Running the application as a Docker container

 ```cmd
 cd example-flask
 # Build the docker image 
 docker build -t shra012/example-flask:1.0 .
 # Run the docker container and put the port as specified in the .env file
 docker run -d -p 5000:5000 --name example-flask -e PORT=5000 -e Build_ENV=development shra012/example-flask:1.0
 # Check the logs
 docker logs -f example-flask
 # Cleaup the container
 docker stop example-flask && docker rm example-flask
 ```

## Author

Shravankumar Nagarajan
