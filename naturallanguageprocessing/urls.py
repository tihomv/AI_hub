from django.urls import path, include
from naturallanguageprocessing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_view, name='chat'),
]
