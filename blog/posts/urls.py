from django.urls import path
from . import views


urlpatterns = [
	path('users/', views.UserList.as_view()),
	path('users/<int:pk>/', views.UserDetail.as_view()),
	path('<int:pk>/', views.PostDetail.as_view()),
	path('', views.PostList.as_view()),
]