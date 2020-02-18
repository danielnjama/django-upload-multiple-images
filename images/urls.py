# articles/urls.py
from django.urls import path

from .views import ArticleListView, ArticleDetailView
from . import views

urlpatterns = [
	path('home',views.post,name='post'),
    path('mypage',views.mypage,name='mypage'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article_detail'), # new
    path('', ArticleListView.as_view(), name='article_list'),

]





'''
from django.urls import path
from . import views

urlpatterns = [
    path('',views.post,name='post'),
    path('mypage',views.mypage,name='mypage'),
]

'''