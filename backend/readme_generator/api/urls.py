from django.urls import path
from .views import ReadMeGeneratorView,ReadmeDownloadView


urlpatterns = [
    path('requests/', ReadMeGeneratorView.as_view(), name='readme-generator'),
    path('download/', ReadmeDownloadView.as_view(),name='download-readme')
]