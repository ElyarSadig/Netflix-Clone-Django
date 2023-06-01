from django.db import models
import uuid

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)


class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    age_limit = models.CharField(max_length=150, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=150, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')


class Video(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title



