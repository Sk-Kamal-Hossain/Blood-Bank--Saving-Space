from django.contrib import admin
from .models import Register
from .models import Camps
from .models import Donation

# Register your models here.

admin.site.register(Register)
admin.site.register(Camps)
admin.site.register(Donation)

