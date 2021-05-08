from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('artikel', views.GenericViewSetTwo, basename='artikel')

urlpatterns = [
    path('', views.article_list),
    path('<int:pk>/', views.article_detail),
    path('class/', views.ArticleAPIView.as_view()),
    path('class/<int:pk>/', views.ArticleDetails.as_view()),
    path('generic/', views.GenericAPIView.as_view()),
    path('generic/<int:id>', views.GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
]
