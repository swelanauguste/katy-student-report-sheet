#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

# python manage.py makemigrations
# python manage.py migrate
# python manage.py flush --no-input
# python manage.py createsuperuser --username kingship --email kingship.lc@gmail.com --no-input
# python manage.py collectstatic --no-input
# # python manage.py add_category_list
# python manage.py add_subject_list
# python manage.py add_year_class
# python manage.py add_fake_teachers
# python manage.py add_fake_students
# python manage.py add_fake_remarks

exec "$@"