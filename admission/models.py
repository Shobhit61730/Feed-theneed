from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    def _str_(self):
        return self.name