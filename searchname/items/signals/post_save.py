from django.db.models.signals import post_save
from django.dispatch import receiver

from items.models import Item


@receiver(post_save, sender=Item)
def create_hash_id(sender, instance, created, **kwargs):
    if not instance.hash_id:
        instance._create_hash_id()
