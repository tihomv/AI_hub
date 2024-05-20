from django.urls import path, include

from AI_hub import settings
from home import views

from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_view, name='uploadview'),
]
