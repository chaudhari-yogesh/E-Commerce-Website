
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="blogindex"),
    path("blogpost/<int:blogid>", views.blogpost, name="blogPost") 
]
