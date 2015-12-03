from django.db import models

from django.contrib.sites.models import Site


class ItemManager(models.Manager):
    pass


class Item(models.Model):

    site = models.ForeignKey(
        Site,
    )

    name = models.CharField(
        unique=True,
        max_length=128,
        verbose_name='이름',
    )

    slug = models.SlugField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()

    class Meta:
        pass

    def __str__(self):
        return self.name
