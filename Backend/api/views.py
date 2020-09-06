from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from . import models
from . import serializers
from django.contrib.auth.models import User


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class MoviesViewset(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['POST'])
    def rate(self, request, pk=None):
        if 'stars' in request.data and 1 <= int(request.data['stars']) <= 5:
            stars = request.data['stars']
            movie = models.Movie.objects.get(pk=pk)
            user = request.user
            if request.user.is_anonymous:
                user = User.objects.get(pk=1)
            try:
                rating = models.Rating.objects.get(user=user, movie=movie)
                rating.stars = stars
                rating.save()
                serializer = serializers.RatingSerializer(rating, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception:
                rating = models.Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = serializers.RatingSerializer(rating, many=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response({'stars': 'You need to enter this field correctly!'}, status=status.HTTP_400_BAD_REQUEST)


class RatingsViewset(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
