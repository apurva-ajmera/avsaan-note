from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone

class Note(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    slug = models.SlugField()
    name = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    extra_information = RichTextField()
    category = models.CharField(max_length=30, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'slug':self.slug})
