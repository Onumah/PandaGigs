from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('create/', views.create, name="Create"),
    path('show/<str:job_id>/', views.show, name="Show"),
    path('manage/', views.manage, name="Manage"),
    path('manage/edit/<str:job_id>/', views.edit, name='Edit'),
    path('manage/delete/<str:job_id>/', views.delete, name='Delete'),
]