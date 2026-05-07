from django.contrib import admin

from .models import hobbies
from .models import Interests

# register the models in the admin
admin.site.register(hobbies)
admin.site.register(Interests)







