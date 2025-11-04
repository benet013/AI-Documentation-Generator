from django.urls import path
from .views import ReadMeGeneratorView


urlpatterns = [
    path('requests/', ReadMeGeneratorView.as_view(), name='readme-generator'),
]