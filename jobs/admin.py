from django.contrib import admin
from .models import City, Company, Country, Job, Language, Skill

# Register your models here.
admin.site.register(Language)
admin.site.register(Skill)
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Job)
