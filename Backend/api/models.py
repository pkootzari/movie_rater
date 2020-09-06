from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model) :
    title = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        unique_together = ['title']
        indexes = [
            models.Index(fields=['title', 'description'])
        ]

    def num_of_ratings(self):
        ratings = self.ratings.all()
        return len(ratings)

    def avg_ratings(self):
        ratings = self.ratings.all()
        if len(ratings) == 0:
            return 0
        return sum([rating.stars for rating in ratings]) / len(ratings)

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
    stars = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ['movie', 'user']
        indexes = [
            models.Index(fields=['stars']),
            models.Index(fields=['movie']),
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return '{} gave {} starts for movie {} '.format(self.user.username, self.stars, self.movie.title)
