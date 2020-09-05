from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model) :
    title = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        unique_together = ['title']
        indexes = [
            models.Index(fields=['title', 'description'])
        ]

    def __str__(self):
        return self.title


class Rating(models.Model):
    RATING_CHOICES = [
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    ]
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        unique_together = ['movie', 'user']
        indexes = [
            models.Index(fields=['stars']),
            models.Index(fields=['movie']),
            models.Index(fields=['user']),
        ]

    # def __str__(self):
    #     return '{} gave {} starts for movie {} '.format(self.user.username, self.stars, self.movie.title)
