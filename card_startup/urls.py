from django.urls import path
from card_startup import views

urlpatterns = [
    path('list/',views.CardListView.as_view(), name='card-list'),
    
]
