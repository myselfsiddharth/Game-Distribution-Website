import os

for i in range(1):
    os.system("py -m pip install django")
    os.system("py -m pip install django-admin-interface")
    os.system("py manage.py runserver")