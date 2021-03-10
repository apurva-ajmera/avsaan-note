from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Note
from django.utils.text import slugify

def unique_slug_generator(instance):
    slug = ''

    if instance.slug == '':
        slug = instance.name
        slug = slugify(slug)

        if Note.objects.filter(slug=slug).exists():
            last = Note.objects.last()
            slug = slug + ' ' + str(last.id)

    slug = slugify(slug)
    return slug

@receiver(pre_save, sender=Note)
def create_profile(sender, instance, **kwargs):
    instance.slug = unique_slug_generator(instance)
    return
