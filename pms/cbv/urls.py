from django.contrib import admin
from django.urls import path,include
from blog.views import home
from .views import *
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('create/',FoodCreateView.as_view(),name='foodcreate'),
    path ('list/',FoodListView.as_view(),name='foodlist'),
    path('delete/<int:pk>',FoodDeleteView.as_view(),name='fooddelete'),
    path('update/<int:pk>',FoodUpdateView.as_view(),name='foodupdate'),
    path('detail/<int:pk>',FoodDetailView.as_view(),name='fooddetail'),
    path('addfile/',AddFileView.as_view(),name='addfile'),
    path('filelist/',FileListView.as_view(),name='filelist'),

]
