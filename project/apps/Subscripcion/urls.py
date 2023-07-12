from django.urls import path
from .views import home

app_name = "Subscripcion"

urlpatterns = [
    path("", home, name="home"),

]