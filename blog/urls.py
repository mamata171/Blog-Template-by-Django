from django.urls import path
from blog import views

urlpatterns = [
        path('', views.home, name='home'),
        path('blogs',views.blogs,name="blog"),
        path('blogpost/<str:slug>',views.blogpost,name = "blogpost"),
        path('contact',views.contact,name="contact"),

        ]               