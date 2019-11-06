from django.contrib import admin

# Register your models here.
from django.contrib import admin
from eventform.models import events
from eventform.models import Registration

admin.site.register(events)
admin.site.register(Registration)