from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # Funcão criada para, quando criada a escolha, redireciona para a detailview da escola
    def get_absolute_url(self):
        return reverse("new_app:detail", kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students')

    def __str__(self):
        return self.name
