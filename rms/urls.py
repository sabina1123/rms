from django.urls import path, include
from .views import *
urlpatterns = [
    path('categories/',CategoryList.as_view()),
    path('categories/<pk>',CategoryDetail.as_view())
]