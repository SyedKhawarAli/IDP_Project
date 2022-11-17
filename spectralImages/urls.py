from django.urls import path
from . import views
from spectralImages.views import fetchDataFromSelected

urlpatterns = [
    path("", views.home, name='spectralImages-home'),
    path('fetchDataFromSelected/<image>/', fetchDataFromSelected, name='select_item_view'),
]
