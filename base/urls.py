from django.contrib import admin
from django.urls import path
from .views import * 
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('a/', index, name='a'),
    path('', TaskList.as_view(), name="tasks"),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(), name='delete'),
]
