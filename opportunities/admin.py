from django.contrib import admin
from .models import Application, Opportunity, Organization

admin.site.register(Application)
admin.site.register(Opportunity)
admin.site.register(Organization)