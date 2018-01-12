from django.db import models
from django.core.urlresolvers import reverse


class Account(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('account_cbv: account_edit', kwargs={'pk': self.pk})

