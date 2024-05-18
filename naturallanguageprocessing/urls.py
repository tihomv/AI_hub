from django.urls import path, include
from naturallanguageprocessing import views

urlpatterns = [
    path('', views.index, name='index'),
]
