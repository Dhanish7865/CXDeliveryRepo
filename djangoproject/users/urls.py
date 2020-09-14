from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('even/', views.EvenUsersView.as_view(), name="even"),
    path('all_records/', views.AllRecords.as_view(), name="all_records"),
]