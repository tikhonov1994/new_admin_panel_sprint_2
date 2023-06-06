from django.urls import path
from movies.api.v1.views import MovieDetailApi, MoviesListApi

urlpatterns = [
    path('movies/', MoviesListApi.as_view()),
    path('movies/<uuid:pk>', MovieDetailApi.as_view()),
]
