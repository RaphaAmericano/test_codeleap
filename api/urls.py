from django.urls import path
from . import views

urlpatterns = [
    path('careers', views.careers, name='careers'),
    path('careers/<int:id>', views.careers_param_request, name='careers_param_request')
]