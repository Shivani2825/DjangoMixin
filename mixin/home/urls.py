from django.contrib import admin
from  django.urls import path
from .views import *

urlpatterns = [
    path('bookapi/',Booklist.as_view()),
    path('bookcreate/',BookCreate.as_view()),
    path('bookretrieve/<int:pk>/',BookRetrieve.as_view()),
    path('bookupdate/<int:pk>/',BookUpdate.as_view()),
    path('bookdelete/<int:pk>/',BookDelete.as_view()),
     
]

