from django.urls import path

from practiceapp import views

urlpatterns = [
    path('', views.home),

]