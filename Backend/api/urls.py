from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('movies', views.MoviesViewset, basename='movieapi')
router.register('ratings', views.RatingsViewset, basename='ratingapi')
router.register('users', views.UserViewset, basename='userapi')

urlpatterns = [
    path('', include(router.urls)),
]