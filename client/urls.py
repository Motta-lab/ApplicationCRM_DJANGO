from django.urls import path,include
from . import views
urlpatterns = [
    path('/<str:pk>/', views.list_clients,name='client'),
]
