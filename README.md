# CodeLeap Backend Test

CodeLeap Backend Test - A Django REST Framework API for managing CRUD operations.

## Installation

```bash
git clone https://github.com/michel-mendes/codeleap-backend-test.git
cd codeleap-backend-test
python -m venv env
source env/bin/activate   # on Windows use: 'env\Scripts\activate'
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
