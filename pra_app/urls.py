from django.contrib import admin # type: ignore
from django.urls import path , include# type: ignore
from pra_app import views 
urlpatterns = [
    path('',views.read, name="passread"),
    path('create',views.create, name="create"),
    path('update/<int:id>',views.update , name="update"),
    path('delete/<int:id>',views.delete, name="delete"),
    path('search',views.search, name="search"),
]
