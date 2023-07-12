from django.urls import path
from .views import home

app_name = "AboutUs"

urlpatterns = [
    path("", home, name="home"),

]