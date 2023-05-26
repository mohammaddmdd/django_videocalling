# django_videocalling
## Build a Scalable Realtime Video Chat App with Agora in Django
## Features:
- Inviting a user to a video call with an incoming call notification
- Returning the appropriate feedback if the user is offline
- Terminating calls before they’re answered
- Declining/rejecting calls
- Accepting/receiving calls

## Installation: 

Clone the repository:

`git clone https://github.com/mohammaddmdd/django_videocalling`

Create a virtual environment and activate it:

`python -m venv env`

`source env/bin/activate   # On Unix or Linux`

`env\Scripts\activate.bat  # On Windows`

Install the requirements:

`pip install -r requirements.txt`

Update the environment variables:

- Open the .env file located at the root of your project folder.

- Add the credentials you obtained from Agora:

  ```DJANGO_SECRET_KEY=''
  DB_NAME=''
  DB_USER=''
  DB_PASSWORD=''
  DB_HOST=''
  DB_PORT=''
  AGORA_APP_ID=''
  AGORA_APP_CERTIFICATE='' 

Set up the database:

`python manage.py migrate`

Create superuser:

`python manage.py createsuperuser`

Run the server:

`python manage.py runserver`
##
## Usage:

Start the Django development server from your terminal:

Open two different browsers or two instances of the same browser, with one instance in incognito mode, and go to `http://127.0.0.1:8000`

If you are not already logged in, you will be presented with the Django admin login page. Log in using your superuser credentials.

After successful login, you will be taken to the Django admin dashboard. Click on the "VIEW SITE" link at the top right to navigate to the video call page.

In each of the browsers you opened, the other users registered on the application will be displayed.

In one browser, you can call the user who is logged in and on the other browser by clicking the button that bears their name.

The other user will be prompted to click the "Accept" button to fully establish the call.

