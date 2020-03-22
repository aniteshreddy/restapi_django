from django.urls import path,include
from .views import article_list,APIviewArticle
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('article',APIviewArticle,basename='article')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('article/',article_list),
]
