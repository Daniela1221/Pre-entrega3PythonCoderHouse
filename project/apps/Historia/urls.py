from django.urls import path
from .views import home

app_name = "Historia"

urlpatterns = [
    path("", home, name="home"),

]