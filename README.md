#FakeDataWebService
## Setup
1. Install dependencies `pip install -r requirements.txt`
2. Specify .env with .env.example.
3. Setting up tailwind environment with `python manage.py tailwind install`
3.1. Run `python manage.py tailwind start` for JIT css updating during development.
3.2. Run `python manage.py tailwind build` to create production build.
3.3. More details: https://django-tailwind.readthedocs.io/en/latest/usage.html