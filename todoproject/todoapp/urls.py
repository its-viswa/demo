from django.contrib import admin
from . import views

from django.urls import path

urlpatterns = [
    path('', views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name="update"),
    path('abc/',views.TaskListviews.as_view(),name="abc"),
    path('details/<int:pk>/',views.Detailview.as_view(),name='details'),
    path('updateview/<int:pk>/',views.Updateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.Deleteview.as_view(),name='deleteview'),
]
