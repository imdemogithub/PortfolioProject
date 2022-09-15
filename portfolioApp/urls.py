from django.urls import path
from .views import index

urlpatterns = [
    path('first_page/', index, name="first_page"),
]