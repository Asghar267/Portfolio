from django.db import models


# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.EmailField(max_length=500, null=True)

    def __str__(self):
        return self.name