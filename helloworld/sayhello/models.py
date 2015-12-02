from django.db import models

# Create your models here.
class SayHello(models.Model):
    person_name = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.person_name
