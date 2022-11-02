from django.db import models

class Dato(models.Model):
    rol = models.CharField(max_length = 20)
    name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.CharField(max_length=5)
    sign = models.CharField(max_length = 40)

    def __str__(self):
        return f'{self.rol}'
