from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.my_view, name='hello_world'),
]