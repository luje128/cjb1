from django.contrib import admin

<<<<<<< HEAD
from apps.users.models import User, Address

admin.site.register(User)
admin.site.register(Address)
=======
# Register your models here.
from django.contrib import admin
from apps.users.models import Test

admin.site.register(Test)
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
