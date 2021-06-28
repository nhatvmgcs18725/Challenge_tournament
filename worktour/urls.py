from django.urls import path
from .views import Post, ListpostDetail
from . import views

app_name = 'worktour'

urlpatterns = [


    path('', views.ttest, name='ttest'),
    path('<str:chatchit>/', views.room, name='room'),

]
"""path('<int:pk>/', ListpostDetail.as_view(), name='listPost'),
    path('', Post.as_view(), name='Post'),"""
