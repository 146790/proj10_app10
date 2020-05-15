from django.urls import path
from . import views

app_name='app10'

urlpatterns =[
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete,name='delete'),
]

