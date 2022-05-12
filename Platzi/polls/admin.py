from django.contrib import admin
# Registrando modelos en el admin
from .models import Question
admin.site.register(Question)
