from django.urls import path

from Expenses import views

urlpatterns = [
    path('expenses/', views.index, name='home'),
    path('add_expense/', views.add_expense, name='add_expense'),
]