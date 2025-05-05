from django.urls import path
from transactions import views

app_name='tran'
urlpatterns = [
    path('list/',  views.list, name='list'),
    path('create/',  views.create, name='create')
]
