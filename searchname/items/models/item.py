from django.db import models

from django.contrib.sites.models import Site


class ItemManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related('site', )


class Item(models.Model):

    site = models.ForeignKey(
        Site,
    )

    name = models.CharField(
        max_length=128,
        verbose_name='이름',
    )

    slug = models.SlugField(
        blank=True,
        null=True,
    )

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()

    class Meta:
        ordering = ['name', ]
        unique_together = (
            ('site', 'name', 'slug', ),
        )

    def __str__(self):
        return self.name

    def _create_hash_id(self):
        from items.utils.hashids import get_encoded_hashid

        self.hash_id = get_encoded_hashid(self)
        self.save()
