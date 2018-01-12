from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class Account(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.title)

    def title_slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('account_slug: account_edit', [self.slug])

