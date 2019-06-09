# Encuestas

Aplicación de encuestas (de la documentación oficial de Django) en castellano.

https://medium.com/@qazi/how-to-deploy-a-django-app-to-heroku-in-2018-the-easy-way-48a528d97f9c

«How to Deploy a Django App to Heroku in 2018… The Easy Way»

Las únicas instrucciones que me han servido para desplegar Django en Herok:

================================================================================

Step 1. Create a Procfile in your project root

Procfile

web: gunicorn project_name.wsgi

================================================================================

Step 2. Do this in your app/settings.py

app/settings.py

(arriba de todo): import django_heroku 

(abajo de todo): django_heroku.settings(locals())

================================================================================

Step 3. Then do this in your command line (bash)

pip install gunicorn

pip install django-heroku

pip freeze > requirements.txt

heroku login

heroku create

heroku addons:create heroku-postgresql:hobby-dev

git add .

git commit -m "Ready to heroku this sucker in the face."

git push heroku master

heroku run python manage.py migrate

================================================================================

https://thawing-brook-47205.herokuapp.com/