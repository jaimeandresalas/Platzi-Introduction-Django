from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
# Las clases dentro del modelo significan tablas dentro de la Base de Datos


class Question(models.Model):
    # Dentro de la clase definimos los atributos que son las columnas de la tabla
    id
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
