from django.urls import path

from objectapp import views

urlpatterns = [
    path('',views.home),


]