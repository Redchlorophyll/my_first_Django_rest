from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<int:pk>/', views.article_detail),
    path('class/', views.ArticleAPIView.as_view()),
    path('class/<int:pk>/', views.ArticleDetails.as_view()),
    path('generic/', views.GenericAPIView.as_view()),
    path('generic/<int:id>', views.GenericAPIView.as_view()),
]
