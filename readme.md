django-admin startproject my_tennis_club # on terminal 


ls
# navigate to the this directory
cd .\my_tennis_club\
python manage.py runserver # on terminal

ctrl+c to stop the server 
# <!-- rename the app member --> #
python manage.py startapp members

Django creates a folder named members in my projec

# views.py


# run this commanad after creating 1st html file and also after adding project name(members) in setting.py

python manage.py migrate

<!-- next step is to create the models (Table ) -->
# migrate
Now when we have described a Model in the models.py file, we must run a command to actually create the table in the database.

Navigate to the /my_tennis_club/ folder and run this command:

# python manage.py makemigrations members

Note that Django inserts an id field for your tables, which is an auto increment number (first record gets the value 1, the second record 2 etc.), this is the default behavior of Django, you can override it by describing your own id field.

The table is not created yet, you will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder.

Run the migrate command:
# python manage.py migrate

<!-- View SQL: -->

# python manage.py sqlmigrate members 0001

<!-- insert Data -->
run
# python manage.py shell
>>>from members.models import Member
>>>Member.objects.all()

>>>member = Members(firstname='Emil', lastname='Refsnes')
>>> member.save()
#to check the values
Members.objects.all().values()

# to add multiple records
>>> member1 = Members(firstname='Tobias', lastname='Refsnes')
>>> member2 = Members(firstname='Linus', lastname='Refsnes')
>>> member3 = Members(firstname='Lene', lastname='Refsnes')
>>> member4 = Members(firstname='Stale', lastname='Refsnes')
>>> member5 = Members(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
...   x.save()

to check saved values
Members.objects.all().values()

<!-- update Records -->
from members.models import Members
x = Members.objects.all()[4]
x.firstname
<!-- update name  -->
x.firstname = "Meri"
x.save()

execute and check if members table update
Members.objects.all().values()


<!-- Delete recodrs -->

>>> from members.models import Members
>>> x = Members.objects.all()[5]
>>> x.firstname
>>> x.delete()


<!-- after updating the model members -->
python manage.py makemigrations members
after select option 2 
rerun   -->  python manage.py migrate

<!-- adding the new values -->
python manage.py shell
rom members.models import Member
>>> x = Member.objects.all()[0]
>>> x.phone = 5551234
>>> x.joined_date = '2022-01-05'
>>> x.save()

<!-- to create the admin.py file -->

python manage.py startapp myword

<!-- to create super user -->
python manage.py createsuperuser

<!-- Include models to admin  -->
add this code in 
/memeber/admin.py

from django.contrib import admin
from .models import Members

# Create your models here.
admin.site.register(Members)
# Register your models here.
