from django.urls import path
from . import views
from spectralImages.views import fetchDataFromSelected, fetchMaskedDataFromSelected

urlpatterns = [
    path("", views.home, name='spectralImages-home'),
    path('fetchDataFromSelected/<image>/', fetchDataFromSelected, name='select_item_view'),
    path('fetchMaskedDataFromSelected/<image>/',
         fetchMaskedDataFromSelected, name='select_masked_item_view'),

]
