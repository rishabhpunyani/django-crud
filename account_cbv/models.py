from django.db import models


class Account(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.title)

