from django.urls import path
from . import views

app_name='google'
urlpatterns = [
    path('', views.HelloView.as_view()),
    path('login/', views.GoogleView.as_view()),
]
