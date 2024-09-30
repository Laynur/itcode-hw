from django.urls import path
from tmp.views import index,list_students, list_groups

urlpatterns = [
    path('', index),
    path('list_students/',list_students),
    path('list_groups/',list_groups),
]