from django.urls import path, include
from . import views
urlpatterns = [
     path("", views.first_page),
     path("ivsegdabudu", views.second_page, name="scp")
]