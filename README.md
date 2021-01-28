# ECell-Website

Steps to run the server:
￼￼
@

1. Clone the project and cd into root folder
2. Create virtualenvironment with the name "venv" and enter using 'source venv/bin/activate'
3. Install the requirements using 'pip install -r requirements.txt'
4. Create a local file "local.sh"
    a. Within "local.sh" add "export SECRET_KEY='random_string'"
    b. Add "export DEBUG_SETTINGS=True"
5. Run the command 'source local.sh'
6. Run the command 'python3 manage.py runserver'
