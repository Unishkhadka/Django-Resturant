from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, default='')
    cmnt = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
