from django.contrib import admin
from .models import Question, Choice
# Registrando modelos en el admin
"""from .models import Question
admin.site.register(Question)"""


class ChoicesInline(admin.StackedInline):
    model = Choice
    can_delete = True
    verbose_name_plural = 'choices'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoicesInline,)
