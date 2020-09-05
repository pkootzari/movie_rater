from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model) :
    title = models.CharField(max_length=30),
    description = models.TextField()

    class Meta:
        unique_together = ['title']
        indexes = [
            models.Index(fields=['title', 'description'])
        ]

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    class Meta:
        unique_together = ['movie', 'user']
        indexes = [
            models.Index(fields=['movie', 'user'])
        ]
