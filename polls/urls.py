from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='homepage'),
    path("about",views.about,name='aboutme')
]