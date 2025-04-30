from django.urls import path
from bands import views

urlpatterns = [
    path('musician/<int:musician_id>/', views.musician, name='musician'),
    path('musicians/', views.musicians, name='musicians'),
    path('All_Musicians/', views.all_musicians, name='all_musicians'),
]